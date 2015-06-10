import os
import glob
import json
import zipfile
import hashlib
import datetime
import contextlib

from fabric.api import env
from fabric.api import lcd
from fabric.api import task
from fabric.api import hide
from fabric.api import local
from fabric.api import execute
from fabric.api import settings

from nexiles.tools.api import get_api

from . import log
from . import utils
from . import environment

# We rely on these environment vars
env.nexiles.update(
    WT_HOST     = os.environ.get("WT_HOST"),
    WT_HOME     = os.environ.get("WT_HOME"),
    WTUSER      = os.environ.get("WTUSER"),
    WTPASS      = os.environ.get("WTPASS"),
    JYTHON_HOME = os.environ.get("JYTHON_HOME"),
)


if env.nexiles.WT_HOME:
    if not os.path.exists(env.nexiles.WT_HOME):
        log.warning("The path for WT_HOME is not accessible: {}", env.nexiles.WT_HOME)

    env.nexiles.update(
        WT_CODEBASE = os.path.join(env.nexiles.WT_HOME, "codebase"),
        WT_SRCLIB   = os.path.join(env.nexiles.WT_HOME, "src", "lib"),
        WT_WEB_INF  = os.path.join(env.nexiles.WT_HOME, "codebase", "WEB-INF")
    )


def api():
    """api() -> nexiles tools api object

    Get the nexiles tools api object."""
    return get_api(env.nexiles.WT_HOST, env.nexiles.WTUSER, env.nexiles.WTPASS)

##############################################################################
# Public Helpers
##############################################################################


def setup_classpath():
    """setup_classpath() -> None

    Sets up CLASSPATH to contain needed JAR files for compiling Windchill
    projects.
    """

    # collect all jars
    codebase_jars = glob.glob(os.path.join(env.nexiles.WT_CODEBASE, "*.jar"))
    webinf_jars = glob.glob(os.path.join(env.nexiles.WT_WEB_INF, "lib", "*.jar"))
    srclib_jars = glob.glob(os.path.join(env.nexiles.WT_SRCLIB, "*.jar"))

    # set the classpath
    all_jars = [env.nexiles.WT_CODEBASE, env.nexiles.WT_SRCLIB] + codebase_jars + webinf_jars + srclib_jars
    classpath = os.environ["CLASSPATH"] = ":".join(all_jars)
    return classpath


def get_package_env(which=None):
    """Return env for specific package"""
    if which is None:
        return env.nexiles

    return env.nexiles[which]


def generate_manifest(name, p, h=None):
    """ generate_manifest(name, p, h) -> mapping

    Generates a mapping used as the manifest file.

    :param name:      a dotted package name, as in setup.py
    :param p:         the zip file with package content.
    :param h:         optional hash function to use.
    :returns:         the path to the created manifest file.
    """
    if h is None:
        h = hashlib.sha256
    m = {}
    fh = m["files"] = {}
    order = []
    with zipfile.ZipFile(p) as zf:
        for fi in zf.filelist:
            order.append(fi.filename)

        hash_all = h()
        for fn in sorted(order):
            contents = zf.read(fn)
            hash_all.update(contents)
            fh[fn] = h(contents).hexdigest()

    m["name"] = name
    m["sum"]  = hash_all.hexdigest()
    m["date"] = datetime.datetime.now().isoformat()
    return m


def add_manifest(package, manifest, egg):
    manifest_resource = os.path.join(*package.import_name.split("."))
    manifest_resource = os.path.join(manifest_resource, "resources", "manifest.json")
    with zipfile.ZipFile(egg, "a") as zf:
        zf.writestr(manifest_resource, json.dumps(manifest))


def get_package_name(package, customer=None, python="2.7"):
    """ returns the egg filename (without the fs path),
        e.g. nexiles.gateway.appservice-1.0.0-py2.7-customer.egg
    """
    if customer:
        return "{}-{}-py{}-{}.egg".format(
            package.import_name,
            package.version,
            python,
            customer
        )
    return "{}-{}-py{}.egg".format(
        package.import_name,
        package.version,
        python
    )


@contextlib.contextmanager
def licensed_package(package, customer):
    """"""

    with file(package.license_module, "w") as f:
        f.write("""# -*- coding: utf-8 -*-
LICENSE = {
   "customer_id": "%s",
   "key":         "%s"
}
""" % (customer, package.urn))
        log.info("   Generated license module for {}".format(customer))

    yield

    log.info("   Removed license module for {}".format(customer))

    with hide("running"):
        local("git checkout {}".format(package.license_module))

    egg_name          = os.path.join(env.nexiles.build_dir, get_package_name(package))
    egg_name_customer = os.path.join(env.nexiles.build_dir, get_package_name(package, customer=customer))

    with hide("running"):
        local("mv {} {}".format(egg_name, egg_name_customer))

    log.info("   Adding package manifest to {} for {}.".format(egg_name_customer, customer))
    manifest = generate_manifest(package.package_name, egg_name_customer)
    add_manifest(package, manifest, egg_name_customer)

    package.setdefault("built_eggs", []).append(egg_name_customer)

##############################################################################
# Tasks
##############################################################################


@task
@utils.Requires(WT_HOME=str, WT_HOST=str, WTUSER=str, WTPASS=str)
def dump_env():
    """Print windchill specific environment."""
    execute(environment.dump)


@task
@utils.Requires(WT_HOME=str)
def classpath():
    """Print CLASSPATH used to build."""
    cp = setup_classpath()
    log.info("CLASSPATH={}".format(cp))


@task
@utils.Requires(build_dir=str, WT_HOME=str, WT_HOST=str, WTUSER=str, WTPASS=str, JYTHON_HOME=str)
def build_gateway_module(which=None):
    """Build gateway module."""
    if which is None:
        package = get_package_env()
        which = env.nexiles.package_name
    else:
        package = get_package_env(which)

    log.info("Building {} version {}".format(which, package.version))

    setup_classpath()

    for customer in package.customers:
        with licensed_package(package, customer):
            with lcd(package.package_dir), hide("running", "stdout"):
                log.info("   Building {} for {}".format(package.package_name, customer))
                local("jython setup.py bdist_egg --exclude-source-files -d {}".format(env.nexiles.build_dir))

    log.info("Built eggs:")
    for p in package.built_eggs:
        log.info("   {}".format(p))

# EOF

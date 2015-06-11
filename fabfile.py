import os
import logging

from fabric.api import env
from fabric.api import task
from fabric.api import hide
from fabric.api import local
from fabric.api import execute

from nexiles.fabric.tasks import log
log.setup_logging(level=logging.ERROR, logfile=None)

from nexiles.fabric.tasks import docs
from nexiles.fabric.tasks import utils
from nexiles.fabric.tasks import release
from nexiles.fabric.tasks import environment

PACKAGE_NAME = "nexiles.fabric.tasks"
PUBLIC_DIR   = "/Volumes/skynet-wt-10-2/ptc/Windchill_10.2/HTTPServer/htdocs/docs/{PACKAGE_NAME}".format(**globals())

env.nexiles.initialize(
    package_name  = PACKAGE_NAME,
    doc_public_dir=PUBLIC_DIR
)


@task
def version():
    """Print package version"""
    log.info("{} {}".format(env.nexiles.package_name, env.nexiles.version))


@task
def build():
    execute(docs.build)
    execute(docs.package)
    with hide("running", "stdout"):
        local("python setup.py clean sdist develop")


@task
def dist():
    execute(docs.publish)
    # execute(dist.dist)


@task
def full_monty():
    execute(build)
    execute(dist)
    execute(release.github)
    execute(release.pypi)

# EOF
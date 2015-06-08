import os

from fabric.api import env

from nexiles.fabric.tasks import docs
from nexiles.fabric.tasks import utils
from nexiles.fabric.tasks import release
from nexiles.fabric.tasks import environment

PACKAGE_NAME = "nexiles.fabric.tasks"
VERSION      = utils.get_version_from_setup_py()

ROOT_DIR     = os.path.abspath(os.path.dirname(__file__))
BUILD_DIR    = "{ROOT_DIR}/dist".format(**globals())

DIST_DIR     = "~/develop/nexiles/dist/{PACKAGE_NAME}/{PACKAGE_NAME}-{VERSION}".format(**globals())

SRC_PACKAGE  = "{BUILD_DIR}/{PACKAGE_NAME}-{VERSION}.tar.gz".format(**globals())
DOC_PACKAGE  = "{BUILD_DIR}/{PACKAGE_NAME}-doc-{VERSION}.tar.gz".format(**globals())
PUBLIC_DIR   = "/Volumes/skynet-wt-10-2/ptc/Windchill_10.2/HTTPServer/htdocs/docs/{PACKAGE_NAME}".format(**globals())

env.nexiles.update(
    public_source=True,
    package_name=PACKAGE_NAME,
    version=VERSION,
    root_dir=ROOT_DIR,
    doc_package=DOC_PACKAGE,
    doc_public_dir=PUBLIC_DIR
)
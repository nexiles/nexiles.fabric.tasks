import sys

from fabric.api import env

from nexiles.fabric.tasks import environment
from nexiles.fabric.tasks import docs

PACKAGE_NAME = "nexiles.fabric.tasks"
VERSION      = "0.1.0"

env.nexiles.update(
    doc_package="{PACKAGE_NAME}-doc-{VERSION}".format(**globals()),
    doc_public_dir="/Volumes/skynet-wt-10-2/ptc/Windchill_10.2/HTTPServer/htdocs/docs/{PACKAGE_NAME}".format(**globals()),
)
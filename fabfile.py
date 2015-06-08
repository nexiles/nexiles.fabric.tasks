from fabric.api import env

from nexiles.fabric.tasks import docs
from nexiles.fabric.tasks import utils
from nexiles.fabric.tasks import release

PACKAGE_NAME = "nexiles.fabric.tasks"
VERSION      = utils.get_version_from_setup_py()

env.nexiles.update(
    public_source=True,
    package_name=PACKAGE_NAME,
    version=VERSION,
    doc_package="{PACKAGE_NAME}-doc-{VERSION}".format(**globals()),
    doc_public_dir="/Volumes/skynet-wt-10-2/ptc/Windchill_10.2/HTTPServer/htdocs/docs/{PACKAGE_NAME}".format(**globals()),
)
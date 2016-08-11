from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")
use_plugin("python.unittest")
use_plugin("python.coverage")

default_task = "publish"

@init
def initialize(project):
  project.build_depends_on('pyyaml')
  project.build_depends_on('dpath')
  project.build_depends_on('pyinstaller')

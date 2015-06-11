.. _env:

=================
Global Fabric Env
=================

Abstract
========

Here we document the environment_ the tasks use.

.. _environment: http://docs.fabfile.org/en/1.10/usage/env.html


Env Vars
========

Build Paths
-----------

**root_dir**
	Repository root directory.

**build_dir**
	:default: `{root_dir}/build`
	Build artefact directory.  All build packages are placed here.  Note,
	this is not the distribution directory.

Distribution and Release
------------------------

**dist_root**
	:default: `~/develop/nexiles/dist`
	The **base directory** where the distribution files are.

Package Settings
----------------

**version**
	Version identifier of the project.

**package_name**
	Package name of the project.  This is used to create dist package
	file names.


..  vim: set ft=rst tw=75 nocin spell nosi ai sw=4 ts=4 expandtab:


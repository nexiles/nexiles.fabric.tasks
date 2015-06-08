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

**root_dir**
	Repository root directory.

**version**
	Version identifier of the project.

**package_name**
	Package name of the project.  This is used to create dist package
	file names.

**build_dir**
	Build artefact directory.  All build packages are placed here.  Note,
	this is not the distribution directory.

**doc_package**
	Documentation package name.


..  vim: set ft=rst tw=75 nocin spell nosi ai sw=4 ts=4 expandtab:


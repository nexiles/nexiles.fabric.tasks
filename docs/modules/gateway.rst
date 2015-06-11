.. _module_gateway:

==================
Module: gateway.py
==================

Abstract
========

**nexiles|gateway** related tasks.

Task: build_eggs
================

Purpose
-------

Build **nexiles|gateway** module eggs.

This task will build all eggs which are configured in `fabric.json`, one
per customer.

Usage
-----

::

	fab gateway.build_eggs

Example
-------

::

	$ fab gateway.build_eggs
	Initializing environment.
	Loading fabric env from fabric.json
	Building nexiles.gateway.example version 1.0.0
	   Generated license module for nexiles
	   Building nexiles.gateway.example for nexiles
	   Removed license module for nexiles
	   Adding package manifest to /Users/seletz/develop/nexiles/nexiles.gateway.example/build/nexiles.gateway.example-1.0.0-py2.7-nexiles.egg for nexiles.
	   Generated license module for acme
	   Building nexiles.gateway.example for acme
	   Removed license module for acme
	   Adding package manifest to /Users/seletz/develop/nexiles/nexiles.gateway.example/build/nexiles.gateway.example-1.0.0-py2.7-acme.egg for acme.
	Built eggs:
	   /Users/seletz/develop/nexiles/nexiles.gateway.example/build/nexiles.gateway.example-1.0.0-py2.7-nexiles.egg
	   /Users/seletz/develop/nexiles/nexiles.gateway.example/build/nexiles.gateway.example-1.0.0-py2.7-acme.egg

	Done.


Configuration
-------------

For this task to work, the gateway module needs to be configured in
`fabric.json`.  For example::

	{
	    "import_name": "nexiles.gateway.example",
	    "package_dir": "src/nexiles.gateway.example",
	    "setup_py":    "src/nexiles.gateway.example/setup.py",
	    "version_file": "src/nexiles.gateway.example/nexiles/gateway/example/version.py",
	    "license_module": "src/nexiles.gateway.example/nexiles/gateway/example/license.py",
	    "urn": "urn:uuid:77cb6351-6ea7-4c16-a397-deadbeef",
	    "customers": ["nexiles", "acme"]
	}


.. note:: Currently, only **one** module per repository is supported.

Task: list_eggs
===============

Purpose
-------

Lists all eggs which would be build.

Usage
-----

::

	fab gateway.list_eggs

Example
-------

::

	$ fab gateway.list_eggs
	Initializing environment.
	Loading fabric env from fabric.json
	/Users/seletz/develop/nexiles/nexiles.gateway.example/build/nexiles.gateway.example-1.0.0-py2.7-nexiles.egg
	/Users/seletz/develop/nexiles/nexiles.gateway.example/build/nexiles.gateway.example-1.0.0-py2.7-acme.egg

	Done.

Task: dist_eggs
===============

Purpose
-------

Copy built gateway modules to dist location.

Usage
-----

::

	fab gateway.dist_eggs

Example
-------

::

	$ fab gateway.dist_eggs
	Loading fabric env from fabric.json
	Initializing environment.
	Distributing None version 1.0.0
	   nexiles.gateway.example-1.0.0-py2.7-nexiles.egg
	   nexiles.gateway.example-1.0.0-py2.7-acme.egg

	Done.


Module Documentation
====================


.. automodule:: nexiles.fabric.tasks.gateway
   :members:


.. vim: set ft=rst tw=75 nocin nosi ai sw=4 ts=4 expandtab:

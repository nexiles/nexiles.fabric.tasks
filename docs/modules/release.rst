.. _module_release:

==================
Module: release.py
==================

Abstract
========

Release specific tasks.

Task: `release.github`
======================

Purpose
-------

Craft a GitHub Release

Usage
-----

::

	$ fab release.github

Notes
-----

This task requires the tool `github-release`, see there_ for installation
instructions.  You also need to add a a personal github access key to your
environment.  See the linked docs.

.. _there: https://github.com/aktau/github-release

Task: `release.pypi`
====================

Purpose
-------

Release source code package of a python package to the Python Package Index.

Usage
-----

::

	$ fab release.pypi

For this to work, you need to have a pypi account set up.  If you don't have
one, then you don't need this taks at all.

Notes
-----

This task will publish **source code**.  This is only allowed for few
packages.  If you do not **know** that you're allowed to do that, then
the answer is **NO**.


Module Documentation
====================


.. automodule:: nexiles.fabric.tasks.release
   :members:


.. vim: set ft=rst tw=75 nocin nosi ai sw=4 ts=4 expandtab:

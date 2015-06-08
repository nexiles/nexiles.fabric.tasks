===========
Development
===========

:Author:    nexiles
:Date:      2015-06-08


Introduction
============

This documentation describes how to bootstrap the development environment.

Bootstrapping
=============

Clone the Project_ to `$HOME/develop/nexiles`::

    cd ~/develop/nexiles
    git clone git@github.com:nexiles/nexiles.fabric.tasks.git
    cd nexiles.fabric.tasks
    mkvirtualenv nexiles.fabric.tasks && setvirtualenvproject
    pip install -r requirements.rst


Documentation
=============

The documentation is built with Sphinx_::

    workon nexiles.fabric.tasks
    cd docs
    make html


.. _Project: https://github.com/nexiles/nexiles.fabric.tasks
.. _Git: git@github.com:nexiles/nexiles.starter2.git
.. _Sphinx: http://sphinx-doc.org

.. vim: set ft=rst ts=4 sw=4 expandtab tw=78 :

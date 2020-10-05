========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/pyaimharder/badge/?style=flat
    :target: https://readthedocs.org/projects/pyaimharder
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/adriandiazgar/pyaimharder.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/adriandiazgar/pyaimharder

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/adriandiazgar/pyaimharder?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/adriandiazgar/pyaimharder

.. |requires| image:: https://requires.io/github/adriandiazgar/pyaimharder/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/adriandiazgar/pyaimharder/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/adriandiazgar/pyaimharder/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/adriandiazgar/pyaimharder

.. |version| image:: https://img.shields.io/pypi/v/pyaimharder.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pyaimharder

.. |wheel| image:: https://img.shields.io/pypi/wheel/pyaimharder.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pyaimharder

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pyaimharder.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pyaimharder

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pyaimharder.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pyaimharder

.. |commits-since| image:: https://img.shields.io/github/commits-since/adriandiazgar/pyaimharder/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/adriandiazgar/pyaimharder/compare/v0.0.1...master



.. end-badges

A Python helper library for https://aimharder.com/ - The ultimate software for your CrossFit®  Box

* Free software: BSD 2-Clause License

Installation
============

::

    pip install pyaimharder

You can also install the in-development version with::

    pip install https://github.com/adriandiazgar/pyaimharder/archive/master.zip


Documentation
=============


https://pyaimharder.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

This is a Websauna application package for {{cookiecutter.project_name}}.

To run this package you need Python 3.4+, PostgresSQL and Redis.

Installation
============

This installation method assumes you the author of the {{cookiecutter.project_name}} application and wish to develop it. Below are instructions to to install the package to a Python virtual environment using pip command in an editable mode.

Example::

    cd {{cookiecutter.pkg_name}}  # This is the folder with setup.py file
    virtualenv venv
    source venv/bin/activate

    # Make sure pip itself is up-to-date
    pip install -U pip

    # Install the package and its dependencies to a currently
    # activated virtualenv from the folder with setup.py file
    pip install -e "."

Running the website
===================

Local development machine
-------------------------

Example (OSX / Homebrew)::

    # Create PostgreSQL database
    psql create {{cookiecutter.db_name}}_dev

    # Write table schemas for models
    ws-sync-db {{cookiecutter.pkg_name}}/conf/development.ini

    # Start web server
    ws-pserve {{cookiecutter.pkg_name}}/conf/development.ini --reload

Running the test suite
======================

Example::

    # Install testing dependencies
    pip install ".[dev,test]"

    # Create database used for unit testing
    psql create {{cookiecutter.db_name}}_test

    # Run test suite using py.test running
    py.test

More information
================

Please see https://websauna.org/
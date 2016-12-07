=============================
websauna-cookiecutter-starter
=============================

A cookiecutter (project template) for creating a Websauna starter project.

Requirements
------------

* See websauna `requirements <https://websauna.org/docs/tutorials/gettingstarted/tutorial_02.html#external-dependencies>`_

Usage
-----

1. Generate a Websauna project.

.. code-block:: bash

    $ ws-create

2. Finish configuring the project by creating a virtual environment and
   installing your new project.
   See detailed instructions on the official Websauna 
   `documentation <https://websauna.org/docs/tutorials/gettingstarted/tutorial_03.html#installing-application-package>`_.

 Contributing
 ------------
 1. Create virtualenv and install tox.

 .. code-block:: bash

    $ virtualenv -p python3 venv
    $ pip install tox

2. Run all the tests:

.. code-block:: bash

    $ tox

3. Add your changes and tests, run tests and create PR.

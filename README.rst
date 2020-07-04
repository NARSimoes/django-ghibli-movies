
=============
Ghibli Movies
=============

Ghibli movies is a simple application which, upon login, serves a page with
a plain list of all movies from the Ghibli API. For each movie the people that
appear in it should be listed.

**Contents:**

.. contents:: :local:

Run using Docker
================

**1. Clone repository**

.. code-block:: bash

    git clone <url>

**2. Start up with docker-compose**

.. code-block:: bash

    docker-compose build --no-cache
    docker-compose up -d

**3. Open application and enjoy (or not :D)!**

    http://127.0.0.1:8990

Run in development mode
=======================

.. code-block:: bash

    docker-compose -f docker-compose-development.yml build --no-cache
    docker-compose up -d

Examples
========

**1. First Page**

.. image:: docs/source/images/first_page.png

**2. Sign Up**

.. image:: docs/source/images/sign_up.png

**3. Sign In**

.. image:: docs/source/images/sign_in.png

**4. Ghibli Movies**

.. image:: docs/source/images/movies.png

Tests
=====

1. Run Tests (not using selenium/geckodriver/firefox) and check coverage

.. code-block:: bash

    docker exec -it <container-id> coverage run manage.py test
    docker exec -it <container-id> coverage html
    open htmlcov/index.html

**Current Coverage:**

.. image:: docs/source/images/coverage.png

2. Run Tests (including tests using selenium/geckodriver/firefox) and check coverage

    Use docker-compose-tests.yml and check docker/view_tests/Dockerfile
    or try to install locally geckodriver, firefox and the requirements.txt

Documentation:
==============

The documentation was created using Sphinx.

Prepared for Google Authentication:
===================================

With the administration account add new site section and a social application (Fill those values with your OAuth details).

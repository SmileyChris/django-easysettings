===================
django-easysettings
===================

.. image:: https://badge.fury.io/py/django-easysettings.svg
    :alt: PyPI version
    :target: https://badge.fury.io/py/django-easysettings

.. image:: https://travis-ci.org/SmileyChris/django-easysettings.svg?branch=master
    :alt: Build status
    :target: http://travis-ci.org/SmileyChris/django-easysettings

.. image:: https://codecov.io/gh/SmileyChris/django-easysettings/branch/master/graph/badge.svg
    :alt: Coverage status
    :target: https://codecov.io/gh/SmileyChris/django-easysettings


Easy app-specific settings for Django apps.

Provides a method for using a declarative class for an app's default settings.
The instance of this class can be used to access all project settings in place
of ``django.conf.settings``.

.. contents::
    :local:
    :backlinks: none


Installation
============

To install, run: ``pip install django-easysettings``


Usage
=====

Create a ``conf.py`` file within your app's directory, adding attributes for
the default values of your app-specific settings. They will be overridden by
any project setting that is provided.

For example:

.. code:: python

    from easysettings import AppSettings


    class Settings(AppSettings):
        MYAPP_FRUIT = 'Apple'


    settings = Settings()


Then in your app, rather than `from django.conf import settings`, use
`from myapp.conf import settings`. For example:

.. code:: python

    from myapp.conf import settings


    def dashboard(request):
        context = {}
        context['fruit'] = settings.MYAPP_FRUIT
        if settings.DEBUG:
            context['debug_mode'] = True
        # ...


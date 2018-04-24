===================
django-easysettings
===================

.. image:: https://circleci.com/gh/SmileyChris/django-easysettings.svg?style=svg
    :alt: Build status
    :target: https://circleci.com/gh/SmileyChris/django-easysettings

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

    from easysettings.app import AppSettings


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

Dictionaries
------------

A common pattern is to use a dictionary as a namespace for all an app's
settings, such as ``settings.MYAPP['settings']``.

Easy-settings handles this fine, overriding any keys provided in the project
while still having access to the default app settings keys.

You can also use a subclass of an ``AppSettings`` class to set up a dictionary.

.. code:: python

    from easysettings.apps import AppSettings


    class MyAppSettings(AppSettings):
        """
        MyApp settings
        """
        #: Preferred fruit
        FRUIT = 'Apple'
        #: Preferred drink
        DRINK = 'Water'


    class Settings(AppSettings):
        MYAPP = MyAppSettings


    settings = Settings()

Legacy Usage
------------

If previously your app used a common prefix (like `MYAPP_`) you
can still support projects that still use these stand-alone legacy settings
while moving to a ``MYAPP`` dictionary for your settings.

.. code:: python

    from easysettings.legacy import LegacyAppSettings


    class Settings(LegacyAppSettings):
        MYAPP = {'FRUIT': 'Apple'}


    settings = Settings()

If a project uses settings like ``MYAPP_FRUIT = 'Banana'`` they will continue
to work. As soon as a project switches to ``MYAPP``, any ``MYAPP_*`` settings
will be ignored.

While the legacy app settings class is used, the dictionary settings can still
be accessed via the prefixed setting (for example, ``settings.MYAPP_FRUIT``).

==================
django-easysettings
==================

Easy app-specific settings for Django.


Installation
============

To install, run: ``pip install django-easysettings``

Or for the `development version`__: ``pip install django-easysettings==dev``

__ https://github.com/SmileyChris/django-easysettings/tarball/master#egg=django-easysettings-dev


Usage
=====

Create a `conf.py` file within your app's directory, adding attributes for the
default values of your app-specific settings. They will be overridden by
any project setting that is provided.

For example::

    from easysettings import AppSettings


    class Settings(AppSettings):
        MYAPP_WIDGETS = ('foo', 'bar')

Then in your app, rather than `from django.conf import settings`, use
`from myapp.conf import settings`. For example::

    from myapp.conf import settings


    def dashboard(request):
        data = {}
        for widget in settings.MYAPP_WIDGETS:
            data[widget] = render_widget(widget)
        if settings.DEBUG:
            data['debug_mode'] = True
        # ...

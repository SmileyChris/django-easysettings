===================
django-easysettings
===================

Easy app-specific settings for Django.


Installation
============

To install, run: ``pip install django-easysettings``


Usage
=====

Create a ``conf.py`` file within your app's directory, adding attributes for
the default values of your app-specific settings. They will be overridden by
any project setting that is provided.

For example::

    from easysettings import AppSettings


    class Settings(AppSettings):
        MYAPP_WIDGETS = ('foo', 'bar')


    settings = Settings()


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


Isolating Settings when Testing
-------------------------------

You can force your app's tests to use the default project settings rather than
any value in the project's ``settings`` configuration module.

Just set ``settings.isolated = True``.

For example, you could use a base test class to do this::

    class BaseTest(TestCase):

        def setUp(self):
            """
            Isolate all application specific settings.
            """
            output = super(BaseTest, self).setUp()
            settings.isolated = True
            return output

        def tearDown(self):
            """
            Restore settings to their original state.
            """
            settings.isolated = False
            settings.revert()
            return super(BaseTest, self).tearDown()

As also shown in the example above, you can revert any changes made by calling
``settings.revert()``.

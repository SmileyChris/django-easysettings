"""
Easy app-specific settings for Django.

The standard use is to import and extend :class:`AppSettings` in a `conf`
module (for example, `myapp/conf.py`), adding attributes for the default
values of your app-specific settings.

Project settings override the default settings specified in this subclass.

The app's `conf` module will look something like this::

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
"""
from django.conf import BaseSettings
from django.conf import settings as django_settings


class AppSettings(BaseSettings):
    """
    A holder for app-specific Django settings.

    When :attr:`isolated` is ``False`` (the default) the holder returns
    attributes from the project's setting module, falling back to the default
    attributes provided in this module if the attribute wasn't found.
    """

    def __init__(self, isolated=False, *args, **kwargs):
        self.isolated = isolated
        self._changed = {}
        self._added = []
        super(AppSettings, self).__init__(*args, **kwargs)

    def get_isolated(self):
        return self._isolated

    def set_isolated(self, value):
        if value:
            self._isolated_overrides = BaseSettings()
        self._isolated = value

    isolated = property(get_isolated, set_isolated)

    def revert(self):
        """
        Revert any changes made to settings.
        """
        for attr, value in self._changed.items():
            setattr(django_settings, attr, value)
        for attr in self._added:
            delattr(django_settings, attr)
        self._changed = {}
        self._added = []
        if self.isolated:
            self._isolated_overrides = BaseSettings()

    def __getattribute__(self, attr):
        if attr == attr.upper():
            if self.isolated:
                try:
                    return getattr(self._isolated_overrides, attr)
                except AttributeError:
                    pass
            else:
                try:
                    return getattr(django_settings, attr)
                except AttributeError:
                    pass
        try:
            return super(AppSettings, self).__getattribute__(attr)
        except AttributeError:
            if not self.isolated:
                raise
            return getattr(django_settings, attr)

    def __setattr__(self, attr, value):
        if attr == attr.upper():
            if self.isolated:
                try:
                    super(AppSettings, self).__getattribute__(attr)
                except AttributeError:
                    pass
                else:
                    # Set the app setting to an isolated overrides that gets
                    # checked before the project's settings.
                    return setattr(self._isolated_overrides, attr, value)
            # Keep track of any project settings changes so they can be
            # reverted.
            if attr not in self._added:
                try:
                    self._changed.setdefault(attr,
                        getattr(django_settings, attr))
                except AttributeError:
                    self._added.append(attr)
            return setattr(django_settings, attr, value)
        return super(AppSettings, self).__setattr__(attr, value)

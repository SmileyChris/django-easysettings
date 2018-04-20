"""
Easy app-specific settings for Django.

The standard use is to import and extend :class:`AppSettings` in a `conf`
module (for example, `myapp/conf.py`), adding attributes for the default
values of your app-specific settings.
"""
import django.conf.settings


class AppSettings(object):
    """
    A container for app-specific Django settings that can be overridden by
    project settings.
    """

    def __getattribute__(self, attr):
        default_value = super(AppSettings, self).__getattribute__(attr)
        if attr != attr.upper():
            return default_value
        if (isinstance(default_value, AppSettings)
                or issubclass(default_value, AppSettings)):
            default_value = default_value.default_dict()
        try:
            settings_value = getattr(django.conf.settings, attr)
        except AttributeError:
            return default_value
        if isinstance(default_value, dict):
            value = default_value.copy()
            value.update(settings_value)
            return value
        return settings_value

    def get_project_value(self, attr):
        return getattr(django.conf.settings, attr)

    @classmethod
    def default_dict(cls):
        return dict(
            (attr, value) for attr, value in dir(cls).items()
            if attr == attr.upper())

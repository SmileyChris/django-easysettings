"""
Easy app-specific settings for Django.

The standard use is to import and extend :class:`AppSettings` in a `conf`
module (for example, `myapp/conf.py`), adding attributes for the default
values of your app-specific settings.
"""
from django.conf import settings as django_settings


class AppSettings(object):
    """
    A container for app-specific Django settings that can be overridden by
    project settings.
    """

    def __getattribute__(self, attr):
        if attr != attr.upper():
            return super(AppSettings, self).__getattribute__(attr)
        try:
            project_value = self.get_project_value(attr)
        except AttributeError:
            return self.get_app_setting(attr)
        if isinstance(project_value, dict) and attr in dir(self):
            app_value = self.get_app_setting(attr)
            if isinstance(app_value, dict):
                value = app_value.copy()
                value.update(project_value)
                return value
        return project_value

    def get_app_setting(self, attr):
        value = super(AppSettings, self).__getattribute__(attr)
        if (isinstance(value, AppSettings)
                or (isinstance(value, type)
                    and issubclass(value, AppSettings))):
            return value.default_dict()
        return value

    def get_project_value(self, attr):
        return getattr(django_settings, attr)

    @classmethod
    def default_dict(cls):
        return dict(
            (attr, getattr(cls, attr)) for attr in dir(cls)
            if attr == attr.upper())

from django.conf import settings as django_settings
from easysettings.app import AppSettings


class LegacyAppSettings(AppSettings):
    """
    Deal with legacy prefixed settings that have been moved to a
    dictionary.

    This allows for access to ``settings.SOME_SETTING`` where a ``SOME``
    dictionary with a ``SETTING`` key is defined on the class.
    """

    def __getattribute__(self, attr):
        """
        Before just getting the attribute, first try to find it as an attribute
        inside a new dictionary setting.
        """
        try:
            if attr != attr.upper():
                raise AttributeError("Not a setting")
            return self.get_legacy_attr(attr)
        except AttributeError:
            return super(LegacyAppSettings, self).__getattribute__(attr)

    def get_project_value(self, attr):
        """
        If no project value is found for a defined dictionary app setting,
        fall back to building a dictionary from legacy prefixed settings.
        """
        try:
            return super(LegacyAppSettings, self).get_project_value(attr)
        except AttributeError:
            default_dict = self.get_app_setting(attr)
            if isinstance(default_dict, dict):
                settings_dict = {}
                for key in default_dict:
                    legacy_attr = '{}_{}'.format(attr, key)
                    try:
                        settings_dict[key] = getattr(
                            django_settings, legacy_attr)
                    except AttributeError:
                        pass
                if settings_dict:
                    return settings_dict
            raise

    def get_legacy_attr(self, attr):
        """
        Return the value of a legacy attribute (or if it's not, raise an
        ``AttributeError``).
        """
        if attr in dir(self):
            raise AttributeError(
                "Defined app setting, so not a legacy setting")
        for k in dir(self):
            if not attr.startswith(k + '_'):
                continue
            v = self.get_app_setting(k)
            if not isinstance(v, dict):
                continue
            inner_key = attr[len(k)+1:]
            try:
                return getattr(self, k)[inner_key]
            except KeyError:
                continue
        raise AttributeError('No legacy setting found')

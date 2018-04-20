import django.conf.settings
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
            default_dict = self.default_dict().get(attr)
            if isinstance(default_dict, dict):
                settings_dict = {}
                for key in default_dict[attr]:
                    legacy_attr = '{}_{}'.format(attr, key)
                    try:
                        settings_dict[key] = getattr(
                            django.conf.settings, legacy_attr)
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
        if attr != attr.upper():
            raise AttributeError("Not a setting")
        if hasattr(type(self), attr):
            raise AttributeError(
                "Defined app setting, so not a legacy setting")
        parts = attr.split('_', 1)
        if len(parts) != 2 or not all(parts):
            raise AttributeError('Not in the format of a legacy setting')
        new_prefix, new_key = parts
        new_dict = getattr(type(self), new_prefix)
        if not isinstance(new_dict, dict):
            raise AttributeError('Prefix is not a dictionary app setting')
        try:
            return new_dict[new_key]
        except KeyError:
            raise AttributeError('No matching key in dictionary setting')

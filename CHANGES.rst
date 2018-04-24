==========
Change Log
==========

2.0 (24 April 2018)
===================

- Full rework of project! Import is now
  ``from easysettings.app import AppSettings`` (but left importable from
  ``easysettings`` for better backwards compatibility).

- Removed isolated settings functionality, unnecessary with a separate settings
  module for tests and/or use of the ``TestCase.settings()`` context manager.

- Added ``easysettings.legacy.LegacyAppSettings`` for providing backwards
  compatibility for prefixed project settings when moving settings to a
  dictionary rather than individual settings with the same prefix.

1.1 (4 April 2017)
==================

- Django 1.11 compatibility.

1.0.1 (24 May 2012)
===================

- Included extra source files.

1.0 (16 April 2012)
===================

- Initial release.

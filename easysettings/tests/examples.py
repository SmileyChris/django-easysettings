from easysettings.app import AppSettings
from easysettings.legacy import LegacyAppSettings


class Basic(AppSettings):
    FRUIT = 'Apple'


class Dict(AppSettings):
    SEARCH = {
        'COUNT': 10,
        'MAX': 100,
    }


class Inner(AppSettings):
    FIBULA = True


class Nested(AppSettings):
    BONES = Inner


class Underscore(LegacyAppSettings):
    UNDER_SCORE = '_'


class Under(LegacyAppSettings):
    UNDER = {
        'SCORE': '_',
        'WATER': '~',
    }


class UnderUnder(LegacyAppSettings):
    UNDER = 'not dict'
    UNDER_UNDER = {'WEAR': 'bikini'}

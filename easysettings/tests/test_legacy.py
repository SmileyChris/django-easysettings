import pytest

import easysettings.app
import easysettings.legacy
from . import examples


class ProjectSettings(object):
    pass


@pytest.fixture
def project_settings(mocker):
    settings = ProjectSettings()

    def return_settings():
        return settings

    mocker.patch.object(
        easysettings.app, 'django_settings', new_callable=return_settings)
    mocker.patch.object(
        easysettings.legacy, 'django_settings', new_callable=return_settings)
    return settings


def test_standard(project_settings):
    settings = examples.Under()
    assert settings.UNDER == {'SCORE': '_', 'WATER': '~'}


def test_standard_override(project_settings):
    settings = examples.Under()
    project_settings.UNDER = {'WATER': '~~~'}
    assert settings.UNDER == {'SCORE': '_', 'WATER': '~~~'}


def test_project(project_settings):
    settings = examples.Under()
    project_settings.DATABASES = {'default': {'NAME': 'app.sqlite3'}}
    assert settings.DATABASES['default'] == {'NAME': 'app.sqlite3'}


def test_legacy(project_settings):
    settings = examples.Under()
    assert settings.UNDER_SCORE == '_'


def test_legacy_override(project_settings):
    settings = examples.Under()
    project_settings.UNDER = {'WATER': '~~~'}
    assert settings.UNDER_SCORE == '_'
    assert settings.UNDER_WATER == '~~~'


def test_legacy_override_legacy(project_settings):
    settings = examples.Under()
    project_settings.UNDER_WATER = '~~~'
    assert settings.UNDER_SCORE == '_'
    assert settings.UNDER_WATER == '~~~'


def test_legacy_override_both(project_settings):
    settings = examples.Under()
    project_settings.UNDER = {'SCORE': '_ _'}
    project_settings.UNDER_WATER = '~~~'
    assert settings.UNDER_SCORE == '_ _'
    assert settings.UNDER_WATER == '~'


def test_not_dict(project_settings):
    settings = examples.Underscore()
    assert settings.UNDER_SCORE == '_'
    with pytest.raises(AttributeError):
        settings.UNDER


def test_not_dict_override(project_settings):
    settings = examples.Underscore()
    project_settings.UNDER = {'SCORE': '___'}
    assert settings.UNDER_SCORE == '_'


def test_under_under(project_settings):
    settings = examples.UnderUnder()
    assert settings.UNDER == 'not dict'
    assert settings.UNDER_UNDER_WEAR == 'bikini'
    with pytest.raises(AttributeError):
        settings.UNDER_UNDER_WATER

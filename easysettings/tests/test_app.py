import pytest

import easysettings.app
from . import examples


class ProjectSettings(object):
    pass


@pytest.fixture
def project_settings(mocker):
    return mocker.patch.object(
        easysettings.app, 'django_settings', new_callable=ProjectSettings)


def test_app(project_settings):
    settings = examples.Basic()
    assert settings.FRUIT == 'Apple'


def test_app_override(project_settings):
    project_settings.FRUIT = 'Banana'
    settings = examples.Basic()
    assert settings.FRUIT == 'Banana'


def test_project(project_settings):
    project_settings.DEBUG = True
    settings = examples.Basic()
    assert settings.DEBUG is True


def test_missing(project_settings):
    settings = examples.Basic()
    with pytest.raises(AttributeError):
        settings.NOT_A_SETTING


def test_app_dict(project_settings):
    settings = examples.Dict()
    assert settings.SEARCH['COUNT'] == 10


def test_app_override_dict(project_settings):
    settings = examples.Dict()
    ProjectSettings.SEARCH = {'COUNT': 15}
    assert settings.SEARCH['COUNT'] == 15
    print(settings.SEARCH)
    assert settings.SEARCH['MAX'] == 100


def test_project_dict(project_settings):
    settings = examples.Basic()
    project_settings.DATABASES = {'default': {'NAME': 'app.sqlite3'}}
    assert settings.DATABASES['default'] == {'NAME': 'app.sqlite3'}


def test_nested(project_settings):
    settings = examples.Nested()
    assert settings.BONES == {'FIBULA': True}

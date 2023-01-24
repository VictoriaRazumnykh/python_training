import pytest
from fixture.application import Application
import json
import os.path

fixture = None
target=None


# функция, которая инициализирует фикстуру
@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        #автоматическое определение пути к файлу относительно директории проекта
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseUrl"], user=target["username"], password=target["password"])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")

    #parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    #parser.addoption("--user", action="store", default="admin")
    #parser.addoption("--password", action="store", default="secret")

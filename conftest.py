import pytest
from fixture.application import Application

# функция, которая инициализирует фикстуру
@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



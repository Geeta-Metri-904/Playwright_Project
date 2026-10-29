import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    """Fixture to initialize and navigate to the login page before tests."""
    login_pg = LoginPage(page)
    login_pg.navigate("https://www.saucedemo.com/")
    return login_pg
import pytest


def test_successful_login(login_page, page):
    """Test login with valid credentials."""
    login_page.login("standard_user", "secret_sauce")

    # Assert successful redirect to inventory page
    assert "inventory.html" in login_page.get_current_url()


def test_locked_out_user_login(login_page):
    """Test login with a locked-out user to verify error handling."""
    login_page.login("locked_out_user", "secret_sauce")

    error = login_page.get_error_text()
    assert "Epic sadface: Sorry, this user has been locked out." in error
import re
from playwright.sync_api import Page, expect

LOGIN_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


def open_login_page(page):
    page.goto(LOGIN_URL)


def login(page, username="Admin", password="admin123"):
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()


# TC01 - Verify login page is displayed
def test_TC01_verify_login_page(page: Page):
    open_login_page(page)

    expect(page.get_by_placeholder("Username")).to_be_visible()
    expect(page.get_by_placeholder("Password")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()


# TC02 - Verify mandatory field validation
def test_TC02_empty_login_validation(page: Page):
    open_login_page(page)

    page.get_by_role("button", name="Login").click()

    errors = page.locator(".oxd-input-field-error-message")
    expect(errors).to_have_count(2)


# TC03 - Verify login with invalid credentials
def test_TC03_invalid_login(page: Page):
    open_login_page(page)

    login(page, "wronguser", "wrongpass")

    expect(page.locator(".oxd-alert-content-text")).to_contain_text(
        "Invalid credentials"
    )


# TC04 - Verify login with valid credentials
def test_TC04_valid_login(page: Page):
    open_login_page(page)

    login(page)

    expect(page).to_have_url(re.compile(r".*/dashboard/index"))
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()


# TC05 - Verify logout functionality
def test_TC05_logout(page: Page):
    open_login_page(page)

    login(page)

    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()

    page.locator(".oxd-userdropdown-tab").click()
    page.get_by_text("Logout", exact=True).click()

    expect(page.get_by_placeholder("Username")).to_be_visible()
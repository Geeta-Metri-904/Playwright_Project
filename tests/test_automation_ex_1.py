from playwright.sync_api import Page
import time

def test_automation_login(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("Password123")
    page.get_by_role("button", name = "Submit").click()
    page.locator("#menu-item-20").click()
    page.get_by_role("link", name = "Test Table").click()
    page.get_by_role("radio", name = "Python").click()
    page.get_by_role("checkbox", name = "Beginner").uncheck()
    page.get_by_role("checkbox", name="Advanced").uncheck()
    time.sleep(8)


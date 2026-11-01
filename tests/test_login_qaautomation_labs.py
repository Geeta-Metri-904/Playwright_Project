from playwright.sync_api import Page
import time

def test_automation_login(page: Page):
    page.goto("https://practice.expandtesting.com/login")
    page.get_by_label("Username").fill("practice")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name = "Login").click()
    time.sleep(3)
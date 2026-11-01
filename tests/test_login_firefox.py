from playwright.sync_api import Playwright, expect
import time

def test_login_firefox(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.expandtesting.com/login")
    expect(page).to_have_url("https://practice.expandtesting.com/login")
    page.get_by_label("Username").fill("practice")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Logout").click()
    #page.get_by_text("Logout").click()
    time.sleep(4)

from playwright.sync_api import Page, expect
import time

def test_logo(page:Page):
    page.goto("https://practice.expandtesting.com/")
    time.sleep(5)
    page.wait_for_timeout(10000)
    expect(page.get_by_alt_text("Best Website for Practice Automation Testing: Free UI and REST API Examples and Apps. Using Cypress, Playwright, Selenium, WebdriverIO and Postman.")).to_be_visible()
    page.close()
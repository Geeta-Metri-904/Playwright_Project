from playwright.sync_api import Page

#chromium headless mode, 1 single context
def test_playwright_shortcut(page:Page): # page is a fixture, Page is a class
    page.goto("https://google.com")

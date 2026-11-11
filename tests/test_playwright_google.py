from playwright.sync_api import sync_playwright

def test_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com")

        page.locator("textarea[name='q']").fill("Python Playwright")
        page.keyboard.press("Enter")

        page.wait_for_load_state("domcontentloaded")

        print(page.title())

        browser.close()
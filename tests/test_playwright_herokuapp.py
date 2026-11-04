from playwright.sync_api import sync_playwright

def test_herokuapp_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")

        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")

        page.get_by_role("button", name="Login").click()

        print(page.locator("#flash").inner_text())

        browser.close()
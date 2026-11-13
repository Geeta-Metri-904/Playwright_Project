import re
from playwright.sync_api import Page, expect

def test_homepage_navigation(page: Page):
    # Navigate to the website
    page.goto("https://playwright.dev/")

    # Assert the page title contains "Playwright"
    expect(page).to_have_title(re.compile("Playwright"))

    # Click the "Get started" link by its accessible role
    page.get_by_role("link", name="Get started").click()

    # Assert the "Installation" heading is visible on the new page
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
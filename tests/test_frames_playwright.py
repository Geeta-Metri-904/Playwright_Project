from playwright.sync_api import Page, expect
import time

# Frame Handling
def test_frame_handling(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    pageframe = page.frame_locator("#courses-iframe")
    pageframe.get_by_role("link", name = "All Access plan").click()
    expect(pageframe.locator("body")).to_contain_text("Happy Subscibers")


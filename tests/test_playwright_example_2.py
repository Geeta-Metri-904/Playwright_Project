from playwright.sync_api import Page, expect

def test_browser(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_placeholder("Enter Name").fill("Geeta")
    page.get_by_placeholder("Enter EMail").fill("geetametri904@gmail.com")
    page.get_by_role("radio", name = "Female").check()
    page.get_by_role("checkbox", name = "Saturday").check()


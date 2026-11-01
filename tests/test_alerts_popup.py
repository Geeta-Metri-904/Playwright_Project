from playwright.sync_api import Page
import time

#Alert Boxes /Popups
def test_popups_alert(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name = "Confirm").click()
    time.sleep(4)
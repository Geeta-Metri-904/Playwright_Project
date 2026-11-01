from playwright.sync_api import Page, expect
import time

def test_ui_validation_dynamic_script(page:Page):
    # iphone X and Nokia Edge --> verify 2 items are showing in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("stud")
    page.locator("#terms").check()  # css locator by id #terms
    page.get_by_role("button", name="Sign In").click()
    iphonecard = page.locator("app-card").filter(has_text="iphone X")
    iphonecard.get_by_role("button").click()
    nokiacard = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiacard.get_by_role("button").click()
    samsungcard = page.locator("app-card").filter(has_text="Samsung Note 8")
    samsungcard.get_by_role("button").click()
    blackberrycard = page.locator("app-card").filter(has_text="Blackberry")
    blackberrycard.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(4)
    time.sleep(3)




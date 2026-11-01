from playwright.sync_api import Page, expect

def test_invalid_login_creds(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademywrong")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("stud")
    # page.get_by_role("checkbox", name = "terms").check() - checkbox alternative is using css locator
    page.locator("#terms").check() # css locator by id #terms
    page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name = "Sign In").click() # value = "Sign In"
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
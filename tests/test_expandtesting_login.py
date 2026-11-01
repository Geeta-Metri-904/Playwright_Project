'''
Test Case 1: Successful Login
Launch the browser.
Navigate to the login page URL.
Verify that the login page is displayed successfully.
Enter Username: practice.
Enter Password: SuperSecretPassword!.
Click the Login button.
Verify that the user is redirected to the /secure page.
Confirm the success message "You logged into a secure area!" is visible.
Verify that a Logout button is displayed.
'''

from playwright.sync_api import Page, expect

def test_successful_login(page:Page):
    page.goto("https://practice.expandtesting.com/login")
    expect(page).to_have_url("https://practice.expandtesting.com/login")
    expect(page.get_by_text("Test Login page for Automation Testing Practice")).to_be_visible()
    page.get_by_label("Username").fill("practice")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button",name = "Login").click()
    expect(page).to_have_url("https://practice.expandtesting.com/secure")
    expect(page.get_by_text("You logged into a secure area!")).to_be_visible()
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
    page.get_by_role("link", name = "Logout").click()
    expect(page.get_by_text("You logged out of the secure area!")).to_be_visible()



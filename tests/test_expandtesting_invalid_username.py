'''
Test Case 2: Invalid Username
Launch the browser.
Navigate to the login page URL.
Verify that the login page is displayed successfully.
Enter an incorrect Username (e.g., wrongUser).
Enter Password: SuperSecretPassword!.
Click the Login button.
Verify that an error message "Invalid username." is displayed.
Ensure the user remains on the login page.
'''

from playwright.sync_api import Page, expect

def test_unsuccessful_login(page:Page):
    page.goto("https://practice.expandtesting.com/login")
    expect(page).to_have_url("https://practice.expandtesting.com/login")
    expect(page.get_by_text("Test Login page for Automation Testing Practice")).to_be_visible()
    page.get_by_label("Username").fill("wronguser")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button",name = "Login").click()
    expect(page.get_by_text("Your password is invalid!")).to_be_visible()
    expect(page).to_have_url("https://practice.expandtesting.com/login")




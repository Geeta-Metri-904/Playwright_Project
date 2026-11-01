from playwright.sync_api import Page
import time

# https://rahulshettyacademy.com/loginpagePractise/

# Get By Role criteria to work :

# 1. get_by_label works only for this <label>Password <input type="password"/></label>

# or

# 2. <label for="username" class="text-white">Username:</label>
#    <input type="text" name="username" id="username" class="form-control">
#    id has to be associated with for username in label than only get by role works i.e id == for

def test_login_page(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("stud")
    # page.get_by_role("checkbox", name = "terms").check() - checkbox alternative is using css locator
    page.locator("#terms").check() # css locator by id #terms
    page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name = "Sign In").click() # value = "Sign In"
    time.sleep(5)

# css selector
# <input id="terms" name="terms" type="checkbox" data-gtm-form-interact-field-id="0">
# css for above id is --> #terms

# <label for="terms" class="text-info">
# css for above class is --> .text-info

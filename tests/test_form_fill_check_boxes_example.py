from playwright.sync_api import Page, expect

def test_add_item_to_cart(page: Page):
    # Navigate to the sample e-commerce store
    page.goto("https://saucedemo.com")

    # Log in using the site's standard test user
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # Verify products page loaded
    expect(page.get_by_text("Products")).to_be_visible()

    # Add "Sauce Labs Backpack" to the cart
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    # Verify the shopping cart icon displays "1"
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

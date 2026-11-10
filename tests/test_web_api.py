from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils

def test_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # create order --> order Id
    create_order_1 = APIUtils()
    order_id = create_order_1.create_order(playwright)
    print(order_id)

    #Login
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("geetametri904@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Geeta123$")
    page.get_by_role("button", name = "Login").click()
    page.get_by_role("button", name = "ORDERS").click()

    # orders History page --> order is present
    # for index in range(page.locator("tr").count()):
    #     if page.locator("tr").nth(index).filter(has_text="Order Id").count()>0:
    #         column_value = index
    #         print(f"Index of Price column Value is {column_value}")
    #         break
    #
    # row_value = page.locator("th").filter(has_text=order_id)
    # price = row_value.locator("th").nth(column_value).text_content()
    # print(f"Price of the Rice is {price}")
    # expect(rowvalue.locator("th").nth(column_value)).to_have_text(order_id)

    id = page.locator("th").filter(has_text=order_id)
    print(f"id is {id}")
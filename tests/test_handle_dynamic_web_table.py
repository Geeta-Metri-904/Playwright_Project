# Check the price os Rice is equal to 37
# Identify the Price column
# Identify the Rice Row
# Extract the price of the Rice
"""
Understand the complete execution flow
1. Open the offers webpage
2. Find all table headers (th)
3. Identify the index of Price column
4. Find the row containing Rice
5. Extract the price using the column index
6. Verify that the price is 37
"""

from playwright.sync_api import Page, expect

def test_dynamic_web_table(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text = "Price").count()>0:
            columnvalue = index
            print(f"Index of Price column Value is {columnvalue}")
            break

    rowvalue = page.locator("tr").filter(has_text = "Rice")
    price = rowvalue.locator("td").nth(columnvalue).text_content()
    print(f"Price of the Rice is {price}")
    expect(rowvalue.locator("td").nth(columnvalue)).to_have_text("37")

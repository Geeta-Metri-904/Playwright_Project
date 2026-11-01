from playwright.sync_api import Page, expect

def test_child_page_evaluation(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newpage_info:
        page.locator(".blinkingText").nth(0).click() #new page
        count = page.locator(".blinkingText").count()
        #print("blinking text",count)
        childpage = newpage_info.value
        text = childpage.locator(".red").text_content()
        print(text) # Please email us at mentor@rahulshettyacademy.com with below template to receive response
        word = text.split("at")
        print("word", word)# 0 -> Please email us, 1 -> mentor@rahulshettyacademy.com with below template to receive response
        email = word[1].strip().split(" ")[0] # mentor@rahulshettyacademy.com
        assert email == "mentor@rahulshettyacademy.com"
        # ss = ""
        # for i in text.split():
        #     if i == "mentor@rahulshettyacademy.com":
        #         ss = i
        # print(ss)
        # expect(childpage.get_by_text(ss)).to_be_visible()


def test_assert():
    text = "Please email us at mentor@rahulshettyacademy.com with below template to receive response"
    word = text.split("at")
    print("word is", word) #  ['Please email us ', ' mentor@rahulshettyacademy.com with below templ', 'e to receive response']
    email = word[1]
    print("email is", email) #  mentor@rahulshettyacademy.com with below temp
    text = email.split(" ")[1]
    print("text is",text)
    assert text == "mentor@rahulshettyacademy.com"
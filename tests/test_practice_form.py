
import re

from playwright.sync_api import Page, expect


def test_001_submit_practice_form(page: Page) -> None:
    # Open Practice Form
    page.goto("https://demoqa.com/automation-practice-form")

    # Enter First Name and Last Name
    page.locator("#firstName").fill("John")
    page.locator("#lastName").fill("Smith")

    # Enter Email
    page.locator("#userEmail").fill("john.smith@test.com")

    # Select Gender
    page.get_by_text("Male", exact=True).click()

    # Enter Mobile Number
    page.locator("#userNumber").fill("9876543210")

    # Select Date of Birth
    page.locator("#dateOfBirthInput").click()
    page.locator(".react-datepicker__month-select").select_option("5")
    page.locator(".react-datepicker__year-select").select_option("2000")
    page.locator(
        ".react-datepicker__day--015:not(.react-datepicker__day--outside-month)"
    ).click()

    # Enter Subject
    page.locator("#subjectsInput").fill("Maths")
    page.get_by_text("Maths", exact=True).click()

    # Select Sports checkbox
    page.get_by_text("Sports", exact=True).click()

    # Submit Form
    page.locator("#submit").click()

    # Verify confirmation popup
    expect(page.locator(".modal-content")).to_be_visible()

    # Verify submitted name
    expect(page.locator(".modal-content")).to_contain_text("John Smith")

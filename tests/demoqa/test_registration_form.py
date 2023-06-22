import allure
from selene import have, by


@allure.title("Successful fill form")
def test_successful(setup_browser):
    browser = setup_browser
    first_name = "Michael"
    last_name = "Kors"

    with allure.step("Open registrations form"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Fill form"):
        allure.dynamic.tag("Fill the full name")
        browser.element("#firstName").set_value(first_name)
        browser.element("#lastName").set_value(last_name)
        allure.dynamic.tag("Fill the email")
        browser.element("#userEmail").set_value("Michael@Kors.com")
        browser.element("#genterWrapper").element(by.text("Other")).click()
        allure.dynamic.tag("Fill the phone number")
        browser.element("#userNumber").set_value("1231231230")
        allure.dynamic.tag("Fill the subjects and hobbies")
        browser.element("#subjectsInput").send_keys("Maths")
        browser.element("#subjectsInput").press_enter()
        browser.element("#hobbiesWrapper").element(by.text("Sports")).click()
        allure.dynamic.tag("Fill the address")
        browser.element("#currentAddress").set_value("Some street 1")
        allure.dynamic.tag("Choose the state and city")
        browser.element("#state").click()
        browser.element("#stateCity-wrapper").element(by.text("NCR")).click()
        browser.element("#city").click()
        browser.element("#stateCity-wrapper").element(by.text("Delhi")).click()
        allure.dynamic.tag("Submit the form")
        browser.element("#submit").click()

    with allure.step("Check form results"):
        browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))

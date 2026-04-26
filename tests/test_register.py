from pages.register_page import RegisterPage

def test_register_page_loads(page):
    register = RegisterPage(page)
    register.navigate()
    assert page.url == "https://automationexercise.com/login"

def test_register_with_existing_email(page):
    register = RegisterPage(page)
    register.navigate()
    register.enter_name("Martin")
    register.enter_email("your_realemail_here")
    register.click_signup_button()
    error = register.get_error_message()
    assert "Email Address already exist!" in error

def test_register_with_new_email(page):
    register = RegisterPage(page)
    register.navigate()
    register.enter_name("Test User")
    register.enter_email("testuser12345unique@test.com")
    register.click_signup_button()
    assert page.url == "https://automationexercise.com/signup"
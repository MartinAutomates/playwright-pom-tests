from pages.login_page import LoginPage

def test_login_with_wrong_credentials(page):
    login = LoginPage(page)
    login.navigate()
    login.enter_email("wrong@email.com")
    login.enter_password("wrongpassword")
    login.click_login_button()
    error = login.get_error_message()
    assert "Your email or password is incorrect!" in error

def test_login_page_loads(page):
    login = LoginPage(page)
    login.navigate()
    assert page.url == "https://automationexercise.com/login"

def test_login_with_correct_credentials(page):
    login = LoginPage(page)
    login.navigate()
    login.enter_email("your_email_here")
    login.enter_password("your_password_here")
    login.click_login_button()
    assert page.url == "https://automationexercise.com/"
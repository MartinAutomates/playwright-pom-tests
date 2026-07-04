from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_login_with_wrong_credentials(page):
    login = LoginPage(page)
    login.navigate(login.URL)
    login.enter_email("wrong@email.com")
    login.enter_password("wrongpassword")
    login.click_login_button()
    error = login.get_error_message()
    assert "Your email or password is incorrect!" in error

def test_login_page_loads(page):
    login = LoginPage(page)
    login.navigate(login.URL)
    expect(page).to_have_url("https://automationexercise.com/login")

def test_login_with_correct_credentials(page):
    login = LoginPage(page)
    login.navigate(login.URL)
    login.enter_email()
    login.enter_password()
    login.click_login_button()
    expect(page).to_have_url("https://automationexercise.com/")
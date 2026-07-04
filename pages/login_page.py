import os
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://automationexercise.com/login"

    def enter_email(self, email=None):
        email = email or os.getenv("TEST_EMAIL")
        self.page.fill("input[data-qa='login-email']", email)

    def enter_password(self, password=None):
        password = password or os.getenv("TEST_PASSWORD")
        self.page.fill("input[data-qa='login-password']", password)

    def click_login_button(self):
        self.page.click("button[data-qa='login-button']")

    def get_error_message(self):
        return self.page.locator("form[action='/login'] p").inner_text()
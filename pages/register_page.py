import os
from pages.base_page import BasePage

class RegisterPage(BasePage):
    URL = "https://automationexercise.com/login"

    def enter_name(self, name):
        self.page.fill("input[data-qa='signup-name']", name)

    def enter_email(self, email):
        self.page.fill("input[data-qa='signup-email']", email)

    def click_signup_button(self):
        self.page.click("button[data-qa='signup-button']")

    def get_error_message(self):
        return self.page.locator("form[action='/signup'] p").inner_text()
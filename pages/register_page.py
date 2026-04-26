from conftest import handle_consent

class RegisterPage:
    URL = "https://automationexercise.com/login"

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)
        handle_consent(self.page)
        self.page.wait_for_timeout(1000)

    def enter_name(self, name):
        self.page.fill("input[data-qa='signup-name']", name)

    def enter_email(self, email):
        self.page.fill("input[data-qa='signup-email']", email)

    def click_signup_button(self):
        self.page.click("button[data-qa='signup-button']")

    def get_error_message(self):
        return self.page.inner_text("p[style='color: red;']")
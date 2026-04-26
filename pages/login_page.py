from conftest import handle_consent

class LoginPage:
    URL = "https://automationexercise.com/login"

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)
        handle_consent(self.page)
        self.page.wait_for_timeout(1000)

    def enter_email(self, email):
        self.page.fill("input[data-qa='login-email']", email)

    def enter_password(self, password):
        self.page.fill("input[data-qa='login-password']", password)

    def click_login_button(self):
        self.page.click("button[data-qa='login-button']")

    def get_error_message(self):
        return self.page.inner_text("p[style='color: red;']")
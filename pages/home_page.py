from conftest import handle_consent

class HomePage:
    URL = "https://automationexercise.com"

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)
        handle_consent(self.page)

    def get_title(self):
        return self.page.title()

    def click_login(self):
        self.page.click("a[href='/login']")
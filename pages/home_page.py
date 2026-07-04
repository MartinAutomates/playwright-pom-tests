from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://automationexercise.com"

    def get_title(self):
        return self.page.title()

    def click_login(self):
        self.page.click("a[href='/login']")
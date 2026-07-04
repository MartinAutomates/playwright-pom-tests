class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)
        self.handle_consent()

    def handle_consent(self):
        try:
            consent_button = self.page.locator("button:has-text('Consent')")
            consent_button.wait_for(state="visible", timeout=3000)
            consent_button.click()
        except:
            pass
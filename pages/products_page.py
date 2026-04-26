from conftest import handle_consent

class ProductsPage:
    URL = "https://automationexercise.com/products"

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)
        handle_consent(self.page)
        self.page.wait_for_timeout(1000)

    def search_product(self, product_name):
        self.page.fill("input#search_product", product_name)
        self.page.click("button#submit_search")

    def get_search_results(self):
        return self.page.locator(".productinfo").count()

    def get_page_title(self):
        return self.page.inner_text("h2.title.text-center")
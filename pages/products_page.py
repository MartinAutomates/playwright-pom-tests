from pages.base_page import BasePage

class ProductsPage(BasePage):
    URL = "https://automationexercise.com/products"

    def search_product(self, product_name):
        self.page.fill("input#search_product", product_name)
        self.page.click("button#submit_search")

    def get_search_results(self):
        return self.page.locator(".productinfo").count()

    def get_page_title(self):
        return self.page.inner_text("h2.title.text-center")
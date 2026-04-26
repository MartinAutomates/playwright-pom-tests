from conftest import handle_consent

class CartPage:
    URL = "https://automationexercise.com/view_cart"

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)
        handle_consent(self.page)
        self.page.wait_for_timeout(1000)

    def get_page_title(self):
        return self.page.inner_text("li.active")

    def is_cart_empty(self):
        empty = self.page.locator("b:has-text('Cart is empty!')")
        return empty.is_visible()

    def go_to_products(self):
        self.page.click("a[href='/products']")
        self.page.wait_for_timeout(1000)

    def get_cart_items_count(self):
        return self.page.locator("tr.cart_menu").count()
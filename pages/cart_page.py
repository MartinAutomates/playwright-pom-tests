from pages.base_page import BasePage

class CartPage(BasePage):
    URL = "https://automationexercise.com/view_cart"

    def get_page_title(self):
        return self.page.inner_text("li.active")

    def is_cart_empty(self):
        empty = self.page.locator("b:has-text('Cart is empty!')")
        return empty.is_visible()

    def go_to_products(self):
        self.page.click("a[href='/products']")

    def get_cart_items_count(self):
        return self.page.locator("tr.cart_menu").count()
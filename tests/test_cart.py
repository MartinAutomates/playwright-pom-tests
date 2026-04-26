from pages.cart_page import CartPage

def test_cart_page_loads(page):
    cart = CartPage(page)
    cart.navigate()
    assert page.url == "https://automationexercise.com/view_cart"

def test_cart_is_empty_by_default(page):
    cart = CartPage(page)
    cart.navigate()
    assert cart.is_cart_empty() == True

def test_cart_shows_empty_message(page):
    cart = CartPage(page)
    cart.navigate()
    empty_text = page.locator("b:has-text('Cart is empty!')")
    assert empty_text.is_visible()

def test_navigate_to_products_from_cart(page):
    cart = CartPage(page)
    cart.navigate()
    cart.go_to_products()
    assert page.url == "https://automationexercise.com/products"
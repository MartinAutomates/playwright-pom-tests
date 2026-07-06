from pages.cart_page import CartPage
from playwright.sync_api import expect

def test_cart_page_loads(page):
    cart = CartPage(page)
    cart.navigate(cart.URL)
    expect(page).to_have_url("https://automationexercise.com/view_cart")

def test_cart_is_empty_by_default(page):
    cart = CartPage(page)
    cart.navigate(cart.URL)
    assert cart.is_cart_empty() == True

def test_cart_shows_empty_message(page):
    cart = CartPage(page)
    cart.navigate(cart.URL)
    empty_text = page.locator("b:has-text('Cart is empty!')")
    expect(empty_text).to_be_visible()

def test_navigate_to_products_from_cart(page):
    cart = CartPage(page)
    cart.navigate(cart.URL)
    cart.go_to_products()
    expect(page).to_have_url("https://automationexercise.com/products")
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_complete_purchase_flow(page):
    # Step 1 - Login
    login = LoginPage(page)
    login.navigate()
    login.enter_email("your_email_here")
    login.enter_password("your_password_here")
    login.click_login_button()
    page.wait_for_timeout(1000)
    assert page.url == "https://automationexercise.com/"

    # Step 2 - Go to products and add one to cart
    page.goto("https://automationexercise.com/products")
    page.wait_for_timeout(1000)
    page.hover(".productinfo:first-child")
    page.click(".productinfo:first-child .btn")
    page.wait_for_timeout(1000)

    # Step 3 - Handle the "Added to cart" popup
    page.click("button:has-text('Continue Shopping')")
    page.wait_for_timeout(500)

    # Step 4 - Go to cart
    page.goto("https://automationexercise.com/view_cart")
    page.wait_for_timeout(1000)

    # Step 5 - Proceed to checkout
    page.click("a:has-text('Proceed To Checkout')")
    page.wait_for_timeout(1000)

    # Step 6 - Place order
    page.click("a:has-text('Place Order')")
    page.wait_for_timeout(1000)

    # Step 7 - Fill fake payment details
    page.fill("input[data-qa='name-on-card']", "Martin Stoyanov")
    page.fill("input[data-qa='card-number']", "4111111111111111")
    page.fill("input[data-qa='cvc']", "123")
    page.fill("input[data-qa='expiry-month']", "12")
    page.fill("input[data-qa='expiry-year']", "2027")

    # Step 8 - Confirm payment
    page.click("button[data-qa='pay-button']")
    page.wait_for_timeout(2000)

    # Step 9 - Verify order placed
    assert "payment_done" in page.url
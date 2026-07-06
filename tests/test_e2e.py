import os
import re
import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect

@pytest.mark.e2e
def test_complete_purchase_flow(page):
    # Step 1 - Login
    login = LoginPage(page)
    login.navigate(login.URL)
    login.enter_email()
    login.enter_password()
    login.click_login_button()
    expect(page).to_have_url("https://automationexercise.com/")

    # Step 2 - Go to products and add one to cart
    page.goto("https://automationexercise.com/products")
    page.hover(".productinfo:first-child")
    page.click(".productinfo:first-child .btn")

    # Step 3 - Handle the "Added to cart" popup
    page.click("button:has-text('Continue Shopping')")

    # Step 4 - Go to cart
    page.goto("https://automationexercise.com/view_cart")

    # Step 5 - Proceed to checkout
    page.click("a:has-text('Proceed To Checkout')")

    # Step 6 - Place order
    page.click("a:has-text('Place Order')")

    # Step 7 - Fill fake payment details
    page.fill("input[data-qa='name-on-card']", "Martin Stoyanov")
    page.fill("input[data-qa='card-number']", "4111111111111111")
    page.fill("input[data-qa='cvc']", "123")
    page.fill("input[data-qa='expiry-month']", "12")
    page.fill("input[data-qa='expiry-year']", "2027")

    # Step 8 - Confirm payment
    page.click("button[data-qa='pay-button']")

    # Step 9 - Verify order placed
    expect(page).to_have_url(re.compile("payment_done"))


@pytest.mark.e2e
def test_checkout_with_invalid_card(page):
    login = LoginPage(page)
    login.navigate(login.URL)
    login.enter_email()
    login.enter_password()
    login.click_login_button()

    page.goto("https://automationexercise.com/products")
    page.hover(".productinfo:first-child")
    page.click(".productinfo:first-child .btn")
    page.click("button:has-text('Continue Shopping')")

    page.goto("https://automationexercise.com/view_cart")
    page.click("a:has-text('Proceed To Checkout')")
    page.click("a:has-text('Place Order')")

    page.fill("input[data-qa='name-on-card']", "Martin Stoyanov")
    page.fill("input[data-qa='card-number']", "123")
    page.fill("input[data-qa='cvc']", "1")
    page.fill("input[data-qa='expiry-month']", "13")
    page.fill("input[data-qa='expiry-year']", "2020")

    page.click("button[data-qa='pay-button']")

    expect(page.locator("body")).not_to_contain_text("ORDER PLACED!")
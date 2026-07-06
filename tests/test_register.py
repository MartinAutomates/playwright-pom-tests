import os
from pages.register_page import RegisterPage
from playwright.sync_api import expect
import random

def test_register_page_loads(page):
    register = RegisterPage(page)
    register.navigate(register.URL)
    expect(page).to_have_url("https://automationexercise.com/login")

def test_register_with_existing_email(page):
    register = RegisterPage(page)
    register.navigate(register.URL)
    register.enter_name("Martin")
    register.enter_email(os.getenv("TEST_EMAIL"))
    register.click_signup_button()
    error = register.get_error_message()
    assert "Email Address already exist!" in error

def test_register_with_new_email(page):
    register = RegisterPage(page)
    register.navigate(register.URL)
    unique_email = f"testuser{random.randint(10000,99999)}@test.com"
    register.enter_name("Test User")
    register.enter_email(unique_email)
    register.click_signup_button()
    expect(page).to_have_url("https://automationexercise.com/signup")
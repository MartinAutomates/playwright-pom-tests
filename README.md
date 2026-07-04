# Playwright POM Test Framework 🎭

An automated QA test framework built with Python and Playwright using the Page Object Model (POM) design pattern. Tests the [AutomationExercise](https://automationexercise.com) e-commerce website.

## What it tests
- Homepage loading and navigation
- Login with valid and invalid credentials
- User registration
- Product search
- Shopping cart
- Full end-to-end purchase flow (login → add to cart → checkout → payment confirmation)

## Tech Stack
Python, Playwright, pytest

## Project Structure
- `pages/` — Page Object classes for each page
  - home_page.py, login_page.py, register_page.py, products_page.py, cart_page.py
- `tests/` — Test files
  - test_home.py, test_login.py, test_register.py, test_products.py, test_cart.py, test_e2e.py
- `conftest.py` — Browser setup and consent handler

## How to Run
1. Install dependencies: `pip install pytest-playwright`
2. Install browsers: `playwright install`
3. Run all tests: `pytest tests/ -v`

## Test Results
17 tests total — covering unit tests and a full end-to-end purchase flow.

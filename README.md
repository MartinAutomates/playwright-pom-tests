# Playwright POM Test Framework 🎭

An automated QA test framework built with Python and Playwright using the Page Object Model (POM) design pattern. Tests the [AutomationExercise](https://automationexercise.com) e-commerce website.

## What it tests
- Homepage loading and navigation
- Login with valid and invalid credentials
- User registration with test isolation (randomized data)
- Product search including edge cases (empty search, nonexistent products)
- Shopping cart
- Full end-to-end purchase flow (login → add to cart → checkout → payment confirmation)
- Negative testing (invalid payment details)

## Tech Stack
Python, Playwright, pytest, GitHub Actions

## Project Structure
- `pages/` — Page Object classes, all inheriting from a shared BasePage
  - base_page.py, home_page.py, login_page.py, register_page.py, products_page.py, cart_page.py
- `tests/` — Test files organized with pytest markers (@smoke, @e2e)
- `conftest.py` — Browser setup, environment-aware headless mode, screenshot-on-failure
- `.github/workflows/tests.yml` — CI/CD pipeline that runs all tests automatically on every push

## Key Features
- **Environment-based config** — credentials stored securely via `.env` (local) and GitHub Secrets (CI)
- **Proper Playwright waits and assertions** — no hardcoded timeouts, uses `expect()` for reliable checks
- **Test isolation** — registration tests use randomized data to avoid conflicts on reruns
- **Negative and edge case testing** — empty search, nonexistent products, invalid payment details
- **CI/CD with GitHub Actions** — tests run automatically on every push, headless on CI, visible locally
- **HTML reporting** — visual test reports generated automatically
- **Screenshots on failure** — automatic debugging aid when tests fail
- **Bot-detection bypass** — custom user-agent configuration to run reliably in cloud CI environments

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Install browsers: `playwright install`
3. Create a `.env` file with `TEST_EMAIL` and `TEST_PASSWORD`
4. Run all tests: `pytest tests/ -v`
5. Run only smoke tests: `pytest -m smoke -v`
6. Generate HTML report: `pytest tests/ -v --html=report.html --self-contained-html`

## Test Results
20 tests total — covering unit tests, negative testing, edge cases, and a full end-to-end purchase flow. Runs automatically via GitHub Actions CI/CD on every push.

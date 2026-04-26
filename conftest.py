import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def handle_consent(page):
    try:
        consent_button = page.locator("button:has-text('Consent')")
        if consent_button.is_visible():
            consent_button.click()
    except:
        pass
import os
from dotenv import load_dotenv
load_dotenv()

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def page(request):
    with sync_playwright() as p:
        is_ci = os.getenv("CI") == "true"
        browser = p.chromium.launch(headless=is_ci)
        page = browser.new_page()
        yield page

        if request.node.rep_call.failed:
            screenshot_path = f"screenshots/{request.node.name}.png"
            page.screenshot(path=screenshot_path)

        browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
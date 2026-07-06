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
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
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
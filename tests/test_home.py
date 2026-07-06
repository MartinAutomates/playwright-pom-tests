from pages.home_page import HomePage
from playwright.sync_api import expect

def test_homepage_loads(page):
    home = HomePage(page)
    home.navigate(home.URL)
    title = home.get_title()
    assert "Automation Exercise" in title

def test_login_link_works(page):
    home = HomePage(page)
    home.navigate(home.URL)
    home.click_login()
    expect(page).to_have_url("https://automationexercise.com/login")
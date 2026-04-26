from pages.home_page import HomePage

def test_homepage_loads(page):
    home = HomePage(page)
    home.navigate()
    title = home.get_title()
    assert "Automation Exercise" in title

def test_login_link_works(page):
    home = HomePage(page)
    home.navigate()
    home.click_login()
    assert page.url == "https://automationexercise.com/login"
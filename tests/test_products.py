from pages.products_page import ProductsPage

def test_products_page_loads(page):
    products = ProductsPage(page)
    products.navigate()
    assert page.url == "https://automationexercise.com/products"

def test_products_page_title(page):
    products = ProductsPage(page)
    products.navigate()
    title = products.get_page_title()
    assert "ALL PRODUCTS" in title
    
def test_search_returns_results(page):
    products = ProductsPage(page)
    products.navigate()
    products.search_product("dress")
    count = products.get_search_results()
    assert count > 0

def test_search_specific_product(page):
    products = ProductsPage(page)
    products.navigate()
    products.search_product("top")
    count = products.get_search_results()
    assert count > 0

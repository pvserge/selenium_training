from selenium.webdriver.common.by import By
from model.product import Product


def test_stickers(app):
    driver = app.wd
    driver.get("http://localhost/litecart/en/")

    def has_only_one_sub_element(element, *args):
        return len(element.find_elements(*args)) == 1

    products = driver.find_elements_by_css_selector("li.product")
    for product in products:
        assert has_only_one_sub_element(product, By.CSS_SELECTOR, "div.sticker")


def test_product_page(app):
    product_main = app.product.get_first_campaigns_main()
    product_detail = app.product.get_product_details(product_main)
    # check product name on both pages
    assert product_main.name == product_detail.name
    # check regular price on both pages
    assert product_main.price == product_detail.price
    # check campaign price on both pages
    assert product_main.auc_price == product_detail.auc_price
    # all 3 verifications above in one assert
    assert product_main == product_detail
    # check decoration of regular price (line-through) on main page
    assert product_main.price_decoration == "line-through"
    # check if campaign price is bold on main page
    assert int(product_main.auc_price_decoration) >= 700
    # check decoration of regular price (line-through) on appropriate product page
    assert product_detail.price_decoration == "line-through"
    # check if campaign price is bold on appropriate product page
    assert int(product_detail.auc_price_decoration) >= 700
    # check that campaign price is bigger on main page
    assert float(product_main.auc_price_size) > float(product_main.price_size)
    # check that campaign price is bigger on appropriate product page
    assert float(product_detail.auc_price_size) > float(product_detail.price_size)
    # check colors
    # check that regular price in grey on main page (R=G=B)
    assert int(product_main.price_color[0]) == int(product_main.price_color[1]) == int(product_main.price_color[2])
    # check that regular price in grey on appropriate product page (R=G=B)
    assert int(product_detail.price_color[0]) == int(product_detail.price_color[1]) == int(product_detail.price_color[2])
    # check that campaign price on main page has red color (G=B=0)
    assert int(product_main.auc_price_color[1]) == int(product_main.auc_price_color[2]) == 0
    # check that campaign price on appropriate product page has red color (G=B=0)
    assert int(product_detail.auc_price_color[1]) == int(product_detail.auc_price_color[2]) == 0


def test_add_product(app, data_products):
    product = data_products
    old_products = app.product.get_product_list_from_admin_page()
    app.product.add_new_product_to_catalog(product)
    new_products = app.product.get_product_list_from_admin_page()
    old_products.append(product)
    new_product_names_list = []
    for product in new_products:
        new_product_names_list.append(product.name)
    print(new_product_names_list)
    old_product_names_list = []
    for product in old_products:
        old_product_names_list.append(product.name)
    print(old_product_names_list)
    assert old_product_names_list.sort() == new_product_names_list.sort()


def test_log_while_clicking_products(app):
    assert app.product.check_log_clicking_products_on_admin_products_catalog()






from selenium.webdriver.common.by import By


def test_stickers(driver):
    driver.get("http://localhost/litecart/en/")

    def has_only_one_sub_element(element, *args):
        return len(element.find_elements(*args)) == 1

    products = driver.find_elements_by_css_selector("li.product")
    for product in products:
        assert has_only_one_sub_element(product, By.CSS_SELECTOR, "div.sticker")


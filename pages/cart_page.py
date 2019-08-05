from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.wd = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.wd.get("http://localhost/litecart/en/checkout")

    def is_on_this_page(self):
        if not ("/litecart/en/checkout" in self.wd.current_url and self.wd.find_element_by_css_selector("div#box-checkout-cart")):
            return False
        return True

    @property
    def products_table(self):
        return self.wd.find_element_by_css_selector("table.dataTable")

    @property
    def items_in_cart(self):
        return self.wd.find_elements_by_css_selector("ul.items li.item")

    @property
    def product_shortcut(self):
        return self.wd.find_elements_by_css_selector("li.shortcut a")[0]

    @property
    def remove_button(self):
        return self.wd.find_element_by_name("remove_cart_item")

    def are_elements_present(self, *args):
        return len(self.wd.find_elements(*args)) > 0

    def is_product_shortcut_exists(self):
        if self.are_elements_present(By.CSS_SELECTOR, "li.shortcut a"):
            return True
        else:
            return False

    def is_summary_table_exists(self):
        if self.are_elements_present(By.CSS_SELECTOR, "table.dataTable") > 0:
            return True
        else:
            return False





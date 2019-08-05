from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.wd = driver
        self.wait = WebDriverWait(driver, 5)

    @property
    def add_button(self):
        return self.wd.find_element_by_name("add_cart_product")

    def wait_presence_of(self, *args):
        return self.wait.until(EC.presence_of_element_located(*args))

    def get_cart_counter_text(self):
        cart_counter = self.wait_presence_of((By.CSS_SELECTOR, "div#cart span.quantity"))
        return cart_counter.text

    def are_elements_present(self, *args):
        return len(self.wd.find_elements(*args)) > 0

    def get_option_index_by_text(self, options, text):
        for i in range(len(options)):
            if options[i].text == text:
                return i

    def select_field_value(self, field_name, value):
        if value is not None:
            select = self.wd.find_element_by_css_selector("select[name='%s']" % field_name)
            options = self.wd.find_elements_by_css_selector("select[name='%s'] option" % field_name)
            index = self.get_option_index_by_text(options, value)
            self.wd.execute_script("arguments[0].selectedIndex = %s; arguments[0].dispatchEvent(new Event('change'))" % index, select)

    def select_small_size(self):
        if self.are_elements_present(By.CSS_SELECTOR, "[name='options[Size]']"):
            self.select_field_value("options[Size]", "Small")

    def wait_cart_refresh(self, text):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div#cart span.quantity"), str(int(text) + 1)))





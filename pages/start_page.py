from selenium.webdriver.support.wait import WebDriverWait


class StartPage:

    def __init__(self, driver):
        self.wd = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.wd.get("http://localhost/litecart/en/")
        self.wd.find_element_by_css_selector("div#box-account-login h3")

    def is_on_this_page(self):
        if not ("/litecart/en/" in self.wd.current_url and self.wd.find_element_by_css_selector("h3").text == "Login"):
            return False
        return True

    @property
    def cart_link(self):
        return self.wd.find_element_by_css_selector("div#cart a.link")

    @property
    def first_popular_product(self):
        return self.wd.find_elements_by_css_selector("div#box-most-popular li.product a.link")[0]


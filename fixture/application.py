from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from fixture.session import SessionHelper
from fixture.country import CountryHelper
from fixture.product import ProductHelper
from fixture.user import UserHelper


class Application:

    def __init__(self, browser):
        browser_upper = browser.upper()
        if browser_upper == "FIREFOX":
            self.wd = webdriver.Firefox()
        elif browser_upper == "CHROME":
            self.wd = webdriver.Chrome()
        elif browser_upper == "IE":
            self.wd = webdriver.Ie()
        elif browser_upper == "SAFARI":
            self.wd = webdriver.Safari()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.country = CountryHelper(self)
        self.wait = WebDriverWait(self.wd, 5)
        self.product = ProductHelper(self)
        self.user = UserHelper(self)

    def open_page(self, url):
        wd = self.wd
        wd.get(url)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        wd = self.wd
        wd.quit()

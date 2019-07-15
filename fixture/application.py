from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from fixture.session import SessionHelper
from fixture.country import CountryHelper


class Application:

    def __init__(self, browser):
        browser_upper = browser.upper()
        if browser_upper == "FIREFOX":
            self.wd = webdriver.Firefox()
        elif browser_upper == "CHROME":
            self.wd = webdriver.Chrome()
        elif browser_upper == "IE":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.country = CountryHelper(self)
        self.wait = WebDriverWait(self.wd, 10)

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

from selenium.webdriver.support import expected_conditions as EC


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_as_admin(self):
        wd = self.app.wd
        self.app.open_page("http://localhost/litecart/admin/login.php")
        wd.find_element_by_name("username").send_keys("admin")
        wd.find_element_by_name("password").send_keys("admin")
        wd.find_element_by_name("login").click()
        self.app.wait.until(EC.title_is("My Store"))

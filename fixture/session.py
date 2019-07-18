from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def are_elements_present(self, *args):
        return len(self.app.wd.find_elements(*args)) > 0

    def login_as_admin(self):
        wd = self.app.wd
        if not ("/litecart/admin/" in wd.current_url and self.are_elements_present(By.ID, "box-apps-menu")):
            self.app.open_page("http://localhost/litecart/admin/login.php")
            wd.find_element_by_name("username").send_keys("admin")
            wd.find_element_by_name("password").send_keys("admin")
            wd.find_element_by_name("login").click()
            self.app.wait.until(EC.title_is("My Store"))

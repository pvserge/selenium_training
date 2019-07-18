class UserHelper:

    def __init__(self, app):
        self.app = app

    def open_signup_page(self):
        wd = self.app.wd
        wd.get("http://localhost/litecart/en/create_account")

    def login(self, user):
        wd = self.app.wd
        self.app.open_page("http://localhost/litecart/")
        wd.find_element_by_css_selector("input[name=email]").send_keys(user.email)
        wd.find_element_by_css_selector("input[name=password]").send_keys(user.password)
        wd.find_element_by_css_selector("button[name=login]").click()
        wd.find_element_by_xpath("//div[@id='box-account']//a[contains(text(),'Logout')]")

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_option_index_by_text(self, options, text):
        for i in range(len(options)):
            if options[i].text == text:
                return i

    def select_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            select = wd.find_element_by_css_selector("select[name=%s]" % field_name)
            options = wd.find_elements_by_css_selector("select[name='%s'] option" % field_name)
            index = self.get_option_index_by_text(options, value)
            wd.execute_script("arguments[0].selectedIndex = %s; arguments[0].dispatchEvent(new Event('change'))" % index, select)

    def fill_form(self, user):
        self.change_field_value("tax_id", user.tax_id)
        self.change_field_value("company", user.company)
        self.change_field_value("firstname", user.first_name)
        self.change_field_value("lastname", user.last_name)
        self.change_field_value("address1", user.address1)
        self.change_field_value("address2", user.address2)
        self.change_field_value("postcode", user.postcode)
        self.change_field_value("city", user.city)
        self.select_field_value("country_code", user.country_name)
        self.select_field_value("zone_code", user.zone_name)
        self.change_field_value("email", user.email)
        self.change_field_value("phone", user.phone)
        self.change_field_value("password", user.password)
        self.change_field_value("confirmed_password", user.password)

    def sign_up(self, user):
        wd = self.app.wd
        # open signup page
        self.open_signup_page()
        # fill signup form
        self.fill_form(user)
        # submit
        wd.find_element_by_name("create_account").click()
        wd.find_element_by_xpath("//div[@id='box-account']//a[contains(text(),'Logout')]")

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='box-account']//a[contains(text(),'Logout')]").click()





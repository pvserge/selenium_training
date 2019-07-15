from model.country import Country


class CountryHelper:

    def __init__(self, app):
        self.app = app

    def open_country_page(self):
        wd = self.app.wd
        self.app.session.login_as_admin()
        wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    def get_country_list(self):
        wd = self.app.wd
        self.open_country_page()
        country_list = []
        for element in wd.find_elements_by_css_selector("tr.row"):
            text = element.text
            id = element.find_element_by_name('selected[]').get_attribute('value')
            country_list.append(Country(name=text, id=id))
        return list(country_list)



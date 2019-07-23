from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from model.country import Country
from model.zone import Zone


class CountryHelper:

    def __init__(self, app):
        self.app = app

    def open_countries_page(self):
        wd = self.app.wd
        self.app.session.login_as_admin()
        wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    def open_geozones_page(self):
        wd = self.app.wd
        self.app.session.login_as_admin()
        wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

    def open_first_country_to_edit(self):
        wd = self.app.wd
        self.open_countries_page()
        wd.find_element_by_css_selector("a[title='Edit']").click()
        wd.find_element_by_css_selector("td#content h1")

    def get_country_list_countries_page(self):
        wd = self.app.wd
        self.open_countries_page()
        country_list = []
        for row in wd.find_elements_by_css_selector("tr.row"):
            cells = row.find_elements_by_css_selector("td")
            id = cells[2].text
            code = cells[3].text
            name = cells[4].text
            link = cells[4].find_element_by_css_selector("a").get_attribute("href")
            zones = cells[5].text
            country_list.append(Country(id=id, code=code, name=name, link=link, zones=zones))
        return list(country_list)

    def get_country_list_geozones_page(self):
        wd = self.app.wd
        self.open_geozones_page()
        country_list = []
        for row in wd.find_elements_by_css_selector("tr.row"):
            cells = row.find_elements_by_css_selector("td")
            id = cells[1].text
            name = cells[2].text
            link = cells[2].find_element_by_css_selector("a").get_attribute("href")
            zones = cells[3].text
            country_list.append(Country(id=id, name=name, link=link, zones=zones))
        return list(country_list)

    def get_zones_list_edit_country_page(self, country):
        wd = self.app.wd
        wd.get(country.link)
        zones_list = []
        for row in wd.find_elements_by_css_selector("table#table-zones tr:not(.header)"):
            cells = row.find_elements_by_css_selector("td")
            id = cells[1].text
            code = cells[2].text
            name = cells[3].text
            zones_list.append(Zone(id=id, code=code, name=name))
        return list(zones_list)

    def get_zones_list_edit_zone_page(self, country):
        wd = self.app.wd
        wd.get(country.link)
        zones_list = []
        for row in wd.find_elements_by_css_selector("table#table-zones tr:not(.header)"):
            cells = row.find_elements_by_css_selector("td")
            id = cells[0].text
            if not id == "":
                select = Select(wd.find_element_by_css_selector("[name*='zones[%s][zone_code']" % id))
                name = select.first_selected_option.text
                zones_list.append(Zone(id=id, name=name))
        return list(zones_list)

    def get_external_links_on_edit_page(self):
        wd = self.app.wd
        self.open_first_country_to_edit()
        return wd.find_elements_by_xpath("//i[contains(@class, 'fa-external-link')]/..")

    def there_is_window_other_than(self, old_windows):
        wd = self.app.wd
        windows = wd.window_handles
        for window in windows:
            if window not in old_windows:
                return window

    def check_external_links_on_edit_page(self):
        wd = self.app.wd
        wait = self.app.wait
        main_window = wd.current_window_handle
        old_windows = wd.window_handles
        links = self.get_external_links_on_edit_page()
        print("Amount of links to test is: %s" % str(len(links)))
        for link in links:
            print("URL under test is: %s" % link.get_attribute("href"))
            link.click()
            wait.until(EC.new_window_is_opened(old_windows))
            new_window = self.there_is_window_other_than(old_windows)
            wd.switch_to.window(new_window)
            if "/litecart/admin" in wd.current_url:
                print("The url in current window is wrong")
                return False
            wd.close()
            wd.switch_to.window(main_window)
        return True


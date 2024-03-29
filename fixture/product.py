import re
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from model.product import Product
from pages.start_page import StartPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class ProductHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd
        self.start_page = StartPage(self.wd)
        self.product_page = ProductPage(self.wd)
        self.cart_page = CartPage(self.wd)

    def open_start_page(self):
        if not self.start_page.is_on_this_page():
            self.start_page.open()

    def are_elements_present(self, *args):
        return len(self.app.wd.find_elements(*args)) > 0

    def open_catalog_page(self):
        wd = self.app.wd
        session = self.app.session
        session.login_as_admin()
        if not (wd.current_url.endswith("/litecart/admin/?app=catalog&doc=catalog") and wd.find_element_by_css_selector("h1").text == "Catalog"):
            wd.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
            wd.find_element_by_css_selector("td#content h1")

    def open_products_on_catalog_page(self):
        wd = self.app.wd
        session = self.app.session
        session.login_as_admin()
        if not (wd.current_url.endswith("/litecart/admin/?app=catalog&doc=catalog&category_id=1")
                and wd.find_element_by_css_selector("h1").text == "Catalog"):
            wd.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
            wd.find_element_by_css_selector("td#content h1")

    def open_cart_page(self):
        if not self.cart_page.is_on_this_page():
            self.open_start_page()
            self.start_page.cart_link.click()

    def get_first_campaigns_main(self):
        wd = self.app.wd
        self.open_start_page()
        product = wd.find_element_by_css_selector("div#box-campaigns li.product")
        name = product.find_element_by_css_selector("div.name").text
        manufacturer = product.find_element_by_css_selector("div.manufacturer").text
        price = product.find_element_by_css_selector("s.regular-price").text
        price_color = re.search(r'\((.*?)\)', product.find_element_by_css_selector("s.regular-price")
                                .value_of_css_property("color")).group(1).replace(" ", "").split(',')
        price_decoration = product.find_element_by_css_selector("s.regular-price").value_of_css_property("text-decoration-line")
        price_size = product.find_element_by_css_selector("s.regular-price").value_of_css_property(
            "font-size")[:-2]
        auc_price = product.find_element_by_css_selector(".campaign-price").text
        auc_price_color = re.search(r'\((.*?)\)', product.find_element_by_css_selector(".campaign-price")
                                    .value_of_css_property("color")).group(1).replace(" ", "").split(',')
        auc_price_decoration = product.find_element_by_css_selector(".campaign-price").value_of_css_property(
            "font-weight")
        auc_price_size = product.find_element_by_css_selector(".campaign-price").value_of_css_property(
            "font-size")[:-2]
        link = product.find_element_by_css_selector("a.link").get_attribute("href")
        return Product(name=name, manufacturer=manufacturer, price=price, price_color=price_color,
                       price_decoration=price_decoration, price_size=price_size, auc_price=auc_price,
                       auc_price_color=auc_price_color, auc_price_decoration=auc_price_decoration,
                       auc_price_size=auc_price_size, link=link)

    def get_product_details(self, product):
        wd = self.app.wd
        wd.get(product.link)
        name = wd.find_element_by_css_selector("h1.title").text
        price = wd.find_element_by_css_selector("s.regular-price").text
        price_color = re.search(r'\((.*?)\)', wd.find_element_by_css_selector("s.regular-price")
                                .value_of_css_property("color")).group(1).replace(" ", "").split(',')
        price_decoration = wd.find_element_by_css_selector("s.regular-price").value_of_css_property(
            "text-decoration-line")
        price_size = wd.find_element_by_css_selector("s.regular-price").value_of_css_property(
            "font-size")[:-2]
        auc_price = wd.find_element_by_css_selector(".campaign-price").text
        auc_price_color = re.search(r'\((.*?)\)', wd.find_element_by_css_selector(".campaign-price")
                                    .value_of_css_property("color")).group(1).replace(" ", "").split(',')
        auc_price_decoration = wd.find_element_by_css_selector(".campaign-price").value_of_css_property(
            "font-weight")
        auc_price_size = wd.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")[:-2]
        return Product(name=name, price=price, price_color=price_color, price_decoration=price_decoration,
                       price_size=price_size, auc_price=auc_price, auc_price_color=auc_price_color,
                       auc_price_decoration=auc_price_decoration, auc_price_size=auc_price_size)

    def get_product_list_from_admin_page(self):
        wd = self.app.wd
        self.open_catalog_page()
        table = wd.find_elements_by_css_selector("table.dataTable tr.row")
        product_list = []
        for row in table:
            cells = row.find_elements_by_css_selector("td")
            product_list.append(Product(name=cells[2].find_element_by_css_selector("a").text))
        return list(product_list)

    def get_option_value_by_text(self, options, text):
        for i in range(len(options)):
            if options[i].find_element_by_xpath("//%s/.." % options[i]).text == text:
                return options[i].get_attribute("value")

    def get_option_index_by_text(self, options, text):
        for i in range(len(options)):
            if options[i].text == text:
                return i

    def check_radiobutton_by_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            option = wd.find_element_by_css_selector("input[name=%s][value='%s']" % (field_name, value))
            if not option.get_attribute("checked"):
                option.click()

    def check(self, name, value):
        wd = self.app.wd
        checkbox = wd.find_element_by_css_selector("input[name='%s'][value='%s']" % (name, value))
        if not checkbox.get_attribute("checked"):
            checkbox.click()

    def select_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            select = wd.find_element_by_css_selector("select[name='%s']" % field_name)
            options = wd.find_elements_by_css_selector("select[name='%s'] option" % field_name)
            index = self.get_option_index_by_text(options, value)
            wd.execute_script("arguments[0].selectedIndex = %s; arguments[0].dispatchEvent(new Event('change'))" % index, select)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def add_new_product_to_catalog(self, product):
        wd = self.app.wd
        self.open_catalog_page()
        wd.find_element_by_xpath("//a[contains(text(),'Add New Product')]").click()
        # fill form on General tab
        wd.find_element_by_xpath("//a[@href='#tab-general']").click()
        time.sleep(3)
        self.check_radiobutton_by_value("status", product.status)
        self.change_field_value("name[en]", product.name)
        self.change_field_value("code", product.code)
        self.check("product_groups[]", product.gender)
        self.change_field_value("quantity", product.qty)
        wd.find_element_by_name("new_images[]").send_keys(product.image)
        self.change_field_value("date_valid_from", product.date_from)
        self.change_field_value("date_valid_to", product.date_to)
        # fill form on Information tab
        wd.find_element_by_xpath("//a[@href='#tab-information']").click()
        time.sleep(3)
        self.select_field_value("manufacturer_id", product.manufacturer)
        self.change_field_value("keywords", product.keywords)
        self.change_field_value("short_description[en]", product.short_description)
        self.change_field_value("description[en]", product.description)
        self.change_field_value("head_title[en]", product.title)
        self.change_field_value("meta_description[en]", product.meta)
        ## fill form on Prices tab
        wd.find_element_by_xpath("//a[@href='#tab-prices']").click()
        time.sleep(3)
        self.change_field_value("purchase_price", product.price)
        self.select_field_value("purchase_price_currency_code", product.currency)
        # submit form
        wd.find_element_by_css_selector("button[name=save]").click()
        wd.find_element_by_css_selector("td#content h1")

    def add_first_product_to_cart(self):
        self.open_start_page()
        self.start_page.first_popular_product.click()
        self.product_page.select_small_size()
        text = self.product_page.get_cart_counter_text()
        self.product_page.add_button.click()
        self.product_page.wait_cart_refresh(text)

    def delete_first_product_from_cart(self):
        wait = self.app.wait
        self.open_cart_page()
        table = self.cart_page.products_table
        if self.cart_page.is_product_shortcut_exists():
            self.cart_page.product_shortcut.click()
        self.cart_page.remove_button.click()
        wait.until(EC.staleness_of(table))

    def delete_products_from_cart(self):
        self.open_cart_page()
        items = self.cart_page.items_in_cart
        for i in range(len(items)):
            self.delete_first_product_from_cart()

    def is_summary_table_exists(self):
        if self.cart_page.is_summary_table_exists():
            return True
        else:
            return False

    def get_products_from_admin_products_catalog(self):
        wd = self.app.wd
        self.open_products_on_catalog_page()
        table = wd.find_elements_by_css_selector("table.dataTable tr.row")
        product_list = []
        for row in table:
            cells = row.find_elements_by_css_selector("td")
            name = cells[2].find_element_by_css_selector("a").text
            link = cells[2].find_element_by_css_selector("a").get_attribute("href")
            product_list.append(Product(name=name, link=link))
        return list(product_list)

    def check_log_clicking_products_on_admin_products_catalog(self):
        wd = self.app.wd
        result = True
        products = self.get_products_from_admin_products_catalog()
        for product in products:
            print("Go to product %s by link %s" % (product.name, product.link))
            wd.get(product.link)
        messages = wd.get_log("browser")
        if len(messages) > 0:
            for msg in messages:
                print(msg)
                result = False
        return result






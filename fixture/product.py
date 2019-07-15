from model.product import Product


class ProductHelper:

    def __init__(self, app):
        self.app = app

    def open_product_page(self):
        wd = self.app.wd
        wd.get("http://localhost/litecart/en/")

    def get_first_campaigns_main(self):
        wd = self.app.wd
        self.open_product_page()
        product = wd.find_element_by_css_selector("div#box-campaigns li.product")
        name = product.find_element_by_css_selector("div.name").text
        manufacturer = product.find_element_by_css_selector("div.manufacturer").text
        price = product.find_element_by_css_selector("s.regular-price").text
        price_color = product.find_element_by_css_selector("s.regular-price").value_of_css_property("color")
        price_decoration = product.find_element_by_css_selector("s.regular-price").value_of_css_property("text-decoration-line")
        price_size = product.find_element_by_css_selector("s.regular-price").value_of_css_property(
            "font-size")[:-2]
        auc_price = product.find_element_by_css_selector(".campaign-price").text
        auc_price_color = product.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
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
        price_color = wd.find_element_by_css_selector("s.regular-price").value_of_css_property("color")
        price_decoration = wd.find_element_by_css_selector("s.regular-price").value_of_css_property(
            "text-decoration-line")
        price_size = wd.find_element_by_css_selector("s.regular-price").value_of_css_property(
            "font-size")[:-2]
        auc_price = wd.find_element_by_css_selector(".campaign-price").text
        auc_price_color = wd.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
        auc_price_decoration = wd.find_element_by_css_selector(".campaign-price").value_of_css_property(
            "font-weight")
        auc_price_size = wd.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")[:-2]
        return Product(name=name, price=price, price_color=price_color, price_decoration=price_decoration,
                       price_size=price_size, auc_price=auc_price, auc_price_color=auc_price_color,
                       auc_price_decoration=auc_price_decoration, auc_price_size=auc_price_size)



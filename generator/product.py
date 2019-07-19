import random
import string
import datetime
import os.path
from model.product import Product


class ProductGenerator:

    def random_string(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits + " " * 10 + "." + "_"
        return prefix + "".join([random.choice(symbols) for i in range(maxlen)])

    def random_digits(self, maxlen):
        digits = string.digits
        return "".join([random.choice(digits) for i in range(maxlen)])

    def get_date(self, when):
        if when == "today":
            return datetime.datetime.now().strftime("%Y-%m-%d")
        if when == "nextyear":
            return (datetime.datetime.now() + datetime.timedelta(days=365)).strftime("%Y-%m-%d")

    def get_image(self, file):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file)

    def generate_product(self):
        return Product(name="N Bad Duck", status="1", code=self.random_digits(3), gender="1-3",
                       qty=self.random_digits(2), image=self.get_image("resources/images/upside_down_duck.png"),
                       date_from=self.get_date("today"), date_to=self.get_date("nextyear"),
                       manufacturer="ACME Corp.", keywords=self.random_string("", 5),
                       short_description=self.random_string("desc: ", 5), description=self.random_string("", 20),
                       title="Title", meta="Meta", price=self.random_digits(2), currency="US Dollars")

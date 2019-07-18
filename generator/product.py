import random
import string
from model.product import Product


class ProductGenerator:

    def random_string(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits + " " * 10 + "." + "_"
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def random_digits(self, maxlen):
        digits = string.digits
        return "".join([random.choice(digits) for i in range(random.randrange(maxlen))])

    def generate_product(self):
        return Product(name="Bad Duck", status="Enabled", code=self.random_digits(3), gender="1-3",
                       qty=self.random_digits(2), image="", date_from="07182019", date_to="07182020",
                       manufacturer="ACME Corp.", keywords=self.random_string("", 5),
                       short_description=self.random_string("desc: ", 5), description=self.random_string("", 20),
                       title="Title", meta="Meta", price=self.random_digits(2), currency="US Dollars")

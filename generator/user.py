import random
import string
from model.user import User


class UserGenerator:

    def random_string(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits + " " * 10 + "." + "_"
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def random_phone(self, maxlen):
        digits = string.digits
        prefix = "+111"
        index = random.randrange(len(prefix))
        return prefix[index] + "".join([random.choice(digits) for i in range(random.randrange(maxlen))])

    def random_email(self, maxlen):
        symbols = string.ascii_lowercase
        digits = string.digits
        prefix = "".join([random.choice(symbols+digits) for i in range(maxlen)])
        dmnname = "".join([random.choice(symbols+digits) for i in range(1, maxlen)])
        zone = "".join([random.choice(symbols) for i in range(3)])
        return "%s@%s.%s" % (prefix, dmnname, zone)

    def generate_user(self):
        return User(first_name=self.random_string("FN_", 5), last_name=self.random_string("LN_", 5),
                    address1=self.random_string("A1: ", 5), postcode="11111", city="Boston",
                    country_name="United States", zone_name='Massachusetts', phone=self.random_phone(5),
                    email=self.random_email(5), password='test123')

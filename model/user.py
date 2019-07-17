class User:

    def __init__(self, tax_id=None, company=None, first_name=None, last_name=None, address1=None, address2=None,
                 postcode=None, city=None, country_name=None, zone_name=None, email=None, phone=None, newsletter=None,
                 password=None):
        self.tax_id = tax_id
        self.company = company
        self.first_name = first_name
        self.last_name = last_name
        self.address1 = address1
        self.address2 = address2
        self.postcode = postcode
        self.city = city
        self.country_name = country_name
        self.zone_name = zone_name
        self.email = email
        self.phone = phone
        self.newsletter = newsletter
        self.password = password

    def __repr__(self):
        return "%s:%s:%s" % (self.first_name, self.last_name, self.email)

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name



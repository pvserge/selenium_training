class Product:

    def __init__(self, name=None, manufacturer=None, price=None, auc_price=None, price_color=None, auc_price_color=None,
                 price_decoration=None, auc_price_decoration=None, price_size=None, auc_price_size=None, link=None):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.price_color = price_color
        self.price_decoration = price_decoration
        self.price_size = price_size
        self.auc_price = auc_price
        self.auc_price_color = auc_price_color
        self.auc_price_decoration = auc_price_decoration
        self.auc_price_size = auc_price_size
        self.link = link
        self.status = status
        self.code = code
        self.gender = gender
        self.qty = qty
        self.image = image
        self.date_from = date_from
        self.date_to = date_to
        self.keywords = keywords
        self.short_description = short_description
        self.description = description
        self.title = title
        self.meta = meta

    def __repr__(self):
        return "%s:%s:%s" % (self.name, self.price, self.auc_price)

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.auc_price == other.auc_price

    def get_name(self):
        return self.name

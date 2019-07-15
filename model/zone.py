class Zone:

    def __init__(self, id=None, code=None, name=None, link=None, zones=None):
        self.id = id
        self.code = code
        self.name = name
        self.link = link
        self.zones = zones

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.name == other.name



class Zone:

    def __init__(self, id=None, code=None, name=None):
        self.id = id
        self.code = code
        self.name = name

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.code, self.name)

    def __eq__(self, other):
        return self.name == other.name

    def get_name(self):
        return self.name


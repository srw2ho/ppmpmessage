class Limits(object):

    allowed_keys = ['lowerError', 'lowerWarn', 'target', 'upperError', 'upperWarn']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.allowed_keys:
                setattr(self, key, value)
            else:
                raise Exception(f"{key} is not an allowed attribute name!")

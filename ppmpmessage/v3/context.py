class Context(object):

    allowed_keys = ['limits', 'namespace', 'type', 'unit', 'additionalData']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.allowed_keys:
                setattr(self, key, value)
            else:
                raise Exception(f"{key} is not an allowed attribute name!")

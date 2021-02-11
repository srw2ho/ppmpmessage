class SpecialValue(object):

    allowed_keys = ['time', 'name']

    def __init__(self, value, **kwargs):
        self.value = value

        for key, value in kwargs.items():
            if key in self.allowed_keys:
                setattr(self, key, value)
            else:
                raise Exception(f"{key} is not an allowed attribute name!")

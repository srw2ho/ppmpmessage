class Message(object):

    allowed_keys = ['description', 'hint', 'origin', 'severity', 'title', 'type', 'additionalData']

    def __init__(self, ts, code, **kwargs):
        self.ts = ts
        self.code = code

        for key, value in kwargs.items():
            if key in self.allowed_keys:
                setattr(self, key, value)
            else:
                raise Exception(f"{key} is not an allowed attribute name!")

class Process(object):

    allowed_keys = ['externalId', 'program', 'result', 'additionalData']

    def __init__(self, ts, **kwargs):
        self.ts = ts

        for key, value in kwargs.items():
            if key in self.allowed_keys:
                setattr(self, key, value)
            else:
                raise Exception(f"{key} is not an allowed attribute name!")

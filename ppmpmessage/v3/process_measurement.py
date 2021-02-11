class ProcessMeasurement(object):

    allowed_keys = ['code', 'context', 'name', 'phase', 'result', 'specialValues', 'additionalData']

    def __init__(self, ts, series, **kwargs):
        self.ts = ts
        self.series = series

        for key, value in kwargs.items():
            if key in self.allowed_keys:
                setattr(self, key, value)
            else:
                raise Exception(f"{key} is not an allowed attribute name!")

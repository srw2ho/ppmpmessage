class Series(object):

    def __init__(self, time, **kwargs):
        self.time = time

        for key, value in kwargs.items():
            setattr(self, key, value)

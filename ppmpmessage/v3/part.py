class Part(object):

    allowed_keys = ['code', 'type', 'typeId', 'result', 'additionalData']
    map_keys = {
        '_id': 'id'
    }

    def __init__(self, _id, **kwargs):
        self._id = _id

        for key, value in kwargs.items():
            if key in self.allowed_keys:
                setattr(self, key, value)
            else:
                raise Exception(f"{key} is not an allowed attribute name!")

    def __getstate__(self):
        odict = self.__dict__

        # create new dictionary entries for all maped variables and delete the old representations
        for k, v in self.map_keys.items():
            if k in odict:
                odict[v] = odict[k]
                del odict[k]

        return odict

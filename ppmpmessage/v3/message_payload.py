class MessagePayload(object):

    map_keys = {
        'content_spec': 'content-spec'
    }

    def __init__(self, device, messages, content_spec='urn:spec://eclipse.org/unide/machine-message#v3'):
        self.content_spec = content_spec
        self.device = device
        self.messages = messages

    def __getstate__(self):
        odict = self.__dict__

        # create new dictionary entries for all maped variables and delete the old representations
        for k, v in self.map_keys.items():
            if k in odict:
                odict[v] = odict[k]
                del odict[k]

        return odict

    def to_ppmp(self):
        """ Dumps the object to JSON format

        Returns:
            [str] -- Object in JSON
        """
        # return dumps(self)
        return self

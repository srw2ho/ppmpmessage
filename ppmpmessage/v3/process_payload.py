class ProcessPayload(object):

    allowed_keys = ['part']
    map_keys = {
        'content_spec': 'content-spec'
    }

    def __init__(self, device, process, measurements, content_spec="urn:spec://eclipse.org/unide/process-message#v3", **kwargs):
        self.device = device
        self.process = process
        self.measurements = measurements
        self.content_spec = content_spec

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
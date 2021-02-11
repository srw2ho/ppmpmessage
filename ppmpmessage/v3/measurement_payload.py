integer_types = (int,)
class MeasurementPayload(object):

    allowed_keys = ['part']
    map_keys = {
        'content_spec': 'content-spec'
    }

    def __init__(self, device, measurements, content_spec="urn:spec://eclipse.org/unide/measurement-message#v3", **kwargs):
        self.content_spec = content_spec
        self.device = device
        self.measurements = measurements

        for key, value in kwargs.items():
            if key in self.allowed_keys:
                if (isinstance(value,  integer_types) and not isinstance(value, bool)):
                   conv= float(value)
                else :conv= value
                setattr(self, key, conv)
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

    def to_ppmp(self):
        """ Dumps the object to JSON format

        Returns:
            [str] -- Object in JSON
        """
        # return dumps(self)
        return self

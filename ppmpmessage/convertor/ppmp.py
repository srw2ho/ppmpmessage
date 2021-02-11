import json
from unide.util import loads
from datetime import timedelta


class PPMPObject(object):
    """ Class that represents a PPMP object and allows to transform it to InfluxDB format

    Arguments:
        object {[type]} -- [description]
    """

    def __init__(self, json):
        self.ppmp = loads(json, validate=True)


    def export_to_influxdb(self):
        """ Export object information to InfluxDB format
        """
        data = []

        # get deviceID
        deviceID = self.ppmp.device.deviceID

        # iterate all measurements
        for measurement in self.ppmp.measurements:
            timestamp = measurement.ts
            offsets = measurement.series['offsets']

            # iterate over all values (get total number by # of offsets)
            for index in range(0, len(measurement.series.offsets)):
                fields = {}
                # iterate all dimensions in measurement
                for dimension in measurement.series.dimensions:
                    values = measurement.series[dimension]

                    # add to fields
                    fields[dimension] = values[index]

                data.append({
                    "measurement": deviceID,
                    #"tags": { "deviceID": deviceID },
                    "time": str(timestamp + timedelta(milliseconds=offsets[index])), # timestamp + offset [ms]
                    "fields": fields
                })

        #return json.dumps(data)
        return data
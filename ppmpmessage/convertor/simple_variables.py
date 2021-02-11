from ppmpmessage.v3.measurement_payload import MeasurementPayload
from ppmpmessage.v3.series import Series
from ppmpmessage.v3.time_measurement import TimeMeasurement
from ppmpmessage.v3.util import dumps
from dateutil.parser import parse


class SimpleVariables(object):
    """ Class that represents a simple JSON object consisting of variables ([identifier] = value) and timestamp

    Arguments:
        object {[type]} -- [description]
    """

    def __init__(self, device, variables, timestamp):
        self.device = device
        self.variables = variables
        self.timestamp = parse(timestamp).isoformat()


    def to_ppmp(self):
        """ convert object to PPMPv3 representation
        """
        measurements = []

        series = Series(
            [0],
            **{key: [value] for key, value in self.variables.items()}
        )

        measurements.append(TimeMeasurement(self.timestamp, series))

        return dumps(MeasurementPayload(self.device, measurements).to_ppmp())



from mqttconnector.client import MQTTClient

from ppmpmessage.v3.device_state import DeviceState
from ppmpmessage.v3.device import Device
from ppmpmessage.v3.series import Series
from ppmpmessage.v3.time_measurement import TimeMeasurement
from ppmpmessage.v3.util import machine_message_generator, measurement_payload_generator
from ZeromqDevicebase.devicebase import grafanaDevice

# MQTT_HOST = '10.33.198.103'
MQTT_HOST = 'localhost'
MQTT_PORT = 8883
MQTT_USER = ''
MQTT_PASSWORD = ''
MQTT_TLS_CERT = ''
DEVICE_TYPE = 'PPMP'
SUBSCRIBE_PORT = 5580

class PPMPPublisher:

    def __init__(self):
        # connect to MQTT
        self.client = MQTTClient(host=MQTT_HOST, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, tls_cert=MQTT_TLS_CERT)

        self.device = Device(
            state=DeviceState.ERROR,
            additionalData={
                'type': DEVICE_TYPE
            },
        )

        # set up ZeroMQ data sink
        self.consumer_inst = grafanaDevice(SUBSCRIBE_PORT, None)
        self.consumer_inst.connect(self.publish)()

    def connect(self):
        """ Connect to MQTT and set up LWTs
        """
        # create machine message with state ERROR (LWT) (do this before(!) connect)
        self.client.last_will(
            self.device.info_topic(),
            machine_message_generator(self.device, state=DeviceState.ERROR, code="offline"),
            retain=True
        )

        self.client.connect(forever=True)

        # create machine message with state=ON and code=online (retain)
        self.client.publish(
            self.device.info_topic(),
            machine_message_generator(self.device),
            retain=True
        )

        # do not exit, instead wait for changes
        self.client.loop()


    def publish(self, topic, **kwargs):
        """ Publishes data in PPMP structure via MQTT

        Arguments:
            series {obj} -- Series with value names as obj-key, values list ast obj-value
            timestamp {str} -- Reference timestamp
            offsets {list} -- List of offsets (same size as data value is required!)
        """
        # create a measurements
        measurements = [ TimeMeasurement(value['timestamp'], Series([0], **{key: value['values']})) for key, value in kwargs.items() ]

        # publish data via MQTT
        self.client.publish(
            self.device.ppmp_topic(),
            measurement_payload_generator(self.device, measurements)
        )

if __name__ == '__main__':
    publisher = PPMPPublisher()
    publisher.connect()

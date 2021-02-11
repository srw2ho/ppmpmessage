import random
import time

from mqttconnector.client import MQTTClient

from ppmpmessage.v3.device_state import DeviceState
from ppmpmessage.v3.device import Device
from ppmpmessage.v3.series import Series
from ppmpmessage.v3.time_measurement import TimeMeasurement
from ppmpmessage.v3.util import local_now, machine_message_generator, measurement_payload_generator

MQTT_NET_NAME = 'mh'
# MQTT_HOST = '10.33.198.103'
MQTT_HOST = 'localhost'
MQTT_PORT = 8883
MQTT_USER = ''
MQTT_PASSWORD = ''
MQTT_TLS_CERT = ''
#MQTT_TLS_CERT = ''
DEVICE_TYPE = 'ABC4000'

VARIABLES = [
    "Leakage1",
    "Leakage2",
    "Leakage3",
    "Leakage4",
    "Leakage5",
    "Leakage6",
    "Leakage7",
    "Leakage8",
    "Leakage9",
    "Leakage10",
]

SERIES_RANGE = [random.uniform(0, 0.2) for index in range(len(VARIABLES))]
SERIES_BASE = {index: random.uniform(0, 10) for index in range(len(VARIABLES))}
SERIES_LENGTH = 10

def get_random_measurements(variable):
    index = VARIABLES.index(variable)
    value = SERIES_BASE[index]

    meas_list = [random.uniform(value - SERIES_RANGE[index], value + SERIES_RANGE[index]) for _ in range(10)]
    return meas_list

if __name__ == '__main__':
    # connect to MQTT
    client = MQTTClient(host=MQTT_HOST, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, tls_cert=MQTT_TLS_CERT)

    device = Device(
        state=DeviceState.ERROR,
        additionalData={
            'type': DEVICE_TYPE
        },
    )

    # create machine message with state ERROR (LWT) (do this before(!) connect)
    client.last_will(
        device.info_topic(),
        machine_message_generator(device, state=DeviceState.ERROR, code="offline"),
        retain=True
    )

    client.connect()

    # create machine message with state=ON and code=online (retain)
    client.publish(
        device.info_topic(),
        machine_message_generator(device),
        retain=True
    )

    while True:
        measurements = []

        # create 3 TimeMeasurements
        for i in range(1):
            # add 5 random series to measurement (10 millisecond offsets)
            series = Series(
                [index * 10 for index in range(len(VARIABLES))],
                **{var: get_random_measurements(var) for var in VARIABLES}
            )
            measurement = TimeMeasurement(local_now(), series)
            measurements.append(measurement)

        client.publish(
            device.ppmp_topic(),
            measurement_payload_generator(device, measurements)
        )

        time.sleep(1)

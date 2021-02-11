from os import urandom
from ppmpmessage.v3.util import local_now
import unittest

from ppmpmessage.publisher import PPMPPublisher

class PPMPPublisher(unittest.TestCase):

    def test_publish(self):
        publisher = PPMPPublisher()
        publisher.connect()

        while True:
            series = {
                'Temp1': [urandom.uniform(0, 0.2) for index in range(10)],
                'Temp2': [urandom.uniform(0, 0.2) for index in range(10)],
                'Temp3': [urandom.uniform(0, 0.2) for index in range(10)],
            }
            timestamp = local_now()
            offsets = list(range(0, 100, 10))

            publisher.publish(series, timestamp, offsets)

            time.sleep(1)


if __name__ == '__main__':
    unittest.main()

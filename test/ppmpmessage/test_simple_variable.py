import unittest
import json
import os
import sys
sys.path.append(os.getcwd())

from ppmpmessage.convertor.simple_variables import SimpleVariables
from dateutil.tz import tzoffset
from ppmpmessage.v3.util import local_now


class TestPPMPObject(unittest.TestCase):

    def test_to_ppmp_single(self):
        timestamp = local_now()
        variables = {
            'a': 'aa',
        }
        sv = SimpleVariables(variables, timestamp, "testdevice", "testid")
        ppmp = sv.to_PPMP()

        self.assertIsNotNone(sv)
        self.assertIsNotNone(ppmp)

        json_ppmp = json.loads(ppmp)
        self.assertIsNotNone(json_ppmp)

        self.assertEqual(json_ppmp['device']['id'], 'testid')
        self.assertEqual(json_ppmp['device']['additionalData']['hostname'], 'testdevice')

        self.assertEqual(len(json_ppmp['measurements'][0]['series']), 2)
        self.assertEqual(json_ppmp['measurements'][0]['series']['a'], ['aa'])


    def test_to_ppmp_combined(self):
        timestamp = local_now()
        variables = {
            'a': 'aa',
            'b': 'bbb',
            'c': 1234,
            'd': 0.2,
        }
        sv = SimpleVariables(variables, timestamp, "testdevice", "testid")
        ppmp = sv.to_PPMP()

        json_ppmp = json.loads(ppmp)
        self.assertIsNotNone(json_ppmp)

        self.assertEqual(json_ppmp['device']['id'], 'testid')
        self.assertEqual(json_ppmp['device']['additionalData']['hostname'], 'testdevice')

        self.assertEqual(len(json_ppmp['measurements'][0]['series']), 5)
        self.assertEqual(json_ppmp['measurements'][0]['series']['a'], ['aa'])


if __name__ == '__main__':
    unittest.main()

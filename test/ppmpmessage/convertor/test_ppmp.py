import unittest
from ppmpmessage.convertor.ppmp import PPMPObject

class TestPPMPObject(unittest.TestCase):

    def test_export_to_influxdb(self):
        # testdata
        json = '''{
            "content-spec": "urn:spec://eclipse.org/unide/measurement-message#v2",
            "device": {"deviceID": "99232"},
            "measurements": [{
                        "series": {
                                "$_time": [
                                            0,
                                            0,
                                            0,
                                            0,
                                            0
                                ],
                                "temperature": [
                                            10.114128726544047,
                                            1.8779273356050297,
                                            11.701677954589076,
                                            7.028277862631345,
                                            2.4205878756542565
                                ],
                                "pressure": [
                                            10.789956726544047,
                                            1.789956356050297,
                                            11.789595654589076,
                                            7.789956442631345,
                                            2.789956544442565
                                ]
                        },
                        "ts": "2002-05-30T09:30:10.123000+02:00"
            }]
        }'''
        ppmp = PPMPObject(json)
        data = ppmp.export_to_influxdb()

        #self.assertNotEqual(data, None)
        self.assertEqual(data[0]['fields']['temperature'], 10.114128726544047)
        self.assertEqual(data[0]['fields']['pressure'], 10.789956726544047)

        self.assertEqual(data[3]['fields']['temperature'], 7.028277862631345)
        self.assertEqual(data[3]['fields']['pressure'], 7.789956442631345)


if __name__ == '__main__':
    unittest.main()
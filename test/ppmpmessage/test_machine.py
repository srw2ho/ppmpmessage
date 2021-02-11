import unittest
import os
import sys
sys.path.append(os.getcwd())

from ppmpmessage.v3 import Machine

class TestPPMPObject(unittest.TestCase):

    def test_machine(self):
        msg = Machine("localhost")
        self.assertIsNotNone(msg)


if __name__ == '__main__':
    unittest.main()

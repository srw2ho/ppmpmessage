import socket
from uuid import uuid1
from getmac import get_mac_address
from ppmpmessage.v3.util import fletcher16


class Device(object):

    allowed_keys = ['mode', 'state', 'additionalData']
    map_keys = {
        '_id': 'id'
    }

    def __init__(self, net_name='mh', **kwargs):
        hostname = socket.gethostname()
        macaddress = get_mac_address(hostname=hostname)

        if macaddress==None:macaddress = get_mac_address()
        
        self.__macaddress = macaddress
        
        self._id = str(uuid1())
        self.__net_name = net_name
        # self.__net_id = str(fletcher16(hostname + get_mac_address(hostname=hostname) + kwargs['additionalData']['type']))
        self.__net_id = str(fletcher16(hostname + macaddress + kwargs['additionalData']['type']))
     
        for key, value in kwargs.items():
            if key in self.allowed_keys:
                setattr(self, key, value)
            else:
                raise Exception(f"{key} is not an allowed attribute name!")

        # set own hostname
        if not hasattr(self, 'additionalData'):
            self.additionalData = {}
        else:
              if not 'hostname' in self.additionalData:
                self.additionalData['hostname'] = hostname
    # set netId to fix string
    def setNetId(self, net_id):
        self.__net_id = net_id

    def sethostNameByNetId(self, net_id):
        hostname = self.additionalData['hostname']
        newhostname = f'{hostname}.{net_id}'
        self.additionalData['hostname'] = newhostname

    def __getstate__(self):
        odict = self.__dict__.copy()

        # create new dictionary entries for all maped variables and delete the old representations
        for k, v in self.map_keys.items():
            if k in odict:
                odict[v] = odict[k]
                del odict[k]

        # ignore variables that are prefixed by "__Device_" e.g. self.__ppmp_topic
        for key in list(odict):
            if '_Device__' in key:
                del odict[key]

        return odict

    def getHostname(self):
        return self.additionalData['hostname']

    def getMacaddress(self):
        return self.__macaddress

    def info_topic(self, net_id=None):
        """ Returns the device's info topic

        Returns:
            [str] -- MQTT topic to retrieve device info
        """
        if net_id is None:
            return f'{self.__net_name}/{self.__net_id}/info'
        else:
            return f'{self.__net_name}/{net_id}/info'

    def ppmp_topic(self, net_id=None):
        """ Returns the device's ppmp topic

        Returns:
            [str] -- MQTT topic to retrieve device measurement messages
        """
        if net_id is None:
            return f'{self.__net_name}/{self.__net_id}/ppmp'
        else:
            return f'{self.__net_name}/{net_id}/ppmp'

        # return f'{self.__net_name}/{self.__net_id}/ppmp'
    def control_set_topic(self, net_id=None):
        """ Returns the device's control set topic

        Returns:
            [str] -- MQTT topic to trigger commands on the device
        """
        if net_id is None:
            return f'{self.__net_name}/{self.__net_id}/control/set'
        else:
            return f'{self.__net_name}/{net_id}/control/set'

    def control_topic(self, net_id=None):
        """ Returns the device's control topic

        Returns:
            [str] -- MQTT topic to retrieve commands responses on the device
        """
        if net_id is None:
            return f'{self.__net_name}/{self.__net_id}/control'
        else:
            return f'{self.__net_name}/{net_id}/control'


class iotHubDevice(Device):

    def __init__(self, net_name='mh', devideid= '', **kwargs):
        
        super().__init__(net_name='mh', **kwargs)
       
        if devideid=='':  self._id = str(uuid1())
        else:  
            self._id = str(devideid)
            newhostname =self.additionalData['hostname'] +"." + self._id 
            self.additionalData['hostname'] = newhostname

        self.__net_id = str(fletcher16(self.additionalData['hostname'] + self.getMacaddress() + kwargs['additionalData']['type']))


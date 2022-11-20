from pydantic import BaseModel
from typing import Union
import yaml

import serial

from port import Port

#from asyncio.timeouts import timeout

from datatype import Commands, LSMParams, Address

class LSM:
    def __init__(self):
        self.port = Port()
        with open(".\config\command.yml", 'r',  encoding='utf8') as file_yml:
            command_ = yaml.safe_load(file_yml)
        self.commands = Commands(**command_)

        with open(".\config\params.yml", 'r',  encoding='utf8') as file_yml:
            params_ = yaml.safe_load(file_yml)
            print(params_)
        self.params = LSMParams(**params_)

        with open(".\config\address.yml", 'r',  encoding='utf8') as file_yml:
            address_ = yaml.safe_load(file_yml)
            print(address_)
        self.address = Address(**address_)

    def initUsbPort(self, params):
        return self.port.init_param(params["usb_baudrate"], params["usb_port"])

    def checkModem(self):
        for i in range(3):
            res = self.port.send_command('ATD', {})
            if (res is not None) and (res.get('str', '') == '0D0A4F4B0D0A'):
                return True
        return False       

    def ComLinkRequest(self, params):
        if self.checkModem(self):
            for i in range(3):
                res = self.port.send_command('link_request', {})
                if res is not None:
                    return True, {}

    def getShortStatus(self, params):
        if self.checkModem(self):
            res = self.port.send_command('short_status', params)
            if res is not None:
                return True, res
        return False, None

    def ComGeneralStatus(self, params):
        if self.checkModem(self):
            for i in range(3):
                res = self.port.send_command('general_status', params)
                if res is not None:
                    return True, res
        return False, None

    def ComFullStatus(self, params):
        if self.checkModem(self):
            for i in range(3):
                res = self.port.send_command('full_status', params)
                if res is not None:
                    return True, res
        return False, None

    def ComSetModeLSM(self, params):
        if self.checkModem(self):
            for i in range(3):
                res = self.port.send_command('set_setting', params)
                if res is not None:
                    return True, res
        return False, None

    def ComSetModemSetting(self, params):
        if self.checkModem(self):
            for i in range(3):
                res = self.port.send_command('set_modem_setting', params)
                if res is not None:
                    return True, res
        return False, None

    def getEvent(self, params):
        if self.checkModem(self):
            for i in range(3):
                res = self.port.send_command('set_factory_setting', params)
                if res is not None:
                    return True, res
        return False, None






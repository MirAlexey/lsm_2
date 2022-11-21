from pydantic import BaseModel
from typing import Union
import yaml

import serial
from lsm_dev.datatype import Commands, LSMParams, Addresses
from lsm_dev.port import Port

#from asyncio.timeouts import timeout



class LSM:
    def __init__(self, data_carrier):
        self.data_carrier = data_carrier
        print('-----------------------------------')
        with open(".\\config\\command.yml", 'r',  encoding='utf8') as file_yml:
            command_ = yaml.safe_load(file_yml)
        self.commands = Commands(**command_)
        
        #print(self.commands)
        with open(".\\config\\params.yml", 'r',  encoding='utf8') as file_yml:
            params_ = yaml.safe_load(file_yml)
        params = LSMParams(**params_)
        self.params =params.params
        self.setting_modem =params.setting_modem
        #print(self.params)
        with open(".\\config\\address.yml", 'r',  encoding='utf8') as file_yml:
            address_ = yaml.safe_load(file_yml)
        self.address = Addresses(**address_)
        #print(self.params)
        self.port = Port(self.commands, self.address,  self.params)

    def initUsbPort(self):
        params = self.data_carrier.getParam() 
        print(params)
        return self.port.init_param(params["usb_size_data"], params["usb_port"])

    def checkModem(self):
        #print(self.commands)
        params = self.data_carrier.getParam()
        for i in range(3):
            res = self.port.send_command('', 'ATD', {})
            print('res!', res, res.get('str', '')[0], res.get('str', '')[0] == '0d0a4f4b0d0a',  (res is not None) and (res.get('str', '')[0] == '0d0a4f4b0d0a'))
            if (res is not None) and (res.get('str', '')[0] == '0d0a4f4b0d0a'):
                return True
        return False       

    def ComLinkRequest(self):
        if self.checkModem(self):
            for i in range(3):
                res = self.port.send_command('link_request', {})
                if res is not None:
                    return True, {}
        return False  

    def getShortStatus(self):
        params = self.data_carrier.getParam()
        if self.checkModem(self):
            res = self.port.send_command('short_status', params)
            if res is not None:
                return True, res
        return False, None

    def ComGeneralStatus(self):
        params = self.data_carrier.getParam()
        if self.checkModem(self):
            for i in range(3):
                res = self.port.send_command('general_status', params)
                if res is not None:
                    return True, res
        return False, None

    def ComFullStatus(self):
        params = self.data_carrier.getParam()
        if self.checkModem(self):
            for i in range(3):
                res = self.port.send_command('full_status', params)
                if res is not None:
                    return True, res
        return False, None

    def ComSetModeLSM(self):
        params = self.data_carrier.getParam()
        if self.checkModem(self):
            for i in range(3):
                res = self.port.send_command('set_setting', params)
                if res is not None:
                    return True, res
        return False, None

    def ComSetModemSetting(self):
        params = self.data_carrier.getParam()
        if self.checkModem(self):
            for i in range(3):
                res = self.port.send_command('set_modem_setting', params)
                if res is not None:
                    return True, res
        return False, None

    def getEvent(self):
        params = self.data_carrier.getParam()
        if self.checkModem(self):
            for i in range(3):
                res = self.port.send_command('set_factory_setting', params)
                if res is not None:
                    return True, res
        return False, None





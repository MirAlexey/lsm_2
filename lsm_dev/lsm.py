from pydantic import BaseModel
from typing import Union
import yaml

import serial

#from asyncio.timeouts import timeout

CONST_SRC = [
    '00', '31', '62', '53', 'C4', 'F5', 'A6', '97',
    'B9', '88', 'DB', 'EA', '7D', '4C', '1F', '2E',
    '43', '72', '21', '10', '87', 'B6', 'E5', 'D4',
    'FA', 'CB', '98', 'A9', '3E', '0F', '5C', '6D',
    '86', 'B7', 'E4', 'D5', '42', '73', '20', '11',
    '3F', '0E', '5D', '6C', 'FB', 'CA', '99', 'A8',
    'C5', 'F4', 'A7', '96', '01', '30', '63', '52',
    '7C', '4D', '1E', '2F', 'B8', '89', 'DA', 'EB',
    '3D', '0C', '5F', '6E', 'F9', 'C8', '9B', 'AA',
    '84', 'B5', 'E6', 'D7', '40', '71', '22', '13',
    '7E', '4F', '1C', '2D', 'BA', '8B', 'D8', 'E9',
    'C7', 'F6', 'A5', '94', '03', '32', '61', '50',
    'BB', '8A', 'D9', 'E8', '7F', '4E', '1D', '2C',
    '02', '33', '60', '51', 'C6', 'F7', 'A4', '95',
    'F8', 'C9', '9A', 'AB', '3C', '0D', '5E', '6F',
    '41', '70', '23', '12', '85', 'B4', 'E7', 'D6',
    '7A', '4B', '18', '29', 'BE', '8F', 'DC', 'ED',
    'C3', 'F2', 'A1', '90', '07', '36', '65', '54',
    '39', '08', '5B', '6A', 'FD', 'CC', '9F', 'AE',
    '80', 'B1', 'E2', 'D3', '44', '75', '26', '17',
    'FC', 'CD', '9E', 'AF', '38', '09', '5A', '6B',
    '45', '74', '27', '16', '81', 'B0', 'E3', 'D2',
    'BF', '8E', 'DD', 'EC', '7B', '4A', '19', '28',
    '06', '37', '64', '55', 'C2', 'F3', 'A0', '91',
    '47', '76', '25', '14', '83', 'B2', 'E1', 'D0',
    'FE', 'CF', '9C', 'AD', '3A', '0B', '58', '69',
    '04', '35', '66', '57', 'C0', 'F1', 'A2', '93',
    'BD', '8C', 'DF', 'EE', '79', '48', '1B', '2A',
    'C1', 'F0', 'A3', '92', '05', '34', '67', '56',
    '78', '49', '1A', '2B', 'BC', '8D', 'DE', 'EF',
    '82', 'B3', 'E0', 'D1', '46', '77', '24', '15',
    '3B', '0A', '59', '68', 'FF', 'CE', '9D', 'AC'
]


class Port:
    def __init__(self, commands):
        self.commands = commands
        pass
    def set_param(self, baudrate, port):
        self.usb = serial.Serial()
        self.usb.baudrate = baudrate
        self.usb.port = port
        self.usb.open()
        res = self.usb.is_open
        self.usb.close()
        return res

    def send_command(self, command, params):
        str_command, time_out, len_response = self._build_command(command, params)
        return self._write_and_read(str_command, time_out, len_response)

    def _write_and_read(self, str_command, time_out, len_response):
        self.usb.open()
        self.usb.write(str_command)
        res = self.usb.read(size=len_response, timeout=time_out)
        self.usb.close()
        return res
        
class SimpleCom(BaseModel):
    name: str
    desc: str
    query: str
    response: str 

class ValuesStepListParam(BaseModel):
    start: float
    end: float
    step: float

class KeysStepListParam(BaseModel):
    start: float
    end: float
    step: float
    name: str

class SimpleCommands(BaseModel):
    commands: list[SimpleCom]

class ListParam(BaseModel):
    keys: list[str]
    values: list[int]

class StepListParam(BaseModel):
    keys: KeysStepListParam
    values: ValuesStepListParam

class Params(BaseModel):
    name: str
    type: str
    param: Union[ListParam, StepListParam]

class BaseParams(BaseModel):
    params: list[Params]

class Address(BaseModel):
    input: str
    output: str

class Addresses(BaseModel):
    addresses: dict[str, Address]


class LSM:
    def __init__(self):
        self.port = Port()
        with open(".\config\simple_command.yml", 'r',  encoding='utf8') as file_yml:
            command_ = yaml.safe_load(file_yml)
            
        self.commands = SimpleCommands(**command_)

        with open(".\config\params.yml", 'r',  encoding='utf8') as file_yml:
            params_ = yaml.safe_load(file_yml)
            print(params_)
        self.params = BaseParams(**params_)

        with open(".\config\\address.yml", 'r',  encoding='utf8') as file_yml:
            address_ = yaml.safe_load(file_yml)
            print(address_)
        #self.address = Address(**address_)


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


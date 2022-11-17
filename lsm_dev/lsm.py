from pydantic import BaseModel
from typing import Union
import yaml

import serial

from port import Port

#from asyncio.timeouts import timeout

class ValData(BaseModel):
    type: str
    values: list[str]

class ValuesData(BaseModel):
    values: list[ValData]

class Query(BaseModel):
    command: str
    address: bool
    data: ValuesData
    crc: bool

class Command(BaseModel):
    name: str
    desc: str
    request: Query
    response: Query
    timeout: int

class Commands(BaseModel):
    commands: list[Command]



class ValuesStepListSetting(BaseModel):
    start: float
    end: float
    step: float

class KeysStepListSetting(BaseModel):
    start: float
    end: float
    step: float
    name: str

class ListSetting(BaseModel):
    keys: list[str]
    values: list[int]

class StepListSetting(BaseModel):
    keys: KeysStepListSetting
    values: ValuesStepListSetting

class SettingModem(BaseModel):
    name: str
    type: str
    param: Union[ListSetting, StepListSetting]

class ParamValue(BaseModel):
    name: str
    mask: int
    shift: int
    mul: int

class ParamsValues(BaseModel):
    name: str
    type: str
    params: list[ParamValue]

class Params(BaseModel):
    name: str
    type: str
    values: list[ParamsValues]
class LSMParams(BaseModel):
    setting_modem: list[SettingModem]
    params: list[Params]

class Address(BaseModel):
    input: str
    output: str

class Addresses(BaseModel):
    addresses: dict[str, Address]


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


from pydantic import BaseModel
from typing import Union
import yaml

import serial

#from asyncio.timeouts import timeout




        
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


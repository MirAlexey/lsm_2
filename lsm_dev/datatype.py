from pydantic import BaseModel
from typing import Union

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


class ParamsValues(BaseModel):
    name: str
    type: str
    number: int
    name: str
    mask: int
    shift: int
    mul: int

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

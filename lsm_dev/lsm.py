from pydantic import BaseModel
from typing import Union
import yaml

import serial
from lsm_dev.datatype import Commands, LSMParams, Addresses
from lsm_dev.port import Port
from lsm_dev.logger import Logger

#from asyncio.timeouts import timeout


logger = Logger()
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
        self.disp_modem_status = False
        self.hex_modem_status = False
        self.current_address = None

    def initUsbPort(self):
        if self.disp_modem_status:
            return True, None
        params = self.data_carrier.getParam() 
        self.disp_modem_status = self.port.init_param(params["usb_speed"], params["usb_port"], 5)
        return self.disp_modem_status, None

    def checkModem(self):
        #print(self.commands)
        if self.hex_modem_status:
            return True, None
        params = self.data_carrier.getParam()
        for i in range(3):
            res = self.port.send_command('', 'ATD', {})
            if (res is not None) and (res.get('str',  ['']) == '4f4b0d0a'):
                self.hex_modem_status = True
                logger.info(f"Модем диспетчера в работе")
                return True, None
        logger.warn(f"Модем диспетчера не отвечает")
        return False, None      

    def ComLinkRequest(self, dest):
        self.current_address = None
        if not self.disp_modem_status:
            res, prm = self.initUsbPort()
            if not res:
                logger.warn('нет связи с модемом диспетчером по USB')
                return False, {'link_mc1' if dest == 'k1' else 'link_mc2': 'Связь отсутствует'} 
        if not self.hex_modem_status:
            res, prm = self.checkModem()
            if not res:
                logger.warn('Запрос канала связи неуспешен, нет связи с модемом диспетчером')
                return False, {'link_mc1' if dest == 'k1' else 'link_mc2': 'Связь отсутствует'}
        count_run = 2
        for i in range(count_run):
            res = self.port.send_command(dest, 'link_request', {})
            if res is not None:
                logger.info(f"Запрос каннала связи с модемом {'МС-1' if dest == 'k1' else 'МС-2'} успешен")
                self.current_address = dest
                return True, {'link_mc1' if dest == 'k1' else 'link_mc2':'Связь установлена' if res is None else 'Связь отсутствует'}
            logger.atn(f'Запрос {i} из {count_run}  канала связи с модемом неуспешен')
        logger.warn('Запрос канала связи неуспешен, нет связи с модемом диспетчером')
        return False, {'link_mc1' if dest == 'k1' else 'link_mc2': 'Связь отсутствует'}

    def _ParamComLsm(self, com_name, count_run):
        logger.info(f'Отправка команды {com_name}')
        params = self.data_carrier.getParam()
        if self.current_address is not None:
            for i in range(count_run):
                res = self.port.send_command(self.current_address, com_name , {})
                if res is not None:
                    logger.info(f'Команда {com_name} прошла ')
                    return True, res
                logger.atn(f'Команда {com_name} не прошла (попытка {i} из {count_run})')
            logger.warn(f'Команда {com_name} не прошла')
        else:
            logger.warn('Нет канала связи')
        return False, None

    def ComShortStatus(self):
        return self._ParamComLsm('short_status', 3)

    def ComGeneralStatus(self):
        return self._ParamComLsm('general_status', 3)

    def ComFullStatus(self):
        return self._ParamComLsm('full_status', 3)

    def ComSetModeLSM(self):
        return self._ParamComLsm('set_setting', 3)

    def ComSetModemSetting(self):
        return self._ParamComLsm('set_modem_setting', 3)

    def _ShortComLsm(self, com_name, count_run):
        logger.info(f'Отправка команды {com_name}')
        if self.current_address is not None:
            for i in range(count_run):
                res = self.port.send_command(self.current_address, com_name , {})
                if res is not None:
                    logger.info(f'Команда {com_name} прошла ')
                    return True, res
                logger.atn(f'Команда {com_name} не прошла (попытка {i} из {count_run})')
            logger.warn(f'Команда {com_name} не прошла')
        else:
            logger.warn('Нет канала связи')
        return False, None

    def ComStartLsm(self):
        return self._ShortComLsm('start', 3)

    def ComStopLsm(self):
        return self._ShortComLsm('stop', 3)

    def ComResetLsm(self):
        return self._ShortComLsm('reset_setting', 3)

    def ComHardResetLsm(self):
        return self._ShortComLsm('set_factory_setting', 3)

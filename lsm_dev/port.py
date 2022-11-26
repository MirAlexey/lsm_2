import serial

from lsm_dev.param_lsm import get_param_obj, get_param_reduce
from lsm_dev.logger import Logger

import time

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

logger = Logger() 

class Port:
    def __init__(self, commands, addresses, params):
        self._commands = commands.commands
        self._addresses = addresses.addresses
        self.params = params
        #print('f', [p for p in params])
        self._param_name= [p.name for p in params]
        #print('f',self.params)
        self._command_name = [com.name for com in self._commands]

    def init_param(self, baudrate, port, timeout):
        self.usb = serial.Serial()
        self.usb.baudrate = baudrate
        self.usb.port = port
        self.usb.timeout=timeout
        self.usb.open()
        res = self.usb.is_open
        return res

    def is_open(self):
        return self.usb.is_open()

    def checkEventMsg(self):
        pass

    def _get_command(self, name):
        return self._commands[self._command_name.index(name)]

    def send_command(self, address, command_name, params_value, postfix_param_name = ''):
        command = self._get_command(command_name)
        str_command, time_out, len_response = self._build_command(address, command, params_value, postfix_param_name)
        #res = self._write_and_read_test(str_command, time_out, len_response)
        res = self._write_and_read(str_command, time_out, len_response)
        res_str = [f'{r:0>2x}' for r in res ]
        #print(len_response)
        if len(res) != len_response:
            logger.warn(f'Ответ {res_str} неверной длины')
            return None
        if command.response.crc and (not self._check_crc(res)):
            logger.warn(f"Ответ {res_str} с неверным crc, получено '{self._get_crc(''.join(res_str[:-1]))}'")
            return None
        
        return self._parse_response(res, address, command)

    def _write_and_read_test(self, str_command, time_out, len_response):
        logger.log(f'Write: {str_command}')
        res = ''
        if str_command == '4154440d':
            res = bytearray.fromhex('4f4b0d0a')
        elif str_command == '5600bd':
            res = bytearray.fromhex('658058') 
        elif str_command == '4600d3':
            res = bytearray.fromhex('6480ac') 
        elif str_command == '4601e2':
            res = bytearray.fromhex('64810001180b15020d0505390f0f0f0f53')
        elif str_command == '460744':
            res = bytearray.fromhex('64873b')
        elif str_command == '46086a':
            res = bytearray.fromhex('648815')
        elif str_command == '460675':
            res = bytearray.fromhex('64860a')
        elif str_command == '460526':
            res = bytearray.fromhex('648559')
        else:
            res = bytearray.fromhex('a346f6d3')

        logger.log('Read: ' + ''.join([f'{r:0>2x}' for r in res ]))

        return res

    def _write_and_read(self, str_command, time_out, len_response):
        #print(self, str_command, time_out, len_response)
        logger.log(f'Отправка: {str_command}')
        self.usb.write(bytearray.fromhex(str_command))
        res = self.usb.read(size=len_response)
        logger.log('Прием: ' + ''.join([f'{r:0>2x}' for r in res ]))
        return res

    def _build_command(self, address, command, params_value, postfix_param_name):
        #print(command)
        req = command.request
        resp = command.response
        time_out = command.timeout

        resp_len = len(resp.data.values)
        resp_len += 1 if resp.address else 0
        resp_len += 1 if resp.command !='' else 0
        resp_len += 1 if resp.crc else 0

        str_command=''
        if req.address:
            str_command+=self._get_address(address, 'input')
        str_command+=req.command 
        str_command+=self._get_data(req.data, params_value, address, postfix_param_name)
        if req.crc:
            str_command+=self._get_crc(str_command)
        return str_command, time_out, resp_len

    def _get_address(self, address, dest):
        if address in self._addresses:
            return self._addresses[address].dict()[dest]

    def _get_data(self, data, params_value, address, postfix_param_name):
        res = ''
        for com_v in data.values:
            params_v = self._get_param_setting(com_v)
            values_v = self._get_param_value(com_v, address, params_value, postfix_param_name)
            rv= 0b00000000
            #print(params_v)
            #print(values_v)
            for pv, vv in zip(params_v, values_v):
                rv |= get_param_obj(pv['type']).encode(pv['params'],vv)
            res+=f'{rv:0>2x}'
        return res

    def _get_param_setting(self, com_val):
        res = []
        #print(com_val)
        #for v in com_val.values:
        v = com_val
        #print(v)
        p_a = v.type.split('__')
        for p in v.values:
            l_a = p.split('__')
            #print(p_a,l_a,p_a[0])
            #print(self._param_name)
            #print(self.params[self._param_name.index(p_a[0])])
            if p_a[0] == 'str':
                cur_res = {'type':'str','params':[], 'type_reduce':'value_con'}
            else:
                param_lsm_values = self.params[self._param_name.index(p_a[0])]
                pv_name = [pv.name for pv in param_lsm_values.values]
                #print(param_lsm_values)
                cur_res = param_lsm_values.values[pv_name.index(l_a[0])]
                #print(cur_res, cur_res.dict())
                cur_res = cur_res.dict()
                cur_res['type_reduce'] = param_lsm_values.type
            res.append(cur_res)
        return res

    def _get_param_value(self, val, address, params_value, postfix_param_name):
        res = []
        #for v in val.values:
        v = val
        for p in v.values:
            source = self._get_current_dest(v.type, p)
            res.append(p if source == 'str' else params_value[source])
        return res

    def _parse_response(self, res, address, command):
        resp = command.response
        resp_address = f'{res[0]:0>2x}' if resp.address else ''
        true_address = self._get_address(address, 'output') if resp.address else ''
        resp_command = f'{res[1]:0>2x}' if resp.command != '' else ''
        true_command = resp.command
        if (resp_address != true_address):
            logger.error(f"Ответ неверный! адрес в ответе неверный '{resp_address}' != '{true_address}'")
            return None
        if (resp_address != true_address) or (resp_command != true_command):     
            logger.error(f"Ответ неверный!  команда в ответе неверная'{resp_command} != '{true_command}'")
            return None
        start_data = int(resp.address) + int(resp.command != '')
        #print('r', resp)
        resp_data = res[start_data:-1] if resp.crc else res[start_data:]
        #print('len', len(resp.data.values), len(resp_data))
        res = {}
        for i,v in enumerate(resp.data.values):
            #print('vvv', v)
            group_values = v.values
            params_v = self._get_param_setting(v)
            values_v = resp_data[i]
            for pv, gv in zip(params_v, group_values):
                cur_dest = self._get_current_dest(v.type, gv, True)
                if cur_dest not in res:
                    res[cur_dest] = {'type_reduce': pv['type_reduce'], 'vl':[]}
                decode_value = get_param_obj(pv['type']).decode(pv['params'], values_v)
                res[cur_dest]['vl'].append(decode_value)
        for k,v in res.items():
            res[k]= get_param_reduce(v['type_reduce']).eval(v['vl'])[0]
        return res 


    def _get_current_dest(self, group_param, group_value, is_full = False):
        group_dev = group_param.split('__')
        value_dev = group_value.split('__')
        if len(value_dev) > 1:
            return group_value if is_full else value_dev[0]
        return group_param if is_full else group_dev[0]


    def _get_crc(self, src_str):
        crc = 0x00
        res=bytearray.fromhex(src_str)
        for r in res:
            crc = int(CONST_SRC[crc ^ r], 16)
        return f'{crc:0>2x}'

    def _check_crc(self,res):
        crc = 0x00
        for r in res[:-1]:
            crc = int(CONST_SRC[crc ^ r], 16)
        return crc == res[-1]




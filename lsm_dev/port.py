import serial

from param_lsm import get_param_obj
from logger import Logger

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
        self._commands = commands
        self._addresses = addresses
        self.params = params
        self._param_name= [p.name for p in params]

    def set_param(self, baudrate, port):
        self.usb = serial.Serial()
        self.usb.baudrate = baudrate
        self.usb.port = port
        self.usb.open()
        res = self.usb.is_open
        self.usb.close()
        return res

    def send_command(self, address, command, params_value):
        str_command, time_out, len_response = self._build_command(address, command, params_value)
        res = self._write_and_read(str_command, time_out, len_response)
        if len(res) != len_response:
            logger.warn(f'Response {res} with invalid length')
            return None
        if ~self._check_crc(res):
            logger.warn(f'Response {res} with error crc')
            return None
        
        return self._parse_response(res, address, command)
        

    def _write_and_read(self, str_command, time_out, len_response):
        
        self.usb.open()
        self.usb.write(bytearray.fromhex(str_command))
        res = self.usb.read(size=len_response, timeout=time_out)
        self.usb.close()
        return res

    def _build_command(self, address, command, params_value):
        req = command['request']
        resp = command['response']
        time_out = command['timeout']

        resp_len = len(resp['data']['values'])
        resp_len += 1 if resp['address'] else 0
        resp_len += 1 if resp['address']!='' else 0
        resp_len += 1 if resp['crc'] else 0

        str_command=''
        if req['address']:
            str_command+=self._get_address(address, 'output')
        str_command+=req['command'] 
        str_command+=self._get_data(req['data'], params_value, address)
        if req['crc']:
            str_command+=self._get_crc(str_command)
        return str_command, time_out, resp_len

    def _get_address(self, address, dest):
        if address in self._addresses:
            return self._addresses[address][dest]

    def _get_data(self, data, params_value, address):
        res = ''
        for v in data['values']:
            params_v = self._get_param_setting(v)
            values_v = self._get_param_value(v, address, params_value)
            rv= 0b00000000
            for pv, vv in zip(params_v, values_v):
                rv |= get_param_obj(pv).encode(vv)
            res+=f'{rv:0>2x}'
        return res

    def _get_param_setting(self, val):
        res = []
        for v in val['values']:
            for p in v['values']:
                l_a = p['values'].split('__')
                res.append(self.params[v['type'][l_a[0]]])
        return res

    def _get_param_value(self, val, address, params_value):
        res = []

        for v in val['values']:
            for p in v['values']:
                l_a = p['values'].split('__')
                tmp = params_value  if address == '' else params_value[address]                
                for a in l_a[::-1]:
                    tmp=tmp[a] 
                res.append(tmp)
        return res

    def _parse_response(self, res, address, command):
        resp = command['response']
        resp_address = f'{res[0]:0>2x}' if resp.address else ''
        true_address = self._get_address(address, 'input') if resp.address else ''
        resp_command = f'{res[1]:0>2x}' if resp.command != '' else ''
        true_command = resp.command
        if (resp_address != true_address) or (resp_command != true_command):
            raise ValueError(f"Response invalid! address: '{resp_address}' != '{true_address}' or command {resp_command} != '{true_command}'")
        start_data = int(resp.address) + (resp.command != '')
        resp_data = resp[start_data:-1]
        







    def _check_crc(self,res):
        crc = 0x00;
        for r in res[:-1]:
            crc = int(CONST_SRC[crc ^ r], 16)
        return crc == res[-1]




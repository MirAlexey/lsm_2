class ParamLSM:
    def __init__(self):
        pass

    def encode(self, params, data):
        pass

    def decode(self, params, data):
        pass

class Param_bit(ParamLSM):
    def decode(self, params, data):
        return sum([((data & res['mask']) >> res['shift']) * res['mul'] for res in params])

    def encode(self, params, data):
        res = 0b00000000
        for p in params:
            res |= (int(data//p['mul']) << p['shift']) & p['mask']
        return res

class Param_bool(ParamLSM):
    def decode(self, params, data):
        return bool((data & params[0]['mask']) >> params[0]['shift'])

    def encode(self, params, data):
        return (int(data) << params[0]['shift'])

class Param_sig(ParamLSM):
    def decode(self, params, data):
        return data-256 if data>127 else data

    def encode(self, params, data):
        return data+256 if data<0 else data

class Param_str(ParamLSM):
    def decode(self, params, data):
        return f'{data:0>2x}'

    def encode(self, params, data):
        return int(data, 16)


def get_param_obj(name):
    if name == 'bit_value':
        return Param_bit()
    elif name == 'bool_value':
        return Param_bool()
    elif name == 'sig_value':
        return Param_sig()
    elif name == 'str':
        return Param_str()
    else:
        raise ValueError(f'Name param: "{name}" is not valid')


class BaseReduce():
    def __init__(self, delim=''):
        self.delim=delim
    def eval(self, list_value):
        return list_value

class SumReduce(BaseReduce):
    def eval(self, list_value):
        return [sum(list_value)]

class ConStrReduce(BaseReduce):
    def eval(self, list_value):
        return [self.delim.join(list_value)]

class ConHexReduce(BaseReduce):
    def eval(self, list_value):
        return [self.delim.join([f'{v:0>2x}' for v in list_value])]

class ConDecReduce(BaseReduce):
    def eval(self, list_value):
        return [self.delim.join([f'{v:0>2}' for v in list_value])]

def get_param_reduce(name):
    if name == 'value':
        return BaseReduce()
    elif name == 'value_sum':
        return SumReduce()
    elif name == 'value_date':
        return ConDecReduce('-')
    elif name == 'value_time':
        return ConDecReduce(':')
    elif name == 'value_con':
        return ConStrReduce()
    else:
        raise ValueError(f'Name reduce: "{name}" is not valid')
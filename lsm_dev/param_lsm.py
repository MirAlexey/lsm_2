class ParamLSM:
    def __init__(self):
        pass

    def encode(self, type_value, name_value, all_params, value):
        pass

    def decode(self, type_value, name_value, all_params, value):
        pass

class Param_date(ParamLSM):
    def decode(self, type_value, name_value, all_params):
        value = all_params[type_value][name_value]
        if type_value == 'year':
           result = ((value & 0b11110000) >> 4)*10 + (value & 0b00001111)
        elif type_value == 'month':
           result = ((value & 0b00010000) >> 4)*10 + (value & 0b00001111)
        elif type_value == 'number':
           result = (value & 0b00000111)
        elif type_value == 'weeks_day':
           result = ((value & 0b11110000) >> 4)*10 + (value & 0b00001111)
        else:
            raise ValueError(f'type_value "{type_value}" not valid for date')
        return result

    def encode(self, type_value, name_value, all_params, value):
        return ((value//10 ) << 4) + (value%10)

class Param_time(ParamLSM):
    def decode(self, type_value, name_value, all_params):
        value = all_params[type_value][name_value]
        if type_value == 'hour':
           result = ((value & 0b00110000) >> 4)*10 + (value & 0b00001111)
        elif type_value == 'min':
           result = ((value & 0b01110000) >> 4)*10 + (value & 0b00001111)
        elif type_value == 'sec':
           result = ((value & 0b01110000) >> 4)*10 + (value & 0b00001111)
        else:
           raise ValueError(f'type_value "{type_value}" not valid for time')
        return result

    def encode(self, type_value, name_value, all_params, value):
        return ((value//10 ) << 4) + (value%10)

class Param_mode(ParamLSM):
    def decode(self, type_value, name_value, all_params):
        value = all_params[type_value][name_value]
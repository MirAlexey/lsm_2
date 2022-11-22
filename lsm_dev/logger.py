import time

class bcolors:
    RED = '\033[91m'
    GRAY = '\033[90m'
    BLUE = '\033[95m'
    GREEN ='\033[92m' 
    YELLOW ='\033[93m' 
    RESET = '\033[0m'


class Logger():
    def __init__(self, log_filename='log.txt'):
        self.log_fn=log_filename

    def _write_log(self, msg, color, type_msg ):
        tm = time.asctime()
        msg = tm + ' ' + color + type_msg + ": "+ msg + bcolors.RESET
        print(msg)
        with open(self.log_fn, 'a', encoding='utf8') as f:
            f.write(msg+'\n')

    def info(self, msg):
        self._write_log(msg, bcolors.GREEN , 'INFO')

    def log(self, msg):
        self._write_log(msg, bcolors.GRAY, 'LOG')

    def warn(self, msg):
        self._write_log(msg, bcolors.YELLOW , "WARNING")

    def atn(self, msg):
        self._write_log(msg, bcolors.BLUE , "ATTENTION")

    def error(self, msg):
        self._write_log(msg, bcolors.RED + "ERROR")

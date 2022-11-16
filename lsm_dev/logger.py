import time

class bcolors:
    RED = '\033[91m'
    GREEN ='\033[92m' 
    YELLOW ='\033[93m' 
    RESET = '\033[0m'


class Logger():
    def __init__(self, log_filename='log.txt'):
        self.log_fn=log_filename

    def _write_log(self, msg):
        print(msg)
        with open(self.log_fn, 'a') as f:
            f.write(msg)

    def info(self, msg):
        self._write_log(time.asctime() + bcolors.GREEN + "INFO: "+ msg + bcolors.RESET)

    def warn(self, msg):
        self._write_log(time.asctime() + bcolors.YELLOW + "INFO: "+ msg + bcolors.RESET)

    def error(self, msg):
        self._write_log(time.asctime() + bcolors.RED + "INFO: "+ msg + bcolors.RESET)

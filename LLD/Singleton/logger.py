from datetime import datetime
from singleton import Singleton


class Logger(Singleton):
    log_file = None
    def __init__(self, path) -> None:
        if None is self.log_file:
            self.log_file = open(path, mode="w")
        
    def write_log(self, text):
        now = str(datetime.now())
        record = f"{now} : {text}\n" 
        self.log_file.write(record)
    
    def close_log(self):
        self.log_file.close()
        self.log_file = None
        
from logger import Logger


logger1 = Logger("mylog.log")

logger1.write_log("Logger1 first log")

logger2 = Logger("newlog.log")

logger2.write_log("Logger2 first log")

print(logger1 is logger2)

logger1.write_log("Logger1 second log")

logger1.close_log()


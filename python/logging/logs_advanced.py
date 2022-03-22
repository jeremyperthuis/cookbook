import logging
import logging.config

logging.config.fileConfig('logging.conf')
logger1= logging.getLogger('module1')
logger2= logging.getLogger('module2')

def module1():
    logger1.info("test")

def module2():
    logger2.info("test")



module1()
module2()
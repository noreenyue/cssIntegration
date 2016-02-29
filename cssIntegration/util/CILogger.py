#-*- coding: utf-8 -*
import logging

def getLogger(logfile):         
    logger = logging.getLogger()
    hdlr = logging.FileHandler(logfile)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s\n')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.NOTSET)
    return  logger
        

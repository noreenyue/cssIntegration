#-*- coding: utf-8 -*
import logging
import os

def getLogger(logfile):         
    dirpath = os.path.split(logfile)[0]
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)
        
    logger = logging.getLogger()
    hdlr = logging.FileHandler(logfile)
    formatter = logging.Formatter('[%(asctime)s %(levelname)s] %(message)s\n')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.NOTSET)
    return  logger
        

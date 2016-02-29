#-*- coding: utf-8 -*


import os
from util import CILogger
CURR_PATH = os.path.abspath(os.path.dirname(__file__)) 
SRC_PATH = os.path.join(CURR_PATH, '../css-src/nt')
LOG_PATH = os.path.join(CURR_PATH, '../log/manager.log')
logger = CILogger.getLogger(LOG_PATH)

def rootDirHandler(rootpath):
    for parent, dirs, files in os.walk(rootpath):
        if parent != SRC_PATH: # sub dir
            continue
        
        for filename in files:
            filepath = os.path.join(SRC_PATH, filename)
            names = os.path.splitext(filepath)
            if names[1] == ".css":
                fileHandler( filepath)
        
def fileHandler(abspath):
    try:
        fh = open(abspath)
        for  line in  fh.readlines(): 
            print  line
    except Exception as e:
        logger.exception(e)

rootDirHandler(SRC_PATH)
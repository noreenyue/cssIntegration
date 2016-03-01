#-*- coding: utf-8 -*


import os
CURR_PATH = os.path.dirname(__file__)
SRC_PATH = os.path.abspath(os.path.join(CURR_PATH, '..', 'css-src/nt'))
LOG_PATH = os.path.abspath(os.path.join(CURR_PATH, '..', 'log/manager.log'))

import time

from util import CILogger, CIUtil
from util.CIConst import Constants
logger = CILogger.getLogger(LOG_PATH)

def compactLine(text):
    text =  CIUtil.lineRemoveNotes(text)
    return CIUtil.lineRemoveSpace(text)

'''
紧凑文件
'''
def compactFiles(subFilePath):
    reName = subFilePath + "_bk"
    fh = open(subFilePath, 'r+')
    lines = fh.readlines() 
    os.rename(subFilePath, reName)
    fh.close()
    os.remove(reName)
    
    newLines = [compactLine(line) for line in lines]
    newLines = CIUtil.crossLineRemoveNotes(newLines)
    newFh = open(subFilePath, 'w')
    newFh.writelines(newLines)
    newFh.flush()
    newFh.close()
    

# YYYYMMDD dir
def makeDirToday():
    dirName = time.strftime("%Y%m%d", time.localtime())
    dirPath = os.path.abspath(os.path.join(CURR_PATH, '..', dirName))
    if os.path.exists(dirPath):
        logger.info('dir %s allready exists! Sub Files delete!' % dirPath)
        CIUtil.removeDir(dirPath)
    else:
        os.makedirs(dirPath)
    return dirPath
    
'''
根节点整合文件
'''
def rootWriter(rootpath):
    dirPath = makeDirToday()
    
    # file 
    for parent, dirs, files in os.walk(rootpath):
        if parent != SRC_PATH: # sub dir
            continue
        
        for filename in files:
            subFilePath = os.path.join(rootpath, filename)
            names = os.path.splitext(subFilePath)
            if names[-1] == Constants.CSS_SUFFIX:
                filePath = os.path.join(dirPath, filename)
                fp = open(filePath, "a+")
                subFileWriter( subFilePath, fp)
                compactFiles(filePath)
                fp.flush()
                fp.close()
                
'''
递归写入子文件
'''
def subFileWriter(abspath, fp):
    fp.write("\n")
    
    fh = open(abspath)
    absDir = os.path.split(abspath) 
    lines = fh.readlines()
    if not lines:
        logger.debug(" file: %s empty!" % abspath)
        
    for line in lines: 
        if CIUtil.regMatchImport(line):
            importfile = extractImportFileName(line)
            filePath = os.path.abspath(os.path.join(absDir[0], importfile))
            subFileWriter(filePath, fp)
        else:
            fp.write(line)

# 提取文件名
def extractImportFileName(filename):
    start = filename.index('"')
    end = filename[start+1:].index('"') + start + 1
    return filename[start+1: end]

if __name__ == "__main__":
    try:
        rootWriter(SRC_PATH)
    except Exception as e:
        print e
        logger.exception(e)
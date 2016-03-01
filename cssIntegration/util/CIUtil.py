# -*- coding: utf-8 -*-       
import re     
import os
from util.CIConst import Constants

# 去除跨行注释
def crossLineRemoveNotes(lines):
    status = False 
    newLines = []
    for line in lines:
        if status :
            endIdx = line.find('*/')
            if endIdx >= 0:
                endIdx = line.index('*/') +1 +len('*/')
                line = line[endIdx:]
                newLines.append(line)
                status = False
        else:
            startIdx = line.find('/*')
            if startIdx >=0 :
                status = True
                startIdx = line.index('/*')
                line = line[:startIdx]
            newLines.append(line)
    return newLines

# 单行去除注释
def lineRemoveNotes(text):
    text = text.strip()
    regex = r"/\*[\w\W]*?\*/"
    match = re.search(regex, text)
    while True:
        match = re.search(regex, text)
        if match:
            start = match.start()
            end = match.end()
            text = text[:start] + text[end:]
        else:
            break
    return text

# 去掉指定符号附近的空格
def removeCloseSpace(symbol, text):
    regex = r"\s*%s\s*" % symbol
    p = re.compile(regex)
    return p.sub(symbol, text)

# 去掉空白
def lineRemoveSpace(text):
    text = text.replace('\r','').replace('\n','').replace('\t','')
    text = removeCloseSpace("{", text)
    text = removeCloseSpace("}", text)
    text = removeCloseSpace(";", text)
    return text

# import匹配
def regMatchImport(text):
    text = text.strip()
    regex = r"%s \"[\w\W]*?%s\";" % (Constants.IMPORT_PREFFIX, Constants.CSS_SUFFIX)
    match = re.search(regex, text)
    if match:
        return True
    else:
        return False


# 删除文件夹下目录及其子文件
def removeDir(dirPath):
    for root, dirs, files in os.walk(dirPath, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
# -*- coding: utf-8 -*-       
import re     
from util.CIConst import Constants
import os

# 注释匹配
def regMatchNotes(text):
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
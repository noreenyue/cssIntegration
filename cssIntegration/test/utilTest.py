#-*- coding: utf-8 -*
import unittest
from util import CILogger, CIUtil

import os
CURR_PATH = os.path.abspath(os.path.dirname(__file__)) 
LOG_PATH = os.path.join(CURR_PATH, '../log/test.log')
logger = CILogger.getLogger(LOG_PATH)

class utilTestCase(unittest.TestCase):
    
#     def test_logger(self):
#         logger.info('test')
#     
#     def test_regular(self):
#         text = "/*test*/"
#         match = CIUtil.lineRemoveNotes(text)
#         self.assertEqual(match, '')
#         
#         text = "%%/*22***/"
#         match = CIUtil.lineRemoveNotes(text)
#         self.assertEqual(match, '%%')
#         
#         text2 = '@import "c/ap.css";'
#         match = CIUtil.regMatchImport(text2)
#         self.assertEqual(match, True)
#         
    def test_crosslineNotes(self):
        filename = 'test.txt'
        fh = open(filename)
        lines = fh.readlines()
        newLines = CIUtil.crossLineRemoveNotes(lines)
        for line in newLines:
            print line 
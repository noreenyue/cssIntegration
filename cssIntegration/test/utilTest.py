#-*- coding: utf-8 -*
import unittest
from util import CILogger

import os
CURR_PATH = os.path.abspath(os.path.dirname(__file__)) 
LOG_PATH = os.path.join(CURR_PATH, '../log/test.log')
logger = CILogger.getLogger(LOG_PATH)

class utilTestCase(unittest.TestCase):
    
    def test_logger(self):
        logger.info('test')
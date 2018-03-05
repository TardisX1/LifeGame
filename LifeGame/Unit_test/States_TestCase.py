#-*- coding:utf-8 –*-

import unittest,pygame
import Codes.Data as Data
import Codes.States as States
from Codes.Cell import Cell

class StatesTestCase(unittest.TestCase):  
    
    def setUp(self):  
        self.screen = pygame.display.set_mode((Data.WIDTH *Cell.size+Data.WIDTH*2, Data.HEIGHT * Cell.size))
    def tearDown(self):   
        self.screen = None  
    
    #初始化
    def testInit(self):  
        self.assertEqual(States.init(self.screen), 'Stop') 
    #停止时
    def testStop(self): 
        self.assertEqual(States.stop(self.screen), 'Stop')
    #演化时 
    def testMove(self): 
        self.assertEqual(States.move(self.screen), 'Move') 
    
    
if __name__ == "__main__":  
          
    unittest.main() 
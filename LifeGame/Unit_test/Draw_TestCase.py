#-*- coding:utf-8 –*-

import unittest,pygame
import numpy as np
import Codes.Data as Data
from Codes.Cell import Cell

from Codes.Draw import draw

class DrawTestCase(unittest.TestCase):  
    
    def setUp(self):  
        self.screen = pygame.display.set_mode((Data.WIDTH *Cell.size+Data.WIDTH*2, Data.HEIGHT * Cell.size))
        pygame.world=np.zeros((Data.HEIGHT,Data.WIDTH))
    def tearDown(self):   
        self.screen = None  
    
    #测试draw方法
    def testDraw(self): 
        draw(self.screen)
        
    
if __name__ == "__main__":  
          
    unittest.main() 
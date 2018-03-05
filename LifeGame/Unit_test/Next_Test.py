#-*- coding:utf-8 –*-

import unittest,pygame
import numpy as np
import Codes.Data as Data
from Codes.Cell import Cell
from Codes.next_generation import next_generation

class StatesTestCase(unittest.TestCase):  
    
    def setUp(self):  
        self.screen = pygame.display.set_mode((Data.WIDTH *Cell.size+Data.WIDTH*2, Data.HEIGHT * Cell.size))
        pygame.world=np.zeros((Data.HEIGHT,Data.WIDTH))
    def tearDown(self):   
        self.screen = None  
    
    def testNext(self):  
        next_generation()
        
   
if __name__ == "__main__":  
          
    unittest.main() 
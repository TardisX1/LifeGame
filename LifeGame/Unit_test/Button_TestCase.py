
#-*- coding:utf-8 –*-

import pygame,unittest
import Codes.Data as Data
from Codes.Cell import Cell
from Codes.Button import Button

class ButtonTestCase(unittest.TestCase):  
    def setUp(self):  
        self.button = Button()  
        self.button.drawbutton(screen=pygame.display.set_mode((Data.WIDTH *Cell.size+Data.WIDTH*2, Data.HEIGHT * Cell.size))) 
    def tearDown(self):   
        self.button = None  
    
    
    def testdrawbutton1(self):  
        self.assertEqual(self.button.positionMove,((2+Data.WIDTH)*Cell.size,Data.HEIGHT))
    def testdrawbutton2(self):  
        self.assertEqual(self.button.positionStop,((2+Data.WIDTH)*Cell.size,Data.HEIGHT*3))
    def testdrawbutton3(self):  
        self.assertEqual(self.button.positionReset,((2+Data.WIDTH)*Cell.size,Data.HEIGHT*5))
if __name__ == "__main__":  
          
    unittest.main() 



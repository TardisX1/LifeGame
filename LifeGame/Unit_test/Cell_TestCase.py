
#-*- coding:utf-8 –*-

import unittest
from Codes.Cell import Cell

class CellTestCase(unittest.TestCase):  
    def setUp(self):  
        self.cell = Cell((500,1000))  
    def tearDown(self):   
        self.cell = None  
    
    #测试cell的成员属性
    def testSize(self):  
        self.assertEqual(self.cell.size, 10) 
    def testImage(self): 
        self.assertEqual(self.cell.rect.topleft,(500,1000))
    
    
if __name__ == "__main__":  
          
    unittest.main() 
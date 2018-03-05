
#-*- coding:utf-8 –*-
import pygame
import Data
from Cell import Cell

#按钮类
class Button():
    def __init__(self): #指定按钮的图像和位置
        self.imageMove= pygame.image.load('../Pictures/Move.PNG')#进行演化
        self.imageStop= pygame.image.load('../Pictures/Stop.PNG')#停止
        self.imageReset= pygame.image.load('../Pictures/Reset.PNG')#重置地图
        self.imageDes=pygame.image.load('../Pictures/Des.PNG')#游戏说明
        
        #设置图片位置
        self.positionMove = ((2+Data.WIDTH)*Cell.size,Data.HEIGHT)
        self.positionStop = ((2+Data.WIDTH)*Cell.size,Data.HEIGHT*3)
        self.positionReset = ((2+Data.WIDTH)*Cell.size,Data.HEIGHT*5)
        self.positionDes=((1+Data.WIDTH)*Cell.size,Data.HEIGHT*6+30)
    
    def drawbutton(self,screen): #画按钮
        screen.blit(self.imageMove,self.positionMove)
        screen.blit(self.imageStop,self.positionStop)
        screen.blit(self.imageReset,self.positionReset) 
        screen.blit(self.imageDes,self.positionDes) 
            
                
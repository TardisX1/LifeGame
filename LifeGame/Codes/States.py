
#-*- coding:utf-8 –*-

import pygame,sys, time
import numpy as np
from pygame.locals import *

import Draw,next_generation,Data
from Cell import Cell

#地图状态

#矩阵宽与高
WIDTH = Data.WIDTH
HEIGHT = Data.HEIGHT

#记录鼠标按键情况的全局变量
pygame.button_down = False

#记录游戏世界的矩阵 一个指定形状的数组
pygame.world=np.zeros((HEIGHT,WIDTH))


#地图初始化
def init(screen):
    pygame.world.fill(0) #将数组用0填充
    Draw.draw(screen)
    return 'Stop'

#停止时的操作
def stop(screen):
    #pygame中的事件处理都放在一个while True的循环中，但是这样会造成死循环，所以在里面加一句sys.exit()来退出
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:#持续按下鼠标
            pygame.button_down = True
            pygame.button_type = event.button

        if event.type == MOUSEBUTTONUP:#鼠标松开
            pygame.button_down = False

        if pygame.button_down:#button_down的bool值由上面两段确定
            mouse_x, mouse_y = pygame.mouse.get_pos()

            sp_col = mouse_x / Cell.size;
            sp_row = mouse_y / Cell.size;
            
            #画细胞
            if sp_col<WIDTH and sp_row<HEIGHT: #将右边的按钮栏排除在外
                if pygame.button_type == 1: #鼠标左键
                    pygame.world[sp_row][sp_col] = 1
                elif pygame.button_type == 3: #鼠标右键
                    pygame.world[sp_row][sp_col] = 0
                Draw.draw(screen)
            
            #定义按钮功能
            #鼠标已经按下，计算鼠标位置是在哪一个按钮上
            if (2+WIDTH)*Cell.size<mouse_x<(2+WIDTH)*Cell.size+Draw.button.imageMove.get_width() and HEIGHT<mouse_y<HEIGHT+Draw.button.imageMove.get_height():
                return 'Move'
            if (2+WIDTH)*Cell.size<mouse_x<(2+WIDTH)*Cell.size+Draw.button.imageStop.get_width() and HEIGHT*3<mouse_y<HEIGHT*3+Draw.button.imageStop.get_height():
                return 'Stop'
            if (2+WIDTH)*Cell.size<mouse_x<(2+WIDTH)*Cell.size+Draw.button.imageReset.get_width() and HEIGHT*5<mouse_y<HEIGHT*5+Draw.button.imageReset.get_height():
                return 'Reset'

    return 'Stop'

#计时器，控制帧率
pygame.clock_start = 0


#进行演化时的操作
def move(screen):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
       
        if event.type == MOUSEBUTTONDOWN:
            pygame.button_down = True
            pygame.button_type = event.button

        if event.type == MOUSEBUTTONUP:
            pygame.button_down = False

        if pygame.button_down:
            mouse_x, mouse_y = pygame.mouse.get_pos() #获得鼠标的当前位置

            sp_col = mouse_x / Cell.size;
            sp_row = mouse_y / Cell.size;
            
            if sp_col<WIDTH and sp_row<HEIGHT: #将右边的按钮栏排除在外
                if pygame.button_type == 1:
                    pygame.world[sp_row][sp_col] = 1
                elif pygame.button_type == 3:
                    pygame.world[sp_row][sp_col] = 0
                Draw.draw(screen)
            
            #定义按钮功能
            if (2+WIDTH)*Cell.size<mouse_x<(2+WIDTH)*Cell.size+Draw.button.imageMove.get_width() and HEIGHT<mouse_y<HEIGHT+Draw.button.imageMove.get_height():
                return 'Move'
            if (2+WIDTH)*Cell.size<mouse_x<(2+WIDTH)*Cell.size+Draw.button.imageStop.get_width() and HEIGHT*3<mouse_y<HEIGHT*3+Draw.button.imageStop.get_height():
                return 'Stop'
            if (2+WIDTH)*Cell.size<mouse_x<(2+WIDTH)*Cell.size+Draw.button.imageReset.get_width() and HEIGHT*5<mouse_y<HEIGHT*5+Draw.button.imageReset.get_height():
                return 'Reset'

    if time.clock() - pygame.clock_start > 0.02:
        next_generation.next_generation()
        Draw.draw(screen)
        pygame.clock_start = time.clock()

    return 'Move'

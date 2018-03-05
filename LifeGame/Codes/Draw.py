
#-*- coding:utf-8 –*-
import pygame
import Data,Button
from Cell import Cell

#按钮
button=Button.Button()

#绘制地图 
def draw(screen):
    screen.fill((0,0,0)) #将画布重置擦除
    button.drawbutton(screen) #画上按钮
    #画上格子
    line=1
    size1=[line*Cell.size for line in range(Data.HEIGHT)]
    size2=[line*Cell.size for line in range(Data.WIDTH+1)]#多加1是为了将右边线画上
    for lines in size1:#画横线
        pygame.draw.line(screen,(54,54,54), (0,lines), (Data.WIDTH*Cell.size,lines))
    for lines in size2:#画竖线
        pygame.draw.line(screen,(54,54,54), (lines,0), (lines,Data.HEIGHT*Cell.size))

    #依次遍历细胞
    for sp_col in range(pygame.world.shape[1]):
        for sp_row in range(pygame.world.shape[0]):
            if pygame.world[sp_row][sp_col]:
                new_cell = Cell((sp_col * Cell.size,sp_row * Cell.size))
                screen.blit(new_cell.image,new_cell.rect)

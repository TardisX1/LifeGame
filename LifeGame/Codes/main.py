
#-*- coding:utf-8 –*-
import pygame
import States,Data
from Cell import Cell


if __name__ == '__main__':
    
    
    pygame.init()  #对Pygame库进行初始化
    pygame.display.set_caption('简单生命游戏')

    #界面
    screen = pygame.display.set_mode((Data.WIDTH *Cell.size+Data.WIDTH*2, Data.HEIGHT * Cell.size))

    #状态机对应三种状态，初始化，停止，进行
    state_actions = {
            'Reset': States.init,
            'Stop': States.stop,
            'Move': States.move
        }
    state = 'Reset'

   
    while True: # 游戏主循环

        state = state_actions[state](screen)
        pygame.display.update()
		


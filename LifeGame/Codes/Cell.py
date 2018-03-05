
#-*- coding:utf-8 –*-
import pygame

#细胞类
class Cell(pygame.sprite.Sprite):

    size = 10

    def __init__(self, position):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([self.size, self.size])

        #填上红色
        self.image.fill((255,0,0))

        # 创建一个以左上角为锚点的矩形
        self.rect = self.image.get_rect()
        self.rect.topleft = position

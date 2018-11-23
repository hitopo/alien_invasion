import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """飞船类，用来描述飞船行为的类"""

    def __init__(self, ai_settings, screen):
        """初始化飞船，设置其初始位置"""
        super(Ship, self).__init__()
        self.screen = screen
        # 加载游戏设置信息
        self.ai_settings = ai_settings

        # 加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放置在屏幕底部的中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""

        '''
        这里不能使用if和elif，必须使用两个if
        否则左右两个键一起按下的时候就会向右走
        这样会使飞船在原地不动
        '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 更新飞船的center值，而不是rect
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """将飞船位置重置，即重新居中"""
        self.center = self.screen_rect.centerx

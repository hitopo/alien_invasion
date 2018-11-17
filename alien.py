import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """外星人类，用来描述外星人"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，设置rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 外星人出生位置在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """检测外星人是否到达屏幕边缘"""
        screen_rect = self.screen.get_rect()
        # 到达右边缘
        if self.rect.right >= screen_rect.right:
            return True
        # 到达左边缘
        elif self.rect.left <= 0:
            return True

import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建存储子弹的编组
    bullets = Group()

    # 开始游戏主循环
    while True:
        # 监视鼠标和键盘事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 在刷新屏幕之前更新飞船位置，刷新屏幕之后方便显示出飞船位置
        ship.update()
        bullets.update()
        # 更新子弹信息
        gf.update_bullets(bullets)
        # 绘制屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()

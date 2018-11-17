import pygame
from pygame.sprite import Group

import game_functions as gf
from button import Button
from game_stats import GameStats
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建开始按钮
    play_button = Button(ai_settings, screen, 'Play')

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一群外星人
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建存储子弹的编组
    bullets = Group()

    # 创建游戏信息统计
    stats = GameStats(ai_settings)

    # 开始游戏主循环
    while True:
        # 监视鼠标和键盘事件
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        # 再更新元素位置信息之前就检查是否还需要继续游戏（有无生命）
        if stats.game_active:
            # 在刷新屏幕之前更新飞船位置，刷新屏幕之后方便显示出飞船位置
            ship.update()
            # 更新子弹信息
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # 更新外星人移动信息
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # 绘制屏幕
        gf.update_screen(ai_settings, screen, stats, ship, aliens,
                         bullets, play_button)


run_game()

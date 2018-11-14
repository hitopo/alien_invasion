import sys

import pygame

from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 响应关闭按钮
        if event.type == pygame.QUIT:
            sys.exit()
        # 响应键盘按下事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # 响应键盘松开时间
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """开火设置"""
    # 创建一个新的子弹，并放到编组bullets中
    # 子弹数是有限制的
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settins, screen, ship, bullets):
    """更新屏幕上的图像，切换到新的屏幕"""
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settins.bg_color)
    '''
        这里要注意，如果先刷新屏幕，在刷新飞船
        那么就看不见飞船了
        因为飞船被背景色覆盖掉了
    '''

    # 绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 绘制飞船
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹位置"""
    bullets.update()
    # 删除多余子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

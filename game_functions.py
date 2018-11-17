import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 响应关闭按钮
        if event.type == pygame.QUIT:
            sys.exit()
        # 响应键盘按下事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # 响应键盘松开事件
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        # 响应鼠标按下事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):
    """玩家单击Play按钮开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏中统计信息
        stats.reset_stats()
        # 重置游戏速度
        ai_settings.initialize_dynamic_settings()
        # 激活游戏
        stats.game_active = True
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏
        reset_game(ai_settings, screen, ship, aliens, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """处理键盘按下事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """开火设置"""
    # 创建一个新的子弹，并放到编组bullets中
    # 子弹数是有限制的
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settins, screen, stats, ship, aliens,
                  bullets, play_button):
    """更新屏幕上的图像，切换到新的屏幕"""
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settins.bg_color)
    # 这里要注意，如果先刷新屏幕，在刷新飞船
    # 那么就看不见飞船了
    # 因为飞船被背景色覆盖掉了
    # 绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 绘制飞船
    ship.blitme()

    # 绘制外星人
    aliens.draw(screen)

    # 如果当前游戏不可用（暂停状态），那么显示button
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹位置"""
    bullets.update()
    # 删除多余子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检测是否有子弹击中了外星人
    # 如果是这样，那么删除子弹和对应的外星人
    check_bullet_alien_collisions(ai_settings, aliens, bullets, screen, ship)


def check_bullet_alien_collisions(ai_settings, aliens, bullets, screen, ship):
    """检测子弹外星人碰撞，并删除子弹和对应的外星人"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 如果外星人全部都被消灭了，那么重新创建外星人并删除所有子弹
    if len(aliens) == 0:
        bullets.empty()
        # 加快游戏速度
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建一群外星人"""
    # 创建一群外星人，计算一行可以容纳多少外星人
    # 外星人的间距为外星人自身的宽度
    alien = Alien(ai_settings, screen)
    # 一行可以创建多少外星人
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.x)
    # 可以创建几行外星人
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # alien_number指的是第几个alien，方便计算每个alien的x位置
            create_alien(ai_settings, screen, aliens, alien_number,
                         row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行最多可以放几个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alient_height):
    """计算屏幕可以容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                         (3 * alient_height) - ship_height)
    number_rows = int(available_space_y / (2 * alient_height))
    return number_rows


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """更新外星人位置"""
    # 检查外星人是否到达左右边缘
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # 检查外星人是否到达底端
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船，或者外星人到达屏幕底端"""
    # 检查生命情况，没命了就game over
    if stats.ships_left > 0:
        stats.ships_left -= 1
        # 重置游戏
        reset_game(ai_settings, screen, ship, aliens, bullets)

        # 暂停一下，让用户发现失去一条命
        sleep(0.5)
    else:
        # 游戏结束
        stats.game_active = False
        # 显示光标，让用户能够开始游戏
        pygame.mouse.set_visible(True)


def reset_game(ai_settings, screen, ship, aliens, bullets):
    """重置游戏"""
    # 清空外星人和子弹组
    aliens.empty()
    bullets.empty()
    # 创建新的外星人，重置飞船的位置
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检测是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            # 有外星人到达屏幕底端
            # 像飞船撞到一样处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def change_fleet_direction(ai_settings, aliens):
    """将外星人群改变方向，并集体向下移动"""
    # 集体向下移动
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    # 改变方向
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    """检测是否有外星人到达屏幕左右边缘，并改变外星人群移动方向"""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

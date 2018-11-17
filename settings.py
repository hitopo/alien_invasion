class Settings:
    """存储着《外星人入侵所有设置的类》"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 550
        # 背景颜色
        self.bg_color = (230, 230, 230)
        # 飞船速度
        self.ship_speed_factor = 1.4

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # 外星人参数设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction=1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

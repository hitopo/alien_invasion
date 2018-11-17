class Settings:
    """存储着《外星人入侵所有设置的类》"""

    def __init__(self):
        """初始化游戏静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 550
        # 背景颜色
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # 外星人参数设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 20
        # fleet_direction=1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

        # Play按钮属性设置
        self.button_width, self.button_height = 175, 50
        self.button_color = (0, 255, 0)
        self.button_text_color = (255, 255, 255)

        # 加快游戏节奏的比例系数
        self.speedup_scale = 1.2

        # 加载动态设置
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随着游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示右，为-1表示左
        self.fleet_direction = 1

    def increase_speed(self):
        """增加游戏速度"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

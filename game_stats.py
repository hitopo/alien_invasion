class GameStats:
    """用来记录游戏过程中的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        # 初始化单次游戏的信息
        self.reset_stats()
        # 游戏状态，False代表游戏结束
        self.game_active = False

    def reset_stats(self):
        """初始化在游戏过程中可能会变化的量"""
        self.ships_left = self.ai_settings.ship_limit

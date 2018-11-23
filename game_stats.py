class GameStats:
    """用来记录游戏过程中的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        # 初始化单次游戏的信息
        self.reset_stats()
        # 游戏状态，False代表游戏结束
        self.game_active = False
        # 任何情况下都不应该重置最高分
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏过程中可能会变化的量"""
        self.ships_left = self.ai_settings.ship_limit

        # 重新开始游戏之后重置得分
        self.score = 0

        # 当前外星人等级
        self.level = 1



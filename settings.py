class Settings():
    """存储外星人入侵游戏的所有设置"""

    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹设置( 数值代表像素)
        self.bullets_speed_factor = 1
        self.bullets_width = 3
        self.bullets_height = 15
        self.bullets_color = 60,60,60
        self.bullets_allowed = 5


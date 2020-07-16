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
        self.ship_limit = 3

        # 子弹设置( 数值代表像素)
        self.bullets_speed_factor = 1
        self.bullets_width = 600
        self.bullets_height = 15
        self.bullets_color = 60,60,60
        self.bullets_allowed = 5
        
        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1



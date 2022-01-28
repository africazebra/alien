class Settings:

    def __init__(self):
        """初始化"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 1000
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.0
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 10

        # 外星人设置
        self.alien_speed = 0.1
        self.fleet_drop_speed = 0.1
        # fleet_direction 为1表示向右移q动，为-1表示向左移动
        self.fleet_direction = 1

        # 加快游戏节奏
        self.speedup_scale = 1.01
        # 外星人分数的提高速度
        self.score_scale = 1.05
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 0.5
        self.bullet_speed = 1.0
        self.alien_speed = 0.1
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)
        # print(self.alien_points)



class Settings:
    '''储存游戏《外星人入侵》中所有设置的类'''
    def __init__(self):
        '''初始化游戏的静态设置'''
        # 屏幕设置
        self.background_image_filename = r'F:\Python\pythonProject\alien_invasion\images\bg.png'
        self.screen_width = 1248
        self.screen_height = 777
        self.bg_color = (230, 200, 200)
        # 飞船速度
        self.ship_limit = 1
        # 子弹设置
        self.bullet_width = 150
        self.bullet_height = 15
        self.bullet_color = (200, 200, 169)
        self.bullet_allowed = 3    # 未消失的子弹
        # 外星人设置
        self.fleet_drop_speed = 50
        # 加快游戏节奏的速度
        self.speedup_scale = 1.1
        # 外星人分数的提高速度。
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置。'''
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 1.0
        # fleet_direction 为1表示右移，为-1表示左移
        self.fleet_direction = 1
        # 计分.
        self.alien_points = 50

    def increase_speed(self):
        '''提高速度设置和外星人分数。'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super().__init__()  # 用python3的语法调用super来继承sprite 精灵. python2写法: super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # lode aline image and set "rect" attribute
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        # set alien start at top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the exact locaton of the alines
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the aline at the specified location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向左或向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

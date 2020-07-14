# sys 模块用于退出
import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    #初始化 游戏模块并且创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:
        #设置背景色, 重绘屏幕.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

    # #设置背景色
    # bg_color = (230,230,230)

        # 让最近的屏幕可见  用于刷新
        pygame.display.flip()

run_game()

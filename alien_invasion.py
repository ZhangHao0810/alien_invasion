import pygame

from settings import Settings
from ship import Ship
# from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化 游戏模块并且创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船,一个子弹编组, 一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群 , 编组 aliens 被添加进外星人.  之后再调用aliens 就是含有外星人对象的编组了.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.upadte_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()

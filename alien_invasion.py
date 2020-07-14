# sys 模块用于退出
import sys

import pygame

def run_game():
    #初始化 游戏模块并且创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    #设置背景色
    bg_color = (230,230,230)

    # 游戏主循环
    while True:

        #监视鼠标和键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #背景色填充.
        screen.fill(bg_color)

        # 让最近的屏幕可见  用于刷新
        pygame.display.flip()

run_game()

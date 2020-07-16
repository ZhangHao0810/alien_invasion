import sys

import pygame
from bullet import Bullet
from alien import Alien


def check_events():
    # 响应鼠标和键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹, 并且加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullets = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullets)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.K_q:
            sys.exit()


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕的图像, 并切换到新屏幕"""
    # 每次循环重绘屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Draw all the bullets behind the ship and the aline
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)  # 对编组调用draw时, Pygame会自动绘制编组的每个元素. 这个时候, aliens编组已经

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def upadte_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹位置
    bullets.update() 将为编组bullets 中的每颗子弹调用bullet.update()"""
    bullets.update()

    # 删除已消失的子弹  不应该从列表或者编组中删除条目, 所以这里遍历的是编组的副本.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的子弹和外星人
    """
    方法sprite.groupcollide() 将每颗子弹的rect 同每个外星人的rect 进行比较，并返回一个字典，其中包含发生了碰撞的子弹和外星人。在这个字典中，每个键都是一
颗子弹，而相应的值都是被击中的外星人
    下面的这行代码遍历编组bullets 中的每颗子弹，再遍历编组aliens 中的每个外星人。每当有子弹和外星人的rect 重叠时，groupcollide() 就在它返回的字典中添加一
个键-值对。
    两个实参True 告诉Pygame删除发生碰撞的子弹和外星人, 反之 False表示不删除这个编组元素.
    """
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人.
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可以容纳多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人并将其加入当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    """
    检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

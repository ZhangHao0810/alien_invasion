import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设定其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        """
        首先，我们导入了模块pygame 。Ship 的方法__init__() 接受两个参数：引用self 和screen ，其中后者指定了要将飞船绘制到什么地方。为加载图像，我们调用
        了pygame.image.load() 。这个函数返回一个表示飞船的surface，而我们将这个surface存储到了self.image 中。
        加载图像后，我们使用get_rect() 获取相应surface的属性rect 。Pygame的效率之所以如此高，一个原因是它让你能够像处理矩形（rect 对象）一样处理游戏元
        素，即便它们的形状并非矩形。像处理矩形一样处理游戏元素之所以高效，是因为矩形是简单的几何形状。这种做法的效果通常很好，游戏玩家几乎注意不到我们处理的不是游
        戏元素的实际形状。
        """
        # 加载飞船图像并获取其外接矩形(图像的和屏幕的外接矩形 , 因为Pygame 将 元素对象定义为了矩形 rect, .
        self.image = pygame.image.load("image/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """
        处理rect 对象时，可使用矩形四角和中心的x 和y 坐标。可通过设置这些值来指定矩形的位置。
        要将游戏元素居中，可设置相应rect 对象的属性center 、centerx 或centery 。要让游戏元素与屏幕边缘对齐，可使用属性top 、bottom 、left 或right ；要调整游
        戏元素的水平或垂直位置，可使用属性x 和y ，它们分别是相应矩形左上角的x 和y 坐标。这些属性让你无需去做游戏开发人员原本需要手工完成的计算，你经常会用到这些属
        性。
        注意　在Pygame中，原点(0, 0)位于屏幕左上角，向右下方移动时，坐标值将增大。在1200×800的屏幕上，原点位于左上角，而右下角的坐标为(1200, 800)。
        """
        # 将飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志( 这样的类似属性的东西, 要放在Init 函数中)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值, 而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船, blit() 是内置的函数  参数是图像对象和矩形对象."""
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx

import pygame
import sys
import random

# 定义玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (250, 250)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# 定义敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 500)
        self.rect.y = random.randint(0, 500)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = random.randint(0, 500)

# 初始化Pygame
pygame.init()

# 设置屏幕大小和标题
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Simple Game")

# 创建玩家和敌人组
all_sprites = pygame.sprite.Group()
player = Player()
enemies = [Enemy() for _ in range(5)]  # 创建5个敌人

all_sprites.add(player)
all_sprites.add(enemies)

# 游戏主循环
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 更新所有精灵
    all_sprites.update()

    # 碰撞检测
    hits = pygame.sprite.spritecollide(player, all_sprites, False)
    if hits:
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # 绘制背景
    screen.fill((255, 255, 255))

    # 绘制所有精灵
    all_sprites.draw(screen)

    # 刷新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

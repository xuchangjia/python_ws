import pygame
import random

# 初始化游戏
pygame.init()

# 定义游戏窗口的宽和高
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 加载飞机图像
player_img = pygame.image.load("./game/player.png")
player_rect = player_img.get_rect()
player_rect.topleft = [width // 2, height - player_rect.height - 10]

# 加载敌机图像
enemy_img = pygame.image.load("./game/enemy.png")
enemy_rect = enemy_img.get_rect()
enemies = []
for i in range(5):
    enemy_rect.topleft = [random.randint(0, width - enemy_rect.width), random.randint(-height, 0)]
    enemies.append(enemy_rect.copy())

# 加载子弹图像
bullet_img = pygame.image.load("./game/bu.png")
bullet_rect = bullet_img.get_rect()
bullets = []

# 设置字体
font = pygame.font.Font(None, 36)

# 设置游戏时钟
clock = pygame.time.Clock()

# 初始化得分
score = 0

# 游戏循环
running = True
while running:
    # 处理退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # 按下空格键发射子弹
                bullet_rect.topleft = [player_rect.x + player_rect.width // 2 - bullet_rect.width // 2, player_rect.y]
                bullets.append(bullet_rect.copy())

    # 移动玩家飞机
    player_pos = pygame.mouse.get_pos()
    player_rect.centerx = player_pos[0]

    # 移动敌机
    for enemy in enemies:
        enemy.y += 5
        if enemy.y > height:
            enemy.x = random.randint(0, width - enemy_rect.width)
            enemy.y = random.randint(-height, 0)

    # 移动子弹
    for bullet in bullets:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)
        else:
            # 检测子弹和敌机的碰撞
            for enemy in enemies:
                if bullet.colliderect(enemy):
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    score += 1
                    break

    # 检测碰撞
    if player_rect.collidelist(enemies) != -1:
        running = False

    # 渲染背景
    screen.fill((0, 0, 0))

    # 渲染飞机
    screen.blit(player_img, player_rect)

    # 渲染敌机
    for enemy in enemies:
        screen.blit(enemy_img, enemy)

    # 渲染子弹
    for bullet in bullets:
        screen.blit(bullet_img, bullet)

    # 渲染得分
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # 更新显示
    pygame.display.flip()

    # 控

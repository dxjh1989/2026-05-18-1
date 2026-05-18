import pygame
import random
import math

# 初始化 Pygame
pygame.init()

# 視窗設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Open World RPG - GitHub Open Source Project")

# 顏色定義
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
GRAY = (128, 128, 128)
BLUE = (50, 150, 255)
WHITE = (255, 255, 255)

# 遊戲時鐘
clock = pygame.time.Clock()
FPS = 60

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 15
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed

    def draw(self, screen, camera_x, camera_y):
        # 將世界座標轉換為螢幕上的相對座標
        screen_x = self.x - camera_x
        screen_y = self.y - camera_y
        pygame.draw.circle(screen, BLUE, (int(screen_x), int(screen_y)), self.radius)

class World:
    def __init__(self):
        # 儲存地圖上的物件（樹木、岩石）及其世界座標
        self.objects = []
        self.generate_world()

    def generate_world(self):
        # 在方圓 3000 像素的開放世界中隨機生成一些地標
        for _ in range(200):
            obj_type = random.choice(["tree", "rock"])
            x = random.randint(-1500, 1500)
            y = random.randint(-1500, 1500)
            self.objects.append({"type": obj_type, "x": x, "y": y})

    def draw(self, screen, camera_x, camera_y):
        # 繪製草地背景（滿鋪畫面）
        screen.fill(GREEN)

        # 繪製世界邊界（讓玩家知道極限在哪，也可以做成無限延伸）
        # 這裡繪製一個簡單的格線作為世界參考
        grid_size = 100
        start_x = int(camera_x // grid_size) * grid_size - grid_size
        start_y = int(camera_y // grid_size) * grid_size - grid_size
        
        for x in range(start_x, start_x + SCREEN_WIDTH + grid_size * 2, grid_size):
            pygame.draw.line(screen, DARK_GREEN, (x - camera_x, 0), (x - camera_x, SCREEN_HEIGHT), 1)
        for y in range(start_y, start_y + SCREEN_HEIGHT + grid_size * 2, grid_size):
            pygame.draw.line(screen, DARK_GREEN, (0, y - camera_y), (SCREEN_WIDTH, y - camera_y), 1)

        # 繪製世界中的物件
        for obj in self.objects:
            screen_x = obj["x"] - camera_x
            screen_y = obj["y"] - camera_y

            # 效能優化：只繪製在螢幕可見範圍內的物件
            if -50 < screen_x < SCREEN_WIDTH + 50 and -50 < screen_y < SCREEN_HEIGHT + 50:
                if obj["type"] == "tree":
                    pygame.draw.circle(screen, DARK_GREEN, (screen_x, screen_y), 20)  # 樹冠
                    pygame.draw.rect(screen, (139, 69, 19), (screen_x - 5, screen_y, 10, 25))  # 樹幹
                elif obj["type"] == "rock":
                    pygame.draw.circle(screen, GRAY, (screen_x, screen_y), 15)

def main():
    player = Player(0, 0)
    world = World()
    
    running = True
    while running:
        clock.tick(FPS)
        
        # 事件處理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 玩家移動
        keys = pygame.key.get_pressed()
        player.move(keys)

        # 鏡頭系統：讓鏡頭中心跟隨玩家
        camera_x = player.x - SCREEN_WIDTH // 2
        camera_y = player.y - SCREEN_HEIGHT // 2

        # 繪製畫面
        world.draw(screen, camera_x, camera_y)
        player.draw(screen, camera_x, camera_y)

        # 顯示玩家當前的座標 (Debug 資訊)
        font = pygame.font.SysFont(None, 24)
        coord_text = font.render(f"World X: {int(player.x)}, Y: {int(player.y)}", True, WHITE)
        screen.blit(coord_text, (10, 10))
        controls_text = font.render("Move: WASD / Arrows", True, WHITE)
        screen.blit(controls_text, (10, 35))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
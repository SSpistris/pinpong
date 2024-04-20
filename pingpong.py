from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,image_name, speed, x, y, w, h):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_p = key.get_pressed()
        if keys_p[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_p[K_s] and self.rect.y < 390:
            self.rect.y += self.speed
    def update1(self):
        keys_p = key.get_pressed()
        if keys_p[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_p[K_DOWN] and self.rect.y < 390:
            self.rect.y += self.speed
class Boll(GameSprite):
    def update2(self, speed_x, speed_y):
        self.rect.x += speed_x
        self.rect.y += speed_y
        if sprite.collide_rect(platforma1, bol) or sprite.collide_rect(platforma2, bol):
            speed_x *= -1
        if self.rect.y <= 0:
            speed_y *= -1
        if self.rect.y >= 500:
            self.rect.y *= -1
screen = display.set_mode((700, 500))
clock = time.Clock()
background_image = transform.scale(image.load('fonmain.jpg'), (700, 500))
bol = Boll('m_bol.webp', 3, 300, 200, 65, 65)
platforma1 = Player('palka.png', 10, 40, 75, 20, 150)
platforma2 = Player('palka.png', 10, 650, 75, 20, 150)
game = True
while game:
    screen.blit(background_image, (0, 0))
    bol.reset()
    bol.update2(2, 2)
    platforma1.reset()
    platforma1.update()
    platforma2.reset()
    platforma2.update1()
   
    for a in event.get():
        if a.type == QUIT:
            game = False

    display.update()
    clock.tick(60)

from pygame import *
font.init()
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
    def update2(self):
        global speed_x, speed_y, game, point_l, point_r, point_all, lose, finesh
        self.rect.x += speed_x
        self.rect.y += speed_y
        if sprite.collide_rect(platforma1, bol) or sprite.collide_rect(platforma2, bol):
            speed_x *= -1
        if self.rect.y <= 0:
            speed_y *= -1
        if self.rect.y >= 500-65:
            speed_y *= -1
        if self.rect.x <= -65:
            lose = font2.render('Игрок 2 выйграл', True, (255, 0, 0))
            finesh = True
            
        if self.rect.x >= 765:
            lose = font2.render('Игрок 1 выйграл', True, (255, 0, 0))
            finesh = True
            
        if sprite.collide_rect(platforma1, bol):
            point_l += 1
        if sprite.collide_rect(platforma2, bol):
            point_r += 1
        if sprite.collide_rect(platforma1, bol) or sprite.collide_rect(platforma2, bol):
            point_all += 1
            if point_all == 5:
                speed_x += -1
                speed_y += -1
            elif point_all == 10:
                speed_x += 1
                speed_y += 1
            elif point_all == 15:
                speed_x += -1
                speed_y += -1
            elif point_all == 20:
                speed_x += 1
                speed_y += 1
            elif point_all == 25:
                speed_x += -1
                speed_y += -1
            elif point_all == 30:
                speed_x += 1
                speed_y += 1
            elif point_all == 35:
                speed_x += -1
                speed_y += -1
            elif point_all == 40:
                speed_x += 1
                speed_y += 1
            if point_l == 100:
                lose = font2.render('Игрок 1 выйграл', True, (255, 0, 0))
                finesh = True
            if point_r == 100:
                lose = font2.render('Игрок 2 выйграл', True, (255, 0, 0))
                finesh = True
screen = display.set_mode((700, 500))
clock = time.Clock()
background_image = transform.scale(image.load('fonmain.jpg'), (700, 500))
bol = Boll('m_bol.png', 3, 300, 200, 65, 65)
platforma1 = Player('sword.png', 10, 40, 75, 20, 150)
platforma2 = Player('sword.png', 10, 650, 75, 20, 150)
font1 = font.SysFont(None, 50)
font2 = font.SysFont(None, 70)
point_all = 0
point_r = 0
point_l = 0
balls_l = font1.render('Баллы:' + str(point_l), True, (255, 0, 0))
balls_r = font1.render('Баллы:' + str(point_r), True, (255, 0, 0))
finesh = False
game = True
speed_x = 2
speed_y = 2
while game:
    if not finesh:
        screen.blit(background_image, (0, 0))
        bol.reset()
        bol.update2()
        platforma1.reset()
        platforma1.update()
        platforma2.reset()
        platforma2.update1()
        screen.blit(balls_l, (10, 10))
        screen.blit(balls_r, (500, 10))
        balls_l = font1.render('Баллы:' + str(point_l), True, (255, 0, 0))
        balls_r = font1.render('Баллы:' + str(point_r), True, (255, 0, 0))
    if finesh:
        screen.blit(lose, (200, 200))
    for a in event.get():
        if a.type == QUIT:
            game = False

    display.update()
    clock.tick(60)

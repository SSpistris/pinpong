from pygame import *

screen = display.set_mode((700, 500))
clock = time.Clock()
background_image = transform.scale(image.load('fonmain.jpg'), (700, 500))
game = True
while game:
    screen.blit(background_image, (0, 0))
   
    for a in event.get():
        if a.type == QUIT:
            game = False

    display.update()
    clock.tick(60)

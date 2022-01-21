from pygame import *

#создай окно игры
window = display.set_mode((1000, 700))
display.set_caption('догонялки')
#задай фон сцены
background = transform.scale(image.load('ping.jpg'), (1000, 700))
#создай 2 спрайта и размести их на сцене
x1 = 0
y1 = 300

x2 = 900
y2 = 300

sprite1 = transform.scale(image.load('raketka1.png'), (100, 100)
)
sprite2 = transform.scale(image.load('raketka2.jpg'), (100, 100)
)

run = True

clock = time.Clock()
FPS = 60

while run:
    window.blit(background,(0, 0))

    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            run = False

    speed = 4

    keys_pressed = key.get_pressed()

    if keys_pressed[K_w] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_s] and y1 < 600:
        y1 += speed

    if keys_pressed[K_UP] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_DOWN] and y2 < 600:
        y2 += speed
        
    
    
    
    
    display.update()
    clock.tick(FPS)
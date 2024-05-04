from pygame import *

# Создание игрового окна
back_color = (200, 255, 255) # цвет фона
win_width = 600 # ширина
win_height = 500 # высота

window = display.set_mode((win_width, win_height)) # установка ширины и высоты
window.fill(back_color) # установка цвета фона

# Создание надписей
font.init()
font_settings = font.Font(None, 35)
message = font_settings.render('Сообщение', True, (180, 0, 0))

# фоновая музыка
mixer.init()
mixer.music.load('название файла')
mixer.music.play()

# одиночный звук
fire_sound = mixer.Sound('название файла')
fire_sound.play()

# Игровой цикл
game = True
finish = False

clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        keys = key.get_pressed()
        
    display.update()
    clock.tick(FPS)

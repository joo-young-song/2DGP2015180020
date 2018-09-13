from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0

frame = 0

head = 0
while head < 3:
    if head == 0:
        while x < 810:
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 100, 100, 100, x, 90)
            update_canvas()
            frame = (frame + 1) % 8
            x = x + 10
            delay(0.05)
            get_events()
            if x >= 800:
                head = 1
    elif head == 1:
        while x > -10:
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, x, 90)
            update_canvas()
            frame = (frame + 1) % 8
            x = x - 10
            delay(0.05)
            get_events()
            if x <= 0:
                head = 0

close_canvas()


import game_framework
import title_state
import global_state
from pico2d import *
name = "StartState"
image = None
font = None
speed = 0


def enter():
    global image,font
    image = load_image('Resource/store.png')
    font = load_font('Font/ENCR10B.TTF', 50)
def exit():
    global image
    del(image)

def update(frame_time):
    global speed
    speed = global_state.high_speed / 10 * 0.3

def draw(frame_time):
    global image,totalmoney,high_speed, rockets,global_state
    clear_canvas()
    image.clip_draw(0, 0, 1600, 900, 500, 400, 1000, 800)
    font.draw(300, 700, 'you have $%d' % global_state.totalmoney, (0, 0, 0))
    font.draw(80, 400, 'highspeed : %d'%speed, (0, 0, 0))
    font.draw(80, 450, '$50', (0, 0, 0))
    font.draw(550, 400, 'rocket : %d' %global_state.rockets , (0, 0, 0))
    font.draw(550, 450, '$100', (0, 0, 0))
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            if global_state.totalmoney > 50:
                global_state.high_speed += 300
                global_state.totalmoney -= 50
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            if global_state.totalmoney > 100:
                global_state.rockets += 1
                global_state.totalmoney -= 100



def pause(): pass


def resume(): pass





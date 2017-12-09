import game_framework
from pico2d import *
import fire_state

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('Resource/title.png')

def exit():
    global image
    del(image)

def update(frame_time):
    global logo_time
    if logo_time > 1.0:
        logo_time = 0
    logo_time += 0.01 * frame_time

def draw(frame_time):
    global image
    clear_canvas()
    image.clip_draw(0, 0, 1600, 900, 500, 400, 1000, 800)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            game_framework.change_state(fire_state)



def pause(): pass


def resume(): pass





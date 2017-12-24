import game_framework
import title_state
from pico2d import *
name = "StartState"
image = None


def enter():
    global image
    image = load_image('Resource/how_to_play.png')

def exit():
    global image
    del(image)

def update(frame_time):
    pass

def draw(frame_time):
    global image,totalmoney
    clear_canvas()
    image.clip_draw(0, 0, 1600, 900, 500, 400, 1000, 800)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)



def pause(): pass


def resume(): pass





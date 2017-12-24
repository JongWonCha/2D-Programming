import game_framework
from pico2d import *
import fire_state
from global_state import *
import how_to_state
import store_state
import global_state
name = "StartState"
image = None
font = None
logo_time = 0.0
bgm = None


def enter():
    global image, font, bgm
    image = load_image('Resource/title.png')
    font = load_font('Font/ENCR10B.TTF', 60)
    bgm = load_wav('Music/title.wav')
    bgm.set_volume(60)
    bgm.play()

def exit():
    global image, bgm
    del(image)
    del(bgm)

def update(frame_time):
    global logo_time
    if logo_time > 1.0:
        logo_time = 0
    logo_time += 0.01 * frame_time

def draw(frame_time):
    global image,totalmoney
    clear_canvas()
    image.clip_draw(0, 0, 1600, 900, 500, 400, 1000, 800)
    font.draw(20, 150, 'press enter to start', (0, 0, 0))
    font.draw(20, 100, 'press space to how to play', (0, 0, 0))
    font.draw(20, 50, 'press s to store', (0, 0, 0))
    print(global_state.totalmoney)
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(how_to_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            game_framework.change_state(store_state)



def pause(): pass


def resume(): pass





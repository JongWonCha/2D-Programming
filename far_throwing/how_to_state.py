import game_framework
import title_state
from pico2d import *
name = "StartState"
image = None
font = None
bgm = None


def enter():
    global image, font, bgm
    image = load_image('Resource/how_to_play.png')
    font = load_font('Font/ENCR10B.TTF', 50)
    bgm = load_music('Music/store.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()


def exit():
    global image, font, bgm
    del(image)
    del(font)
    del(bgm)

def update(frame_time):
    pass

def draw(frame_time):
    global image,totalmoney, font
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





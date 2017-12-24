import game_framework
from pico2d import *
import title_state
import main_state
import global_state
import random

name = "StartState"
background = None
boy = None
gauge = None
power = 0
MAX_POWER = 100.0
MIN_POWER = 2.0
DELTA = 200.0
font = None


class Boy:
    def __init__(self):
        self.x = 200
        self.y = 200
        self.x_acceleration = 0.0
        self.y_acceleration = 0.0
        self.acceleration_dir = 0
        self.image = load_image('Resource/hero_animation.png')
        self.bgm = load_music('Music/fire.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def update(self, frame_time):
        global power, MAX_POWER, MIN_POWER, DELTA
        if power == 0:
            if self.acceleration_dir == 0:
                self.x_acceleration += DELTA * frame_time
                if self.x_acceleration > MAX_POWER:
                    self.acceleration_dir = 1
            elif self.acceleration_dir == 1:
                self.x_acceleration -= DELTA * frame_time
                if self.x_acceleration < MIN_POWER:
                    self.acceleration_dir = 0
        elif power == 1:
            if self.acceleration_dir == 0:
                self.y_acceleration += DELTA * frame_time
                if self.y_acceleration > MAX_POWER:
                    self.acceleration_dir = 1
            else:
                self.y_acceleration -= DELTA * frame_time
                if self.y_acceleration < 0.0:
                    self.acceleration_dir = 0

    def draw(self):
        self.image.clip_draw(108 * 2, 140, 108, 140, 140, self.y)


class Gauge:
    def __init__(self):
        self.x_power_xpos = 300
        self.x_power_ypos = 200
        self.y_power_xpos = 100
        self.y_power_ypos = 300
        self.image = load_image('Resource/black_square.png')

    def draw(self):
        draw_rectangle(self.x_power_xpos, self.x_power_ypos, self.x_power_xpos + 400, self.x_power_ypos + 30)
        draw_rectangle(self.y_power_xpos, self.y_power_ypos, self.y_power_xpos+ 30, self.y_power_ypos + 400)
        self.image.clip_draw(0, 0, 30, 30, self.x_power_xpos +((400.0 / MAX_POWER) * boy.x_acceleration / 2), self.x_power_ypos + 15,(400.0 / MAX_POWER) * boy.x_acceleration, 30 )
        self.image.clip_draw(0, 0, 30, 30, self.y_power_xpos + 15, self.y_power_ypos + ((400.0 / MAX_POWER) * boy.y_acceleration / 2),30, (400.0 / MAX_POWER) * boy.y_acceleration )




class Background():
    def __init__(self):
        self.x = 0
        self.y = 400
        self.image = load_image('Resource/noon.png')

    def draw(self):
        self.image.clip_draw(0, 0, 2133, 800, self.x + 2133 / 2, self.y)

def enter():
    global background, boy, gauge, font
    boy = Boy()
    background = Background()
    gauge = Gauge()
    font = load_font('Font/ENCR10B.TTF', 50)


def exit():
    global boy, background, gauge,power
    power = 0
    del(boy)
    del(background)
    del(gauge)

def update(frame_time):
    boy.update(frame_time)
    #background.update(frame_time)

def draw(frame_time):

    clear_canvas()
    background.draw()
    gauge.draw()
    boy.draw()
    font.draw(300, 350, 'press space', (random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))
    update_canvas()


def handle_events(frame_time):
    global power
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            power += 1
            if power == 2:
                global_state.x_acceleration = boy.x_acceleration
                global_state.y_accelertaion = boy.y_acceleration
                game_framework.change_state(main_state)


def pause(): pass


def resume(): pass





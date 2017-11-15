import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

boy = None
grass = None
font = None
sky = None
hero = None

class Sky:
    def __init__(self):
        self.x, self.y = 0, 1200
        self.image = load_image('sky.png')

    def draw(self):
        if boy.y > 400:
            self.image.draw(self.x, self.y - (boy.y - 400))
        else:
            self.image.draw(self.x, self.y)





class Grass:
    xpos = 0
    ypos = 300
    def __init__(self):
        self.image = load_image('background_2_.png')

    def draw(self):
        if boy.y > 400:
            self.ypos = 300 - (boy.y - 400)
        else:
            self.ypos = 300
        self.image.draw(self.xpos, self.ypos)
        self.image.draw(self.xpos + 1600, self.ypos)
        draw_rectangle(80, 80, 150, 150)


    def update(self):
        self.xpos -= boy.speed/4
        if self.xpos < -1600:
            self.xpos = 0



class Boy:
    def __init__(self):
        self.x, self.y = 100, 90
        self.speed = 100.0
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1
        self.acc = 20.0
        self.gravity = 0.3

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.y = self.y + self.acc
        self.acc = self.acc - self.gravity
        print(self.acc)
        if self.y < 80 and self.acc < 0:
            self.acc = - 3 * self.acc / 4
            self.speed = 3 * self.speed / 4

    def draw(self):
        if self.y >400:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, 400)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global boy, grass,sky
    boy = Boy()
    grass = Grass()
    sky = Sky()


def exit():
    global boy, grass, sky
    del(boy)
    del(grass)
    del(sky)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)


def update():
    boy.update()
    grass.update()


def draw():
    clear_canvas()
    grass.draw()
    sky.draw()
    boy.draw()
    update_canvas()
    delay(0.01)
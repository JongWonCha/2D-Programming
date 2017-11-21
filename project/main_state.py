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
bear = None


class Bear:
    image = None

    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 120
        self.frame = random.randint(0,7)
        self.move = random.randint(4, 8)
        self.on = 1
        self.frame = 0
        self.fra = 0
        if Bear.image == None:
            Bear.image = load_image('Monster_an.png')

    def update(self):
        self.frame = self.frame + 1
        self.x += -(boy.speed / 4) + (self.move * 4)
        if self.x < -50:
            self.x = 850
        if boy.y < 400:
            self.y = 120
        else:
            self.y = 120 - (boy.y - 400)
        if self.frame == 8:
            self.frame = 0
            self.fra = (self.fra + 1) % 8

    def get_bb(self):
        return self.x  - 20, self.y - 28, self.x + 20, self.y + 28

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.image.clip_draw(self.fra * 55, 0, 55, 57, self.x, self.y)

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


    def update(self):
        self.xpos -= boy.speed/4
        if self.xpos < -1600:
            self.xpos = 0



class Boy:
    def __init__(self):
        self.x, self.y = 100, 120
        self.speed = 100.0
        self.frame = 0
        self.image = load_image('Running.png')
        self.dir = 1
        self.acc = 20.0
        self.gravity = 0.3
        self.fra = 0

    def update(self):
        self.frame = self.frame + 1
        self.y = self.y + self.acc
        self.acc = self.acc - self.gravity
        print(self.acc)
        if self.y < 120 and self.acc < 0:
            self.acc = - 3 * self.acc / 4
            self.speed = 3 * self.speed / 4
        if self.frame == 8:
            self.frame = 0
            self.fra = (self.fra + 1) % 8
        for ba in bear:
            if collide(boy, ba) and boy.acc < 0:
                if boy.acc * boy.acc < 4:
                    boy.acc = 10
                else:
                    boy.acc = - 5 * boy.acc / 6

    def draw(self):
        if self.y < 400:
            self.image.clip_draw(self.fra * 108, 140, 108, 140, self.x, self.y)
            #draw_rectangle(self.x-2, -50 + self.y - 2, self.x + 2, -50 + self.y + 2)
        else:
            self.image.clip_draw(self.fra * 108, 140, 108, 140, self.x, 400)

    def get_bb(self):
        if boy.y < 400:
            return self.x - 30, self.y - 40, self.x + 30, self.y + 40
        else:
            return self.x - 30, 350, self.x + 30, 450

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


def enter():
    global boy, grass,sky,bear
    boy = Boy()
    grass = Grass()
    sky = Sky()
    bear = [Bear() for i in range(10)]


def collide(a, b):
   left_a, bottom_a, right_a, top_a = a.get_bb()
   left_b, bottom_b, right_b, top_b = b.get_bb()
   if left_a > right_b: return False
   if right_a < left_b: return False
   if top_a < bottom_b: return False
   if bottom_a > top_b: return False
   return True


def exit():
    global boy, grass, sky, bear
    del(boy)
    del(grass)
    del(sky)
    del(bear)


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
    for bea in bear:
        bea.update()


def draw():
    clear_canvas()
    grass.draw()
    sky.draw()
    boy.draw()
    boy.draw_bb()
    for bea in bear:
        bea.draw()
    for bea in bear:
        bea.draw_bb()
    update_canvas()
    delay(0.01)
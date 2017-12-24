import game_framework
from pico2d import *
import fire_state
import global_state
from class_file import *
import title_state
import random

boy = None
front_background = None
back_background = None
sky = None
floor_enemy = None
ground = None
helicopter = None
showspeed = None
bomb = None
GRAVITIY = 2500
SPEED = global_state.x_acceleration
NORMALSTATE = 0
HELISTATE = 1
boy_max_height = 600
boy_xposition = 140
floor_enemy_speed = 1
is_game_over = 0
localmoney = 0
rocket = 0


class Boy():
    state = NORMALSTATE
    font = None
    oversound = None
    enemysound = None
    def __init__(self):
        self.x, self.y = 0, 100
        self.rotate = 0
        self.frame = 0.0
        self.hero_image = load_image('Resource/hero_animation.png')
        self.heli_image = load_image('Resource/helicopter.png')
        self.over_image = load_image('Resource/game_over.png')
        self.acceleration = 0.0
        if Boy.font == None:
            Boy.font = load_font('Font/ENCR10B.TTF', 50)
        self.bgm = load_music('Music/bgm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        if Boy.enemysound == None:
            Boy.enemysound = load_wav('Music/jump.wav')
            Boy.enemysound.set_volume(64)
        if Boy.oversound == None:
            Boy.oversound = load_wav('Music/die.wav')
            Boy.oversound.set_volume(64)

    def update(self, frame_time):
        global SPEED, floor_enemy_speed, is_game_over, NORMALSTATE, HELISTATE, GRAVITIY, localmoney
        self.x += SPEED * frame_time
        if Boy.state == NORMALSTATE:
            self.y += self.acceleration * frame_time
            if self.acceleration > -2000:
                self.acceleration -= GRAVITIY * frame_time
            self.frame += 10 * frame_time
            if self.frame > 8: self.frame = 0
            if collide(boy, ground):
                if Boy.state == NORMALSTATE and self.acceleration < 0:
                    self.acceleration = - 3 * self.acceleration / 4
                    SPEED = 3 * SPEED / 4
                    if SPEED < 166:
                        is_game_over = 1
                        self.bgm.set_volume(0)
                        Boy.oversound.play()
            for floor_en in floor_enemy:
                if collide(floor_en, boy):
                    if Boy.state == NORMALSTATE and self.acceleration < 0:
                        self.acceleration = -self.acceleration
                        floor_en.x = 1100
                        SPEED = 5 * SPEED / 6
                        localmoney += 10
                        Boy.enemysound.play()

        elif Boy.state == HELISTATE:
            if collide(boy, ground):
                self.acceleration = 2000.0
                SPEED += 1000
                if SPEED > 3000: SPEED = 3000
                Boy.state = NORMALSTATE
            if Helicopter.timer < 0.0:
                self.y += self.acceleration * frame_time
                self.acceleration -= GRAVITIY * frame_time

        if collide(boy, helicopter) and Boy.state == NORMALSTATE:
            Boy.state = HELISTATE
            #GRAVITIY = 0
            Helicopter.timer = 2.0
            self.acceleration = 0



    def draw(self):
        global localmoney, rocket
        if Boy.state == NORMALSTATE:
            if self.y < boy_max_height:
                self.hero_image.clip_draw(int(self.frame) * 108, boy_xposition, 108, boy_xposition, boy_xposition, self.y)
            else:
                self.hero_image.clip_draw(int(self.frame) * 108, boy_xposition, 108, boy_xposition, boy_xposition, boy_max_height)
        elif Boy.state == HELISTATE:
            if self.y < boy_max_height:
                self.heli_image.draw(boy_xposition, self.y)
            else: self.heli_image.draw(boy_xposition, boy_max_height)
        if is_game_over:
            self.over_image.draw(500, 400)
        Boy.font.draw(400, 780, 'money : $%d'%localmoney, (0, 0, 0))
        Boy.font.draw(400, 740, 'rocket : %d' % rocket, (0, 0, 0))
        Boy.font.draw(400, 700, 'distance : %dm' % (self.x / 10 * 0.3), (0, 0, 0))
        Boy.font.draw(190, 740, 'm/s', (0, 0, 0))
        if self.state == HELISTATE:
            Boy.font.draw(300, 400, 'press space to Bungee', (random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))



    def get_bb(self):
        if Boy.state == NORMALSTATE:
            if boy.y < boy_max_height:
                return boy_xposition - 30, self.y - 50, boy_xposition + 30, self.y + 50
            else:
                return boy_xposition - 30, boy_max_height - 50, boy_xposition + 30, boy_max_height + 50
        elif Boy.state == HELISTATE:
            if boy.y < boy_max_height:
                return boy_xposition - 125, self.y - 70, boy_xposition + 125, self.y + 70
            else:
                return boy_xposition - 125, boy_max_height - 70, boy_xposition + 125, boy_max_height + 70

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Background():
    def __init__(self):
        self.x, self.y  = 0, 400
        self.image = load_image('Resource/noon.png')


    def update(self, frame_time):
        self.x -= SPEED * frame_time
        if self.x < -2100:
            self.x = 2000

    def draw(self):

        if boy.y < boy_max_height:
            self.image.clip_draw(0, 0, 2133, 800, self.x + 2133 / 2, self.y)
        else:
            self.image.clip_draw(0, 0, 2133, 800, self.x + 2133 / 2, self.y - (boy.y - boy_max_height))



class Sky():
    def __init__(self):
        self.x, self.y = 500, 1400
        self.image = load_image('Resource/sky.png')

    def draw(self):
        if boy.y < boy_max_height:
            self.image.draw(0, self.y)
        else:
            self.image.draw(self.x, self.y - (boy.y - boy_max_height))
            self.image.draw(self.x,  (1.5 * self.y) - (boy.y - boy_max_height))
            #self.image.draw(self.x, (3 * self.y) - (boy.y - boy_max_height))

class Ground():
    def __init__(self):
        self.x, self.y = 500, 120

    def get_bb(self):
        return self.x - 500, self.y - 120, self.x + 500, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Floorenemy():
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = 200
        self.frame = random.randint(0, 7)
        self.speed = random.randint(400, 1500)
        self.image = load_image('Resource/floor_enemy_animation.png')
        self.on = 1

    def get_bb(self):
        if self.on == 1:
            return self.x - 15, self.y - 25, self.x + 15, self.y + 25

    def draw_bb(self):
        if self.on == 1:
            draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        if self.on == 1:
            self.x -= (SPEED - self.speed) * frame_time
            if self.x < -200: self.x = 1500
            if self.x > 1500: self.x = -150
            self.frame += 15 * frame_time
            if self.frame > 8: self.frame = 0
            if boy.y < boy_max_height: self.y = 195
            else: self.y = 195 - (boy.y - boy_max_height)

    def draw(self):
        if self.on == 1:
            self.image.clip_draw(int(self.frame) * 54, 0, 54, 57, self.x, self.y)


class Helicopter():
    timer = 0.0
    def __init__(self):
        self.x = random.randint(0, 2000)
        self.y = random.randint(boy_max_height + 200, 1500)
        self.image = load_image('Resource/helicopter.png')
        self.speed = 1000.0
        self.realy = self.y

    def update(self,frame_time):
        self.x -= (SPEED - self.speed) * frame_time
        if self.x < -200:
            self.x = 3000
            self.y = random.randint(700, 2000)
            self.realy = self.y
            self.speed = random.randint(700, 1000)
        if boy.y < boy_max_height:
            self.y = self.realy
        else:
            self.y = self.realy - (boy.y - boy_max_height)
        if Boy.state == HELISTATE:
            Helicopter.timer -= frame_time

    def draw(self):
        self.image.clip_draw(0, 0, 250, 250, self.x, self.y)

    def get_bb(self):
        return self.x - 125, self.y - 70, self.x + 125, self.y + 70

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Showspeed():
    def __init__(self):
        self.x = 50
        self.y = 750
        self.image = load_image('Resource/red_numbers.png')
        self.mps = 0.0
        self.ten = 0 #속도의 십의 자리 변수
        self.one = 0#일의 자리 변수

    def update(self, frame_time):
        global SPEED
        self.mps = SPEED / 10 * 0.3
        self.ten = int(self.mps / 10)
        self.one = int(self.mps % 10)

    def draw(self):
        self.image.clip_draw(self.ten * 93, 0, 83, 120, self.x, self.y)
        self.image.clip_draw(self.one * 93, 0, 83, 120, self.x + 93, self.y)


class Bomb():
    def __init__(self):
        self.image = load_image('Resource/bomb.png')
        self.x = 1500
        self.y = 200
        self.speed = random.randint(600, 800)

    def get_bb(self):
        return self.x - 25, self.y - 45, self.x + 25, self.y + 45

    def draw_bb(self):

        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        global SPEED, high_speed
        if is_game_over == 0:
            self.x -= (SPEED - self.speed) * frame_time
            if self.x < -200: self.x = 1500
            if self.x > 1500: self.x = -150
            if boy.y < boy_max_height:
                self.y = 215
            else:
                self.y = 215 - (boy.y - boy_max_height)
            if collide(boy, bomb) and boy.acceleration < 0 and Boy.state == NORMALSTATE:
                SPEED += 1000
                if SPEED > high_speed: SPEED = high_speed
                boy.acceleration = - 5 * boy.acceleration / 4


    def draw(self):
        self.image.clip_draw(0, 0, 50, 90, self.x, self.y)




def enter():
    global boy, front_background, back_background, SPEED,localmoney, sky, floor_enemy, ground, helicopter, showspeed,is_game_over, bomb, rocket
    boy = Boy()
    bomb = Bomb()
    showspeed = Showspeed()
    back_background = Background()
    front_background = Background()
    floor_enemy = [Floorenemy() for i in range(10)]
    ground = Ground()
    sky = Sky()
    helicopter = Helicopter()
    back_background.x = 2000
    #boy.y = 300
    is_game_over = 0
    SPEED = global_state.x_acceleration * 30
    boy.acceleration = global_state.y_accelertaion * 30
    localmoney = 0
    rocket = global_state.rockets


def exit():
    global boy, front_background, back_background, ground_enemy,sky, floor_enemy, ground, helicopter, showspeed, bomb
    del(bomb)
    del(boy)
    del(front_background)
    del(back_background)
    del(sky)
    del(floor_enemy)
    del(ground)
    del(helicopter)
    del(showspeed)


def update(frame_time):
    global is_game_over
    if is_game_over == 0:
        boy.update(frame_time)
        front_background.update(frame_time)
        back_background.update(frame_time)
        for floor in floor_enemy:
            floor.update(frame_time)
        helicopter.update(frame_time)
    showspeed.update(frame_time)
    bomb.update(frame_time)


def draw(frame_time):
    clear_canvas()
    sky.draw()
    back_background.draw()
    front_background.draw()
    for floor in floor_enemy:
        floor.draw()
    boy.draw()
    helicopter.draw()
    showspeed.draw()
    bomb.draw()
    update_canvas()


def handle_events(frame_time):
    global localmoney, global_state, rocket
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            global_state.totalmoney += localmoney
            print(global_state.totalmoney)
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if Boy.state == NORMALSTATE and rocket >= 1:
                boy.acceleration = -1500
                rocket -= 1
            elif Boy.state == HELISTATE:
                Helicopter.timer = 0.0
                Boy.state = NORMALSTATE
                boy.acceleration = -1500

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def pause(): pass


def resume(): pass





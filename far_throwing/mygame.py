import platform
import os
if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

import game_framework
from pico2d import *
import start_state
import fire_state
open_canvas(1000, 800, 0)
game_framework.run(start_state)
close_canvas()

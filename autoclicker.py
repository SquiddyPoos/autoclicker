import mouse
import keyboard
import multiprocessing as mp
from functools import partial
import time

class Autoclicker():

    def __init__(self):
        self.delay = 1
        self.button = "left"
        self.autoclick_task = None

    def set_cps(self, cps):
        self.delay = 1 / cps

    def set_button(self, button):
        self.button = button

    def start_autoclick(self):
        if self.autoclick_task is not None:
            raise AutoclickError("Autoclicker already running!")
        self.autoclick_task = mp.Process(target=self.click, args=(self.delay, self.button))
        self.autoclick_task.start()

    def stop_autoclick(self):
        if self.autoclick_task is None or self.autoclick_task == "Hold":
            raise AutoclickError("Autoclicker is not running!")
        self.autoclick_task.kill()
        self.autoclick_task = None

    def hold_button(self):
        if self.autoclick_task is not None:
            raise AutoclickError("Autoclicker already running!")
        mouse.hold(button = self.button)
        self.autoclick_task = "Hold"

    def release_button(self):
        if self.autoclick_task is None or type(self.autoclick_task) != type(''):
            raise AutoclickError("Autoclicker is not running!")
        mouse.release(button = self.button)
        self.autoclick_task = None

    def click(self, delay, button):
        while True:
            time.sleep(delay)
            #mouse.click(button = button)
            print("Click")


class AutoclickError(Exception):
    pass
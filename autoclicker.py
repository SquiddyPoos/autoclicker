import mouse
import keyboard
import asyncio

class AutoclickManager():

    def __init__(self, cps, button):
        self.delay = 1 / cps
        self.button = button
        self.autoclick_task = None

    def set_cps(self, cps):
        self.delay = 1 / cps

    def set_button(self, button):
        self.button = button

    def start_autoclick(self):
        if self.autoclick_task is not None:
            raise AutoclickError("Autoclicker already running!")
        self.autoclick_task = asyncio.create_task(self.click())

    def stop_autoclick(self):
        if self.autoclick_task is None or self.autoclick_task == "Hold":
            raise AutoclickError("Autoclicker is not running!")
        self.autoclick_task.cancel()
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

    def click(self):
        while True:
            await asyncio.sleep(self.delay)
            mouse.click(button = self.button)


class AutoclickError(Exception):
    pass
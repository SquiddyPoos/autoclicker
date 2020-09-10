from tkinter import *
from tkinter.font import *
from autoclicker import Autoclicker, AutoclickError

class App(object):

    def __init__(self):
        self.root = Tk()
        self.autoclicker = Autoclicker()
        self.default_colour = self.root["bg"]
        self.root.geometry("500x600")
        self.setup_gui()
        self.root.mainloop()

    def setup_gui(self):
        title_font = Font(family="TkDefaultFont", size=25)
        title = Label(self.root, text = "Autoclicker", font = title_font)
        title.place(relx = 0.5, y = 15, anchor = N)
        self.km = IntVar()
        rb1 = Radiobutton(self.root, text = "Mouse", variable = self.km, value = 0, command = self.set_disabled, activebackground = self.default_colour)
        rb1.place(x = 10, rely = 0.15, anchor = W)
        rb2 = Radiobutton(self.root, text = "Keyboard", variable = self.km, value = 1, command = self.set_disabled, activebackground = self.default_colour)
        rb2.place(x = 10, rely = 0.5, anchor = W)
        frame1 = Canvas(self.root, relief = FLAT)
        frame1.place(relx = 0.05, rely = 0.15, y = 13, relwidth = 0.9, relheight = 0.3, anchor = NW)
        self.init_mouse(frame1)
        frame2 = Canvas(self.root, bd = 2, relief = RIDGE)
        frame2.place(relx = 0.05, rely = 0.5, y = 13, relwidth = 0.9, relheight = 0.3, anchor = NW)
        self.init_kb(frame2)

    def init_mouse(self, canvas):
        self.root.update()
        w = canvas.winfo_width()
        h = canvas.winfo_height()
        canvas.create_rectangle(0, 0, w, h, width = 4)
        canvas.create_line(0, 35, w, 35, width = 1)
        canvas.create_line(w/2, 0, w/2, 35, width = 1)
        self.hold_click = IntVar()
        hold = Radiobutton(canvas, text = "Hold", variable = self.hold_click, value = 0, command = self.swap_frame, activebackground = self.default_colour)
        hold.place(relx = 0.25, y = 7, anchor = N)
        click = Radiobutton(canvas, text = "Click", variable = self.hold_click, value = 1, command = self.swap_frame, activebackground = self.default_colour)
        click.place(relx = 0.75, y = 7, anchor = N)
        #self.frame_mouse = Frame(canvas)
        #self.frame_mouse.place(relwidth = 1, relheight = 0.8, rely = 0.2)

    def init_kb(self, canvas):
        pass

    def set_disabled(self):
        pass

    def swap_frame(self):
        pass


if __name__ == "__main__":
    app = App()
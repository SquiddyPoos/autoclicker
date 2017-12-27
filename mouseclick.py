import win32api, win32con, win32gui, time, keyboard, mpmath
def click():
    flags, hcursor, (x,y) = win32gui.GetCursorInfo()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

pressing = 0
lastclick = mpmath.mpf(1)

while True:
    if keyboard.is_pressed('return') and lastclick >= 1:
        if pressing == 0:
            pressing = 1
        else:
            pressing = 0
        lastclick = mpmath.mpf(0)
    if pressing == 1:
        click()
    lastclick = mpmath.fadd(lastclick,mpmath.mpf(.001),exact = True)
    time.sleep(.01)
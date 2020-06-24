import win32api, win32con, win32gui, time, keyboard, threading
from functools import partial
def click():
	flags, hcursor, (x,y) = win32gui.GetCursorInfo()
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

pressing = 0
curr_interval = 10
interval_cycle = [50, 25, 10, 5, 2.5, 1, .5, .1, .05, .01, .001, .0001, .00001, 1e-06, 1e-07, 1e-08, 1e-09, 1e-10, 0]
index = 2

def autoclick():
	global curr_interval
	if pressing == 1:
		click()
	threading.Timer(curr_interval/1000, autoclick).start()

threading.Timer(0, autoclick).start()
print("Alt-C to toggle, Alt-I to toggle speed")
print("Current click speed: 1 click per "+str(curr_interval)+" ms")

def check_for_input(is_pressing):
	press = keyboard.is_pressed('alt+c')
	press_change_interval = keyboard.is_pressed('alt+i')
	global pressing, curr_interval, index, interval_cycle
	if press and not is_pressing:
		if pressing == 0:
			print("Autoclick: On")
			pressing = 1
		else:
			print("Autoclick: Off")
			pressing = 0
		is_pressing = True
	elif press_change_interval and not is_pressing:
		index += 1
		if (index >= len(interval_cycle)):
			index = 0
		curr_interval = interval_cycle[index]
		print("Current click speed: 1 click per "+str(curr_interval)+" ms")
		is_pressing = True
	elif not press and not press_change_interval:
		is_pressing = False
	threading.Timer(0, partial(check_for_input, is_pressing)).start()

check_for_input(0)

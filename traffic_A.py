from sense_hat import SenseHat
import time
sense = SenseHat()
state = 0
w = (255,255,255)
r = (255,0,0)
g = (0,255,0)
y = (255,255,0)
n = (0,0,0)
red = [
 n, n, n, r, r, n, n, n,
 n, n, n, r, r, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]
red_yellow = [
 n, n, n, r, r, n, n, n,
 n, n, n, r, r, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]

yellow = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]
green = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, g, g, n, n, n,
 n, n, n, g, g, n, n, n
 ]

def xy_state(duration,szin):
        sense.set_pixels(szin)
        time.sleep(duration)
        sense.clear()

def out_of_order_state():
    sense.set_pixels(yellow)
    time.sleep(0.5)
    sense.clear()
    time.sleep(0.5)

def set_state():
    global state
    # state variable has been defined outside
    if state < 3:
        state += 1
    elif state == 3:
        state = 0
    else:
        pass

def button_event(event):
    global state
    if event.action == 'released':
        if state != 4:
            state = 4
        else:
            state = 3
    if event.action == 'up':
        if state != 5:
            state = 5
        else:
            state = 3
    if event.action == 'down':
        if state != 6:
            state = 6
        else:
            state = 3
        

sense.stick.direction_middle = button_event

def main():
    global state
    while True:
        if state == 0:
            xy_state(3,red)
        elif state == 1:
            xy_state(1,red_yellow)
        elif state == 2:
            xy_state(2,green)
        elif state == 3:
            xy_state(1,yellow)
        elif state == 5:
            time.sleep(0.3)
        elif state == 6:
            time.sleep(0.3)
        else:
            out_of_order_state()   
        set_state()
        
main()







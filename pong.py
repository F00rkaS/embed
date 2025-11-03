from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()
speed = 0.7
basket = [7,4]  # kosár pozíciója
score = 0

# színek
w = (0,0,0)
r = (255,0,0)
b = (0,0,255)

# üres játékmező
game_space = [w]*64

# kosár inicializálása (két kék pixel alul)
game_space[7*8+basket[1]] = b
game_space[7*8+basket[1]-1] = b

def update_space(x, y, colour):
    """Frissíti egy pixel színét a megadott koordinátán."""
    p = 8 * x + y
    game_space[p] = colour
    sense.set_pixels(game_space)

def left(event):
    if event.action == 'pressed':
        if basket[1] - 1 > 0:
            update_space(7, basket[1], w)
            basket[1] -= 1
            update_space(7, basket[1]-1, b)
            update_space(7, basket[1], b)

def right(event):
    if event.action == 'pressed':
        if basket[1] + 1 < 8:
            update_space(7, basket[1]-1, w)
            basket[1] += 1
            update_space(7, basket[1]-1, b)
            update_space(7, basket[1], b)

sense.stick.direction_left = left
sense.stick.direction_right = right

sense.clear()
sense.set_pixels(game_space)
game_alive = True

# kezdő labda pozíció és irány
x = 0
y = random.randint(0,7)
dx = random.choice([-1, 1])  # oldalirány
dy = 1  # függőleges irány (1 = lefelé, -1 = felfelé)
update_space(x, y, r)

while game_alive:
    # sebesség a pontszámtól függően
    if score < 5:
        sleep(0.5)
    elif score < 10:
        sleep(0.45)
    elif score < 15:
        sleep(0.4)
    elif score < 20:
        sleep(0.35)
    elif score < 30:
        sleep(0.3)
    elif score < 40:
        sleep(0.25)
    elif score < 50:
        sleep(0.2)
    else:
        sleep(0.15)

    # jelenlegi pozíció törlése
    update_space(x, y, w)

    # új pozíció kiszámítása
    x += dy
    y += dx

    # oldalirányú visszapattanás
    if y < 0:
        y = 0
        dx = 1
    elif y > 7:
        y = 7
        dx = -1

    # ha a labda eléri a kosár sort (x == 7)
    if x == 7:
        if y == basket[1] or y == basket[1]-1:
            # eltalálta a kosarat → visszapattan
            score += 1
            dy = -1  # visszafelé indul (felfelé)
            # A labda most a kosár fölött folytatja (ne helyezze újra véletlenül)
            x = 6    # közvetlenül a kosár fölé tesszük
        else:
            # nem találta el a kosarat → game over
            game_alive = False
            break

    # ha a labda eléri a tetejét → ismét lefelé esik
    if x <= 0:
        x = 0
        dy = 1

    # új pozíció kirajzolása
    update_space(x, y, r)

sense.clear()
sense.show_message('Game over!', scroll_speed=0.05, back_colour=w)
sense.show_message('Score: ' + str(score), scroll_speed=0.07, back_colour=w)

from pygame.display import set_mode
from pygame.image import load
from pygame import FULLSCREEN

from os import popen

# screen with pc screen proportions
screen = popen("xrandr -q -d :0").readlines()[0]
w = int(screen.split()[7])
h = int(screen.split()[9][:-1])

win = set_mode((w, h), FULLSCREEN)

def reset_win(win):
	win.fill((0,0,0))
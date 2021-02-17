import pygame as py

from random import randint

from Win.Win import win, reset_win
from Maps.Maps import Map

py.init()
game_ON = True

map = Map()

while game_ON:	
	reset_win(win)
	for event in py.event.get():
		# To quit push esc
		if event.type == py.QUIT or (\
		   event.type == py.KEYDOWN and event.key == py.K_ESCAPE\
		):
			game_ON = False
			
	map.draw(win)	
			
	py.display.flip()
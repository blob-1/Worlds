import pygame as py

from random import randint

from Win.Win import win, w, h, reset_win

py.init()
game_ON = True

while game_ON:	
	for event in py.event.get():
		# To quit push esc
		if event.type == py.QUIT or (\
		   event.type == py.KEYDOWN and event.key == py.K_ESCAPE\
		):
			game_ON = False
			
	py.display.flip()
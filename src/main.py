import pygame as py

from random import randint

from Win.Win import win, reset_win
from Maps.Maps import Map

py.init()
game_ON = True

MapType = "heightMap"
map = Map(None, Perlin = 20)

while game_ON:	
	reset_win(win)
	for event in py.event.get():
		# To quit push esc
		if event.type == py.QUIT:
			game_ON = False
		   
		if event.type == py.KEYDOWN:
			if event.key == py.K_ESCAPE:
				game_ON = False
			elif event.key == py.K_KP1:
				MapType = "heightMap"
			elif event.key == py.K_KP2:
				MapType = "continent"
			
	map.draw(win, MapType)	
			
	py.display.flip()
import pygame as py

from random import randint, seed

from Win.Win import win, reset_win
from Maps.Maps import Map

py.init()
game_ON = True
moussePresed = False

seed(1000)
MapType = "heightMap"
map = Map(None, Perlin = 20)
shift = 0

while game_ON:	
	# events related to keyboard
	for event in py.event.get():
		# To quit push esc
		if event.type == py.QUIT:
			game_ON = False
		   
		elif event.type == py.KEYDOWN:
			if event.key == py.K_ESCAPE:
				game_ON = False
			elif event.key == py.K_KP1:
				MapType = "heightMap"
			elif event.key == py.K_KP2:
				MapType = "continent"
	
	#events related to mousse
	if py.mouse.get_pressed()[0] == 1 and not moussePresed:
		moussePresed = True
		mousePos = py.mouse.get_rel()[0]
	elif py.mouse.get_pressed()[0] == 0 and moussePresed:
		moussePresed = False
	if moussePresed:
		shift = shift+py.mouse.get_rel()[0]
	
	# actual drawing
	map.draw(win, MapType, shift)
	py.display.flip()
	reset_win(win)
	
	

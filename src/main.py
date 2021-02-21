import pygame as py

from random import seed
from Maps.MapDisplay import MapDisplay
from Maps.Maps import Map
from Win.Win import win, reset_win

seed(1000)

mapDisplay = MapDisplay([Map(None, Perlin = 20), Map(None, Perlin = 20), Map(None, Perlin = 20)])

py.init()

gameON = True
while gameON:
	# events related to keyboard
	events = py.event.get()
	for event in events:
		# To quit click the cross or push esc
		if event.type == py.QUIT:
			gameON = False
			break
		elif event.type == py.KEYDOWN:
			if event.key == py.K_ESCAPE:
				gameON = False
				break
			
	mapDisplay.draw(win, events)

	py.display.flip()
	# reset_win(win)
	
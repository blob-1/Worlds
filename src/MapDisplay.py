import pygame as py

class MapDisplay():
	def __init__(self):
		self.__visible = True
		self.__mapType = "continent"
		self.__shift = 0
		self.__moussePresed = False

	def __show(self):
		self.__visible = True
		
	def __hide(self):
		self.__visible = False
		self.__mapType = "continent"
		self.__shift = 0
		self.__moussePresed = False

	def draw(self, map, win, events):
		# events related to keyboard
		for event in events:   
			if event.type == py.KEYDOWN:
				if event.key == py.K_KP1:
					self.__mapType = "continent"
				elif event.key == py.K_KP2:
					self.__mapType = "heightMap"
				elif event.key == py.K_KP8:
					self.__show()
				elif event.key == py.K_KP9:
					self.__hide()
					return 0
	
		if self.__visible:	
			#events related to mousse
			# move the map !
			if py.mouse.get_pressed()[0] == 1 and not self.__moussePresed:
				self.__moussePresed = True
				mousePos = py.mouse.get_rel()[0]
			elif py.mouse.get_pressed()[0] == 0 and self.__moussePresed:
				self.__moussePresed = False
			if self.__moussePresed:
				self.__shift = self.__shift+py.mouse.get_rel()[0]
				
				while self.__shift > win.get_width():
					self.__shift = self.__shift - win.get_width()
				while self.__shift < 0:
					self.__shift = self.__shift + win.get_width()
			
			# actual drawing
			map.draw(win, self.__mapType, self.__shift)
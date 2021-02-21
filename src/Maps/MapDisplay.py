import pygame as py

class MapDisplay():
	def __init__(self, Maps):
		self.__visible = True
		self.__mapType = "continent"
		self.__moussePresed = False
		
		self.__Maps = Maps
		self.__nbMaps = len(Maps)
		self.__Shifts = []
		for maps in self.__Maps:
			self.__Shifts.append([0,0])
		self.__activeMap = 0

	def __show(self):
		self.__visible = True
		
	def __hide(self):
		self.__visible = False
		self.__mapType = "continent"
		self.__moussePresed = False

	def draw(self, win, events):
		# events related to keyboard
		for event in events:   
			if event.type == py.KEYDOWN:
				# show or not the maps
				if event.key == py.K_KP8:
					self.__show()
				elif event.key == py.K_KP9:
					self.__hide()
					return 0
				# change the view type
				elif event.key == py.K_KP1:
					self.__mapType = "continent"
				elif event.key == py.K_KP2:
					self.__mapType = "continent2"		
				elif event.key == py.K_KP3:
					self.__mapType = "heightMap"
				# map selection
				elif event.key == 275: # right arrow
					self.__activeMap = self.__activeMap + 1
					if self.__activeMap >= self.__nbMaps:
						self.__activeMap = 0
				elif event.key == 276: # left arrow
					self.__activeMap = self.__activeMap - 1	
					if self.__activeMap <= -1:
						self.__activeMap = self.__nbMaps - 1
	
		if self.__visible:	
			#events related to mousse
			# move the map !
			if py.mouse.get_pressed()[0] == 1 and not self.__moussePresed:
				self.__moussePresed = True
				mousePos = py.mouse.get_rel()
			elif py.mouse.get_pressed()[0] == 0 and self.__moussePresed:
				self.__moussePresed = False
			if self.__moussePresed:
				mousePos = py.mouse.get_rel()
				self.__set_Xshift(win, mousePos[0])
				self.__set_Yshift(win, mousePos[1])
			
			# actual drawing
			self.__get_map().draw(win, self.__mapType, self.__get_shift())
			
	def __get_shift(self):
		return self.__Shifts[self.__activeMap]	
		
	def __set_Xshift(self, win, shift):
		self.__Shifts[self.__activeMap][0] = self.__get_shift()[0]+shift
		while self.__get_shift()[0] > win.get_width():
			self.__Shifts[self.__activeMap][0] = self.__get_shift()[0] - win.get_width()
		while self.__get_shift()[0] < 0:
			self.__Shifts[self.__activeMap][0] = self.__get_shift()[0] + win.get_width()
		
	def __set_Yshift(self, win, shift):
		self.__Shifts[self.__activeMap][1] = self.__get_shift()[1]+shift
		while self.__get_shift()[1] > win.get_height():
			self.__Shifts[self.__activeMap][1] = self.__get_shift()[1] - win.get_height()
		while self.__get_shift()[1] < 0:
			self.__Shifts[self.__activeMap][1] = self.__get_shift()[1] + win.get_height()
		
	def __get_map(self):
		return self.__Maps[self.__activeMap]
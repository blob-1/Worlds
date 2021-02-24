from pygame.draw import line
from math import ceil

class River():
	def __init__(self, start, end):
		self.__start = start
		self.__end = end
		
	def draw(self, surface, x, y, w, h):
		start_pos = self.__get_point(self.__start, x, y, w, h)
		end_pos = self.__get_point(self.__end, x, y, w, h)
		line(surface, (56,21,164), start_pos, end_pos, 1)
		
	def __get_point(self, type, x, y, w, h):
		if  type[0] == "t":
			X = x
		elif type[0] == "c":
			X = ceil(x+w/2)
		else:
			X = x+w
			
		if type[1] == "l":
			Y = y
		elif type[1] == "c":
			Y = ceil(y+h/2)
		else:
			Y = y+h
			
		return((X,Y))
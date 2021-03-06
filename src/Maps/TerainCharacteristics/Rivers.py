from pygame.draw import aaline
from math import ceil

from .Characteristic import Characteristic

class River(Characteristic):
	def __init__(self, start, end):
		self.__start = start
		self.__end = end
		
	def draw(self, surface, x, y, w, h):
		start_pos = self.__get_point(self.__start, x, y, w, h)
		end_pos = self.__get_point(self.__end, x, y, w, h)
		if start_pos[0] > end_pos[0]:
			tmp = start_pos
			start_pos = end_pos
			end_pos = tmp	

		aaline(surface, (56,21,200), start_pos, end_pos, 1)
		
	def __get_point(self, type, x, y, w, h):
		if type[0] == "t":
			pass
		elif type[0] == "b":
			x = x+w
		else:
			x = x+w/2
			
		if type[1] == "l":
			pass
		elif type[1] == "r":
			y = y+h
		else:
			y = y+h/2		
			
		return((x,y))
from pygame.draw import aaline
from .Characteristic import Characteristic

class OceanCurrent(Characteristic):
	def __init__(self, type = "neutral"):
		self.set_color(type)
		
	def draw(self, surface, x, y, w, h):
		aaline(surface, self.__color, (x, y+int(h/2)), (x+int(w/2), y+int(h/2)), 1)
		
	def set_color(self, type):
		if type == "cold":
			self.__color = (36,10,220)
		if type == "hot":
			self.__color = (220,10,36)
		else:
			self.__color = (0,0,0)
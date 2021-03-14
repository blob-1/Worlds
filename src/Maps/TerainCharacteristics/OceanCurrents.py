from pygame.draw import aaline
from .Characteristic import Characteristic
from math import pi, cos, sin

class OceanCurrent(Characteristic):
	def __init__(self, type = "neutral"):
		self.set_color(type)
		self.__arrow = arrow(self.__color)
		
	def draw(self, surface, x, y, w, h): self.__arrow.draw(surface, x, y, w, h)
		
	def set_color(self, type):
		if type == "cold":
			self.__color = (36,10,220)
		if type == "hot":
			self.__color = (220,10,36)
		else:
			self.__color = (0,0,0)
			
class arrow(Characteristic):
	def __init__(self, color, angle = 0):
		self.__color = color
		self.__angle = angle
		
	def reOrient(self, orientation):self.__orientation = orientation
	def set_color(self, color): self.__color = color
	
	def draw(self, surface, x, y, w, h):
		start = ( x,          y+int(h/2) )
		end   = ( x+w,        y+int(h/2) )
		
		TopS  = ( x+int(w/2), y+int(h/4) )
		TopE  = ( x+w,        y+int(h/2) )
		
		BotS  = ( x+int(w/2), y+int(3*h/4) )
		BotE  = ( x+w,        y+int(h/2) )
		
		Center = ( x+int(w/2), y+int(h/2) )
		
		aaline(surface, self.__color, self.rotate(start, Center, self.__angle), self.rotate(end,  Center, self.__angle), 1)
		aaline(surface, self.__color, self.rotate(TopS,  Center, self.__angle), self.rotate(TopE, Center, self.__angle), 1)
		aaline(surface, self.__color, self.rotate(BotS,  Center, self.__angle), self.rotate(BotE, Center, self.__angle), 1)
		
	def rotate(self, Point, Center, angle):
		angle = angle * (pi / 180)
		x = Point[0]-Center[0]
		y = Point[1]-Center[1]
		
		return( ((x*cos(angle)+y*sin(angle)+Center[0]), (-x*sin(angle)+y*cos(angle)+Center[1])) )
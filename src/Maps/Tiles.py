from random import randint

class Tile():
	def __init__(self, height = None):
		if height != None:
			self.__height = height
		else:
			self.__height = randint(0, 100) # percentage of maximum height in order to be simple !
		
	def get_height(self): return self.__height
	def set_height(self, height): self.__height = height
	
	def draw(self, surface, x, y, w, h):
		grayscale = int((self.__height*255)/100)
		surface.fill((grayscale, grayscale, grayscale), (x, y, w, h))
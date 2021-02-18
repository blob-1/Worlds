from random import randint

class Tile():
	def __init__(self, height = None):
		if height != None:
			self.__height = height
		else:
			self.__height = randint(0, 100) # percentage of maximum height in order to be simple !
		
	def get_height(self): return self.__height
	def set_height(self, height): self.__height = height
	
	def draw(self, surface, x, y, w, h, type = "heightMap"):
		if type == "heightMap":
			grayscale = int((self.__height*255)/100)
			surface.fill((grayscale, grayscale, grayscale), (x, y, w, h))
		elif type == "continent":
			if self.__height < 10:
				color = (10, 5, 71)	
			elif self.__height < 25:
				color = (27, 21, 112)
			elif self.__height < 35:
				color = (60, 53, 158)
			elif self.__height < 50:
				color = (104, 97, 198)
			elif self.__height < 65:
				color = (252, 208, 146)
			elif self.__height < 70:
				color = (216, 185, 140)
			elif self.__height < 85:
				color = (170, 140, 99)
			elif self.__height < 90:
				color = (112, 55, 6)
			else:
				color = (102, 30, 0)
			
			surface.fill(color, (x, y, w, h))
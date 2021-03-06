from random import randint
from pygame.draw import line

class Tile():
	def __init__(self, height = None):
		if height != None:
			self.__height = height
		else:
			self.__height = randint(0, 100) # percentage of maximum height in order to be simple !
			
		self.__region = None
		self.__subRegion = None
		
		self.__caracteristics = []
		
	def get_height(self): return self.__height
	def set_height(self, height): self.__height = height
	
	def draw(self, surface, x, y, w, h, type = "heightMap"):
		if type == "continent":
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
			elif self.__height < 75:
				color = (216, 185, 140)
			elif self.__height < 85:
				color = (170, 140, 99)
			elif self.__height < 90:
				color = (112, 55, 6)
			else:
				color = (102, 30, 0)
				
		elif type == "region":
			color = self.__region.getColor()
			
		elif type == "subRegion":
			color = self.__subRegion.getColor()

		else:
			grayscale = int((self.__height*255)/100)
			color = (grayscale, grayscale, grayscale)
			
		surface.fill(color, (x, y, w, h))	
	
	def drawCharacteristics(self, surface, x, y, w, h, type = "heightMap"):
		if type != "heightMap":
			for chars in self.__caracteristics:
				chars.draw(surface, x, y, w, h)
			
	def regionalize(self, region):self.__region = region
	def getRegion(self): return self.__region	
	
	def subRegionalize(self, subRegion):self.__subRegion = subRegion
	def getSubRegion(self): return self.__subRegion
	
	def __gt__(self, other):
		h1 = self.__height
		h2 = other.get_height()
		if h1 > h2: return True
		elif h1 < h2: return False
		else: return randint(0,1)
		
	def addCharacteristic(self, chars):
		self.__caracteristics.append(chars)
		
	def getCharacteristics(self):return self.__caracteristics
		
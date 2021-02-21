from .Regions import Region
from random import randint

class Continent(Region):
	def __init__(self):
		Region.__init__(self)
		
		self._color = (randint(50,200), randint(50,200), randint(50, 200))
		
	def addTile(self, tile):
		if tile[0].get_height() >= 50 and not tile[0].getRegionalized():
			Region.addTile(self, tile)
			return True
		return False
	
	# test if the first tile is of the right type then catches all of the ones that are of the same type and connected !
	def generate(self, Map, i, j, tile):
		if self.addTile((tile, i, j)):	
			for tile in self._Tiles:
				for neig in Map.getNeibourgs(tile[1], tile[2], returnIndicises = True):
					self.addTile(neig)
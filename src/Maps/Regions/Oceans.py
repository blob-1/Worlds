from .Regions import Region
from .Coasts  import Coast
from .DeepSeas import DeepSea

class Ocean(Region):
	def __init__(self):
		Region.__init__(self)
		
		self._color = (50, 84, 198, 64)		
		
	def addTile(self, tile):
		if tile[0].get_height() < 50 and not tile[0].getRegion():
			Region.addTile(self, tile)
			return True
		return False
	
	# test if the first tile is of the right type then catches all of the ones that are of the same type and connected !	
	def generate(self, Map, i, j, tile):
		if self.addTile((tile, i, j)):	
			for tile in self._Tiles:
				for neig in Map.getNeibourgs(tile[1], tile[2], returnIndicises = True):
					self.addTile(neig)
					
			self.__Zones = []
			for tile in self._Tiles:
				zone = Coast()
				if not zone.addTile(tile):
					zone = DeepSea()
					if not zone.addTile(tile):
						continue
				self.__Zones.append(zone.generate(Map, tile))
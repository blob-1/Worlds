from .Regions import Region

class SubRegion(Region):
	def __init__(self):
		if type(self) is SubRegion:
			raise Exception('SubRegion is an abstract class and cannot be instantiated directly')	
	
		Region.__init__(self)
		
		self._color = (10, 5, 71, 64)	
		self._characteristics = []
		
	def addTile(self, tile):
		self._Tiles.append(tile)
		tile[0].subRegionalize(self)

	def _addCharacteristics(self, Map):pass
		
	# test if the first tile is of the right type then catches all of the ones that are of the same type and connected !
	def generate(self, Map, tile):
		for tile in self._Tiles:
			for neig in Map.getNeibourgs(tile[1], tile[2], returnIndicises = True):
				self.addTile(neig)
					
		self._Tiles.sort(key=lambda x:x[0], reverse = True)
		self._addCharacteristics(Map)
					
from .Regions import Region

class SubRegion(Region):
	def __init__(self):
		Region.__init__(self)
		
		self._color = (10, 5, 71, 64)	
		
	def addTile(self, tile):
		self._Tiles.append(tile)
		tile[0].subRegionalize(self)
		
	# test if the first tile is of the right type then catches all of the ones that are of the same type and connected !
	def generate(self, Map, tile):
		if self.addTile(tile):	
			for tile in self._Tiles:
				for neig in Map.getNeibourgs(tile[1], tile[2], returnIndicises = True):
					self.addTile(neig)
class Region():
	def __init__(self):
		self._Tiles = []
		if type(self) is Region:
			raise Exception('Region is an abstract class and cannot be instantiated directly')

		self._color = (0,0,0)
		
	def getTiles(self): return self._Tiles
	def addTile(self, tile):
		self._Tiles.append(tile)
		tile[0].regionalize(self)
		
	def generate(self, Map, i, j, tile): pass
	
	def getColor(self): return self._color
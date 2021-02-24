from .SubRegions import SubRegion

class Plain(SubRegion):
	def __init__(self):
		SubRegion.__init__(self)
		
		self._color = (10, 128, 48, 64)
		
	def addTile(self, tile):
		if tile[0].get_height() < 65 and tile[0].get_height() >= 50 and not tile[0].getSubRegion():
			SubRegion.addTile(self, tile)
			return True
		return False
from .SubRegions import SubRegion

class Coast(SubRegion):
	def __init__(self):
		SubRegion.__init__(self)
		
		self._color = (60, 53, 158, 64)
		
	def addTile(self, tile):
		if tile[0].get_height() > 25 and tile[0].get_height() < 50 and not tile[0].getSubRegion():
			SubRegion.addTile(self, tile)
			return True
		return False
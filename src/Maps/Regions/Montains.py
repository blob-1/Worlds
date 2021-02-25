from .SubRegions import SubRegion
from ..TerainCharacteristics.Sources import Source
from ..TerainCharacteristics.Rivers import River
from ..TerainCharacteristics.Lacs import Lac
from random import randint

class Montain(SubRegion):
	def __init__(self):
		SubRegion.__init__(self)
		
		self._color = (170, 140, 99, 64)
		
	def addTile(self, tile):
		if tile[0].get_height() >= 65 and not tile[0].getSubRegion():
			SubRegion.addTile(self, tile)
			return True
		return False

	def _addCharacteristics(self, Map):
		for c in range(randint(0, int(len(self._Tiles)/10))):
			i = randint(0, int(len(self._Tiles)-1))
			self._Tiles[i][0].addCharacteristic(Source)
		
			currentTile = self._Tiles[i]
		
			Directions = ["tl", "tc", "tr", "cl", "cr", "bl", "bc", "br"]
			direction1 = "cc"

			while True:
				next = Map.getNeibourgs(currentTile[1], currentTile[2], returnIndicises = True)
				nextTile = next[0]
				for i, tile in enumerate(next):
					if nextTile[0].get_height() >= tile[0].get_height():
						nextTile = tile
						direction2 = Directions[i]
						indice = 7-i
				
				currentTile[0].addCharacteristic(River(direction1, direction2))
				direction1 = Directions[indice]
										
				if nextTile[0].get_height() > currentTile[0].get_height() or nextTile[0].get_height() < 50:break
				currentTile = nextTile
				
			if nextTile[0].get_height() >= 50:
				nextTile[0].addCharacteristic(River(direction1, "cc"))
				nextTile[0].addCharacteristic(Lac)
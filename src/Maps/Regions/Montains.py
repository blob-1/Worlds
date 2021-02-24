from .SubRegions import SubRegion
from ..TerainCharacteristics.Sources import Source
from ..TerainCharacteristics.Rivers import River
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
		
			direction = "cc"
			currentTile = self._Tiles[i]
			next = sorted(Map.getNeibourgs(self._Tiles[i][1], self._Tiles[i][2], returnIndicises = True))[0]
		
			stop = False
			while True:
				if currentTile[1] < next[1]:
					if currentTile[2] < next[2]:
						currentTile[0].addCharacteristic(River(direction, "tl"))
						direction = "br"
					elif currentTile[2] == next[2]:
						currentTile[0].addCharacteristic(River(direction, "tc"))
						direction = "bc"
					else:
						currentTile[0].addCharacteristic(River(direction, "tr"))
						direction = "bl"
				elif currentTile[1] == next[1]:
					if currentTile[2] < next[2]:
						currentTile[0].addCharacteristic(River(direction, "cr"))						
						direction = "cl"
					else:
						currentTile[0].addCharacteristic(River(direction, "cl"))					
						direction = "cr"
				else:
					if currentTile[2] < next[2]:					
						currentTile[0].addCharacteristic(River(direction, "bl"))
						direction = "tr"					
					elif currentTile[2] == next[2]:
						currentTile[0].addCharacteristic(River(direction, "bc"))
						direction = "tc"
					else:
						currentTile[0].addCharacteristic(River(direction, "br"))
						direction = "tl"
				
				currentTile = next
				next = sorted(Map.getNeibourgs(next[1], next[2], returnIndicises = True))[0]
				if stop : break
				if not (next[0].get_height() < currentTile[0].get_height() and next[0].get_height() >= 50):stop = True
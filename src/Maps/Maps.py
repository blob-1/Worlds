from random import randint

from .Tiles import Tile

class Map():
	def __init__(self, tiles = None, x = 1920, y = 1080):
		if tiles != None:
			self.__tiles  = tiles
			self.__height = len(tiles)
			self.__width  = len(tiles[0])
		else:
			self.__tiles = []
			for i in range(x):
				self.__tiles.append([])
				for j in range(y):
					self.__tiles[i].append(Tile())
			self.__height = y
			self.__width  = x
					
	def get_tiles(self): return self.__tiles
	def set_tiles(self, tiles): self.__tiles = tiles
	
	def draw(self, surface):
		tile_height = surface.get_height() / self.__height
		tile_width  = surface.get_width() / self.__width

		x = 0
		for row in self.__tiles:
			y = 0
			for tile in row:
				tile.draw(surface, x, y, tile_width, tile_height)
				y = y+tile_height
			x = x+tile_width
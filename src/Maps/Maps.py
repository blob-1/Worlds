from random import randint

from .Tiles import Tile

class Map():
	def __init__(self, tiles = None, x = 1920, y = 1080, Perlin = 50):
		if tiles != None:
			self.__tiles  = tiles
			self.__height = len(tiles)
			self.__width  = len(tiles[0])
		else:
			self.generate_tiles(x, y)
			self.Perlin(Perlin)

					
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
			
	def generate_tiles(self, x, y):
		self.__tiles = []
		for i in range(x):
			self.__tiles.append([])
			for j in range(y):
				self.__tiles[i].append(Tile())
				self.__height = y
				self.__width  = x
				
	def Perlin(self, nbcycles):	
		for c in range(nbcycles):	
			new_tiles = []
			for i, row in enumerate(self.__tiles):
				new_tiles.append([])
				for j, tile in enumerate(row):
					newHeight = 0
					# top left
					if i != 0 and j != 0                            : newHeight = newHeight+self.__tiles[i-1][j-1].get_height()
					elif i == 0 and j != 0                          : newHeight = newHeight+self.__tiles[-1][j-1].get_height()
					elif i != 0 and j == 0                          : newHeight = newHeight+self.__tiles[i-1][-1].get_height()
					else                                            : newHeight = newHeight+self.__tiles[-1][-1].get_height()
					
					# top top
					if i != 0                                       : newHeight = newHeight+self.__tiles[i-1][j].get_height()
					else                                            : newHeight = newHeight+self.__tiles[-1][j].get_height()
					
					# top right
					if i != 0 and j != self.__height-1              : newHeight = newHeight+self.__tiles[i-1][j+1].get_height()
					elif i == 0 and j != self.__height-1            : newHeight = newHeight+self.__tiles[-1][j+1].get_height()
					elif i != 0 and j == self.__height-1            : newHeight = newHeight+self.__tiles[i-1][0].get_height()
					else                                            : newHeight = newHeight+self.__tiles[-1][0].get_height()			
						
					# left left	
					if j != 0                                       : newHeight = newHeight+self.__tiles[i][j-1].get_height()
					else                                            : newHeight = newHeight+self.__tiles[i][-1].get_height()
					
					# center
					newHeight = newHeight+self.__tiles[i][j].get_height()
						
					# right right 	
					if j != self.__height-1                         : newHeight = newHeight+self.__tiles[i][j+1].get_height()
					else                                            : newHeight = newHeight+self.__tiles[i][0].get_height()		
					
					# bottom left
					if i != self.__width-1 and j != 0               : newHeight = newHeight+self.__tiles[i+1][j-1].get_height()
					elif i == self.__width-1 and j != 0               : newHeight = newHeight+self.__tiles[0][j-1].get_height()
					elif i != self.__width-1 and j == 0               : newHeight = newHeight+self.__tiles[i+1][-1].get_height()
					else                                            : newHeight = newHeight+self.__tiles[0][-1].get_height()
					
					# bottom bottom
					if i != self.__width-1                          : newHeight = newHeight+self.__tiles[i+1][j].get_height()
					else                                            : newHeight = newHeight+self.__tiles[0][j].get_height()
					
					# bottom right
					if i != self.__width-1 and j != self.__height-1 : newHeight = newHeight+self.__tiles[i+1][j+1].get_height()
					elif i == self.__width-1 and j != self.__height-1 : newHeight = newHeight+self.__tiles[0][j+1].get_height()
					elif i != self.__width-1 and j == self.__height-1 : newHeight = newHeight+self.__tiles[i+1][0].get_height()
					else                                            : newHeight = newHeight+self.__tiles[0][0].get_height()
					
					new_tiles[-1].append(Tile(newHeight/9))
			self.__tiles = new_tiles

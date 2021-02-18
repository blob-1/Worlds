from random import randint

from .Tiles import Tile

class Map():
	def __init__(self, tiles = None, x = 192, y = 108, Perlin = 50):
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
				self.__width  = x
				self.__height = y
				
	def Perlin(self, nbcycles):	
		for c in range(nbcycles):	
			new_tiles = []
			for i, row in enumerate(self.__tiles):
				new_tiles.append([])
				for j, tile in enumerate(row):
					newHeight = 0
					# top left
					newHeight = newHeight+self.__getValidNeighbourgTile(i,j,-1,-1).get_height()
					
					# top top
					newHeight = newHeight+self.__getValidNeighbourgTile(i,j,-1,0).get_height()
					
					# top right
					newHeight = newHeight+self.__getValidNeighbourgTile(i,j,-1,1).get_height()		
						
					# left left	
					newHeight = newHeight+self.__getValidNeighbourgTile(i,j,0,-1).get_height()
					
					# center
					newHeight = newHeight+self.__tiles[i][j].get_height()
						
					# right right 
					newHeight = newHeight+self.__getValidNeighbourgTile(i,j,0,+1).get_height()						
					
					# bottom left
					newHeight = newHeight+self.__getValidNeighbourgTile(i,j,1,-1).get_height()
					
					# bottom bottom
					newHeight = newHeight+self.__getValidNeighbourgTile(i,j,1,0).get_height()
					
					# bottom right
					newHeight = newHeight+self.__getValidNeighbourgTile(i,j,1,1).get_height()
					
					new_tiles[-1].append(Tile(newHeight/9))
			self.__tiles = new_tiles

	def __getValidNeighbourgTile(self, i, j, incri, incrj): # note : we are on a torus !
		if incri == -1:
			if i == 0:
				i = -1
			else:
				i = i-1
		
		if incrj == -1:
			if j == 0:
				j = -1
			else:
				j = j-1	
				
		if incri == 1:
			if i == self.__width-1:
				i = 0
			else:
				i = i+1
		
		if incrj == 1:
			if j == self.__height-1:
				j = 0
			else:
				j = j+1

		return(self.__tiles[i][j])
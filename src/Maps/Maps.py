from random import randint, choice
from math import cos, pi

from .Tiles import Tile
from pygame import Surface

class Map():
	def __init__(self, tiles = None, x = 192, y = 108, Perlin = 50):
		if tiles != None:
			self.__tiles  = tiles
			self.__height = len(tiles)
			self.__width  = len(tiles[0])
		else:
			self.__Generate_tiles(x, y)
			for i in range(100):
				self.__generateCircle(randint(10,20), randint(0,x), randint(0,y), randint(0,100))
			self.__Perlin(Perlin)
					
	def get_tiles(self): return self.__tiles
	def set_tiles(self, tiles): self.__tiles = tiles
	
	def draw(self, surface, type = "heightMap", shift = 0):
		img = Surface((surface.get_width(), surface.get_height()))
	
		tile_height = surface.get_height() / self.__height
		tile_width  = surface.get_width() / self.__width

		x = 0
		for row in self.__tiles:
			y = 0
			for tile in row:
				tile.draw(img, x, y, tile_width, tile_height, type)
				y = y+tile_height
			x = x+tile_width
		
		if shift == 0:
			surface.blit(img, (0, 0))
		else:
			while shift > surface.get_width():
				shift = shift - surface.get_width()
			while shift < 0:
				shift = shift + surface.get_width()
			
			surface.blit(img, (-surface.get_width()+shift, 0))	
			surface.blit(img, (shift, 0))
	
	## RANDOM MAP GENERATION ! ##
	
	def __Generate_tiles(self, x, y):
		self.__tiles = []
		for i in range(x):
			self.__tiles.append([])
			for j in range(y):
				self.__tiles[i].append(Tile())
				self.__width  = x
				self.__height = y
				
	def __Perlin(self, nbcycles):	
		for c in range(nbcycles):	
			new_tiles = []
			for i, row in enumerate(self.__tiles):
				new_tiles.append([])
				for j, tile in enumerate(row):
					newHeight = 0
					# top left
					newHeight = newHeight+self.__getValidTile(i-1,j-1).get_height()
					
					# top top
					newHeight = newHeight+self.__getValidTile(i-1,j).get_height()
					
					# top right
					newHeight = newHeight+self.__getValidTile(i-1,j+1).get_height()		
						
					# left left	
					newHeight = newHeight+self.__getValidTile(i,j-1).get_height()
					
					# center
					newHeight = newHeight+self.__tiles[i][j].get_height()
						
					# right right 
					newHeight = newHeight+self.__getValidTile(i,j+1).get_height()						
					
					# bottom left
					newHeight = newHeight+self.__getValidTile(i+1,j-1).get_height()
					
					# bottom bottom
					newHeight = newHeight+self.__getValidTile(i+1,j).get_height()
					
					# bottom right
					newHeight = newHeight+self.__getValidTile(i+1,j+1).get_height()
					
					new_tiles[-1].append(Tile(newHeight/9))
			self.__tiles = new_tiles

	def __getValidTile(self, i, j): # note : we are on a torus here!
		while j < 0:
			j = j + self.__height
		while j >= self.__height:
			j = j - self.__height
		
		while i < 0:
			i = i + self.__width
		while i >= self.__width:
			i = i - self.__width
			
		return(self.__tiles[i][j])
		
	def __generateCircle(self, r, Xshift=10, Yshift=10, height=100):
		for r in range(r):
			l = int(r*cos(pi/4))

			# At x=0, y=r
			y = r

			r2 = y * y
			y2 = y * y
			ty = (2 * y) - 1;
			y2_new = r2 + 3;
			
			Coords = []

			for x in range(l):
				y2_new = y2_new - (2 * x) - 3;

				if (y2 - y2_new) >= ty:
					y2 -= ty;
					y -= 1;
					ty -= 2;

				self.__getValidTile(-x+Xshift, -y+Yshift).set_height(height)
				self.__getValidTile(-x+Xshift, y+Yshift).set_height(height)
				self.__getValidTile(x+Xshift, -y+Yshift).set_height(height)
				self.__getValidTile(x+Xshift, y+Yshift).set_height(height)
				
				self.__getValidTile(-y+Xshift, -x+Yshift).set_height(height)
				self.__getValidTile(-y+Xshift, x+Yshift).set_height(height)
				self.__getValidTile(y+Xshift, -x+Yshift).set_height(height)
				self.__getValidTile(y+Xshift, x+Yshift).set_height(height)

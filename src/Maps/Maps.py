from random import randint, choice
from math import cos, pi

from Maps.Tiles import Tile 
from Maps.Regions.Continents import Continent
from Maps.Regions.Oceans import Ocean

from Maps.TerainCharacteristics.OceanCurrents import OceanCurrent

from pygame import Surface

class Map():
	def __init__(self, tiles = None, x = 192, y = 108, Perlin = 50):
		self.__type = "continent"
		
		if tiles != None:
			self.__Tiles  = tiles
			self.__height = len(tiles)
			self.__width  = len(tiles[0])
		else:
			self.Generate_tiles(x, y)
			for i in range(int((self.__height*self.__height)/116.64)):
				self.__generateCircle(randint(10,20), randint(0,x), randint(0,y), randint(0,100))
			self.__Perlin(Perlin)
		
		# generating the regions ! Ech conected tiles (Ocean or Continent) is assembled in one mass
		self.generateRegions()
			
		# generate the currents :	
		self.generateCurrents(6)	
			
		self.__modified = True
				
		# print(len(max(self.__Regions, key = lambda x:len(x.getTiles())).getTiles()))
		# print(len(self.__Regions))
		# quit()		
			
	def get_tiles(self): return self.__Tiles
	def set_tiles(self, tiles): self.__Tiles = tiles
	
	def draw(self, surface, type = "continent", shift = [0,0]): 
		tile_height = surface.get_height() / self.__height
		tile_width  = surface.get_width() / self.__width
		# placing the tiles
		if self.__modified or self.__type != type:
			self.__type = type
			self.__img = Surface((surface.get_width(), surface.get_height()))

			x = 0
			for row in self.__Tiles:
				y = 0
				for tile in row:
					tile.draw(self.__img, x, y, tile_width, tile_height, type)
					y = y+tile_height
				x = x+tile_width
			
			# adding characteristics
			x = 0
			for row in self.__Tiles:
				y = 0
				for tile in row:
					tile.drawCharacteristics(self.__img, x, y, tile_width, tile_height, type)
					y = y+tile_height
				x = x+tile_width
			
			self.__modified = False
		
		# shifting the view and actually drawing
		if shift == [0,0]:
			surface.blit(self.__img, (0, 0))
		else:
			surface.blit(self.__img, (-surface.get_width()+shift[0], -surface.get_height()+shift[1]))	
			surface.blit(self.__img, (-surface.get_width()+shift[0], shift[1]))			
			surface.blit(self.__img, (shift[0], -surface.get_height()+shift[1]))	
			surface.blit(self.__img, (shift[0], shift[1]))
	
	## RANDOM MAP GENERATION ! ##
	
	def Generate_tiles(self, x, y):
		self.__Tiles = []
		for i in range(x):
			self.__Tiles.append([])
			for j in range(y):
				self.__Tiles[i].append(Tile())
				self.__width  = x
				self.__height = y
				
	def __Perlin(self, nbcycles):	
		for c in range(nbcycles):	
			new_tiles = []
			for i, row in enumerate(self.__Tiles):
				new_tiles.append([])
				for j, tile in enumerate(row):
					newHeight = self.__Tiles[i][j].get_height()
					for neibourg in self.getNeibourgs(i, j):
						newHeight = newHeight+neibourg.get_height()
					
					new_tiles[-1].append(Tile(newHeight/9))
			self.__Tiles = new_tiles

	def getNeibourgs(self, i, j, returnIndicises = False):
		neigs = []
		neigs.append(self.__getValidTile(i-1,j-1, returnIndicises))
		neigs.append(self.__getValidTile(i-1,j  , returnIndicises))
		neigs.append(self.__getValidTile(i-1,j+1, returnIndicises))
		neigs.append(self.__getValidTile(i,j-1  , returnIndicises))
		#neigs.append(self.__getValidTile(i,j))
		neigs.append(self.__getValidTile(i,j+1  , returnIndicises))
		neigs.append(self.__getValidTile(i+1,j-1, returnIndicises))
		neigs.append(self.__getValidTile(i+1,j  , returnIndicises))
		neigs.append(self.__getValidTile(i+1,j+1, returnIndicises))
		return(neigs)

	def __getValidTile(self, i, j, returnIndicises = False): # note : we are on a square flat torus here!
		while j < 0:
			j = j + self.__height
		while j >= self.__height:
			j = j - self.__height
		
		while i < 0:
			i = i + self.__width
		while i >= self.__width:
			i = i - self.__width
		
		if returnIndicises:
			return((self.__Tiles[i][j],i,j))
		else:
			return(self.__Tiles[i][j])
		
	# note : here to generate masses of similar heights and so having a more balanced map	
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
	
	def generateRegions(self):	
		self.__Regions = []
		for i, row in enumerate(self.__Tiles):
			for j, tile in enumerate(row):
				newR = Ocean()
				if not newR.addTile((tile,i,j)):
					newR = Continent()
					if not newR.addTile((tile,i,j)):
						continue
							
				newR.generate(self, i, j, tile)	
				self.__Regions.append(newR)			
				
	def generateCurrents(self, nbcells = 6): # note : was overwhelmed by complexity of how to determine precise circulations cells soooo this is bad ! 
		# get tiles that are on the different longitudes that determine a circulation cells. 
		longitudinalTiles = []
		positions = [int(self.__height*(i/nbcells))-1 for i in range(1, nbcells+1)]
		
	def generateCurrents(self, nbcells = 6): # note : was overwhelmed by complexity of how to determine precise circulations cells soooo this is bad ! 
		# get tiles that are on the different longitudes that determine a circulation cells. 
		longitudinalTiles = []
		positions = [int(self.__height*(i/nbcells))-1 for i in range(1, nbcells+1)]
		
		direction = "hot"
		
		for i, listOFtile in enumerate(self.__Tiles):
			for j, tile in enumerate(listOFtile):
				if j in positions:
					if direction == "hot":
						direction = "cold"
					else:
						direction = "hot"
				if type(tile.getRegion()) is Ocean:
					tile.addCharacteristic(OceanCurrent(direction))

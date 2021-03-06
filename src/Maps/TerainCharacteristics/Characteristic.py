from pygame.draw import aaline

class Characteristic():
	def __init__(self):
		if type(self) is Characteristic:
			raise Exception('Characteristic is an abstract class and cannot be instantiated directly')		
			
	def draw(self, surface, x, y, w, h):
		pass
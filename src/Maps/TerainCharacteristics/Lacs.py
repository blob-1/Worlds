from pygame.draw import ellipse

class Lac():
	def __init__(self):
		pass
		
	def draw(surface, x, y, w, h):ellipse(surface, (56,21,200), (x, y, w, h))
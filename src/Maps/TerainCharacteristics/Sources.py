from pygame.draw import ellipse

class Source():
	def __init__(self):
		pass
		
	def draw(surface, x, y, w, h):ellipse(surface, (56,21,200), (x+w/4, y+h/4, w/2, h/2))
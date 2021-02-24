from pygame.draw import circle

class Source():
	def __init__(self):
		pass
		
	def draw(surface, x, y, w, h):circle(surface, (56,21,200), (int(x+h/2), int(y+w/2)), 3)
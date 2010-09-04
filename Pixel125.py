# Copyright (c) 2007 Hartmut Bohnacker
# http://hartmut-bohnacker.de/

from FL import *

class Tool:
	
	def __init__(self):
		
		self.pressed = 0
		self.autoscroll = 1
		self.position = Point(0, 0)
		self.path = []
		self.size = 125
		self.drawmode = 1
		
	def Show(self, c, i):
		
		p = Point(self.path[i])
		s = self.size
		c.pen_style = cPEN_NULL
		c.brush_color = 0
		c.Rectangle(0, p.x, p.y, p.x + s, p.y + s)

	def Draw(self, g, p, size):
	
		node = Node(nMOVE, Point(p.x, p.y))
		g.Add(node)

		node.type = nLINE;
		node.points = [Point(p.x, p.y + size)]
		g.Add(node)

		node.points = [Point(p.x + size, p.y + size)]
		g.Add(node)

		node.points = [Point(p.x + size, p.y)]
		g.Add(node)

		node.points = [Point(p.x, p.y)]
		g.Add(node)
		
	def down(self, x, y, keys):
		
		if self.pressed == 1:
		  return 0
		
		fl.capture = 1
		
		self.path = []
		self.g = fl.glyph

		fl.SetUndo()
		c = fl.GetCanvas()
		fl.GetConvert(c)
		
		p = c.UnConvert(Point(x, y))
		p.x = int(int(p.x / self.size) * self.size)
		p.y = int(int(p.y / self.size) * self.size)

		self.position = p
		self.path.append(self.position)
		self.Show(c, 0)
		self.pressed = 1

		# determine drawmode

		temp = Glyph(self.g.layers_number)
		gtemp = Glyph(self.g)

		self.Draw(temp, self.position, self.size)
		gtemp.Bintersect(temp)

		if (len(gtemp.nodes) > 0):
			self.drawmode = 0
		else:
			self.drawmode = 1

		del temp
		del gtemp

		return 1

	def up(self, x, y, keys):
		
		if self.pressed == 0:
		  return

		temp = Glyph(self.g.layers_number)

		for i in range(len(self.path)):
		  self.Draw(temp, self.path[i], self.size)

		temp.RemoveOverlap()
		
		if (self.drawmode == 1):
			self.g.Badd(temp)
		else:
			self.g.Bsubtract(temp)
		
		del temp

		fl.UpdateGlyph()
		self.path = []
		self.pressed = 0
		fl.capture = 0

	def move(self, x, y, keys):
		
		if self.pressed == 0:
		  return 0

		c = fl.GetCanvas()
		fl.GetConvert(c)

		p = c.UnConvert(Point(x, y))
		p.x = int(int(p.x / self.size) * self.size)
		p.y = int(int(p.y / self.size) * self.size)
		
		if self.position == p:
		  return 1

		self.position = p
		self.path.append(p)

		self.Show(c, len(self.path) - 1)
		return 1

	def paint(self, c):
		
		fl.GetConvert(c)
		for i in range(len(self.path)):
		  self.Show(c, i)

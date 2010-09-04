#FLM: Pixel tool

# Copyright (c) 2007 Hartmut Bohnacker
# Version 1.1 - modified by Paul van der Laan
# Draws pixels according to FontLab grid preferences


from FL import *
o = Options()


class Tool:
	
	def __init__(self):
		
		self.pressed = 0
		self.autoscroll = 1
		self.position = Point(0, 0)
		self.path = []
		self.sizex = o.EditGridX
		self.sizey = o.EditGridY
		self.drawmode = 1
		self.debug = False
	
	
	def Show(self, c, i):
		
		if self.debug :
			print "Show", c, i
		
		p = Point(self.path[i])
		sx = self.sizex
		sy = self.sizey
		c.pen_style = cPEN_NULL
		c.brush_color = 0
		c.Rectangle(0, p.x, p.y, p.x + sx, p.y + sy)
	
	
	def Draw(self, g, p, sizex, sizey):
		
		if self.debug :
			print "Draw", g, p
		
		node = Node(nMOVE, Point(p.x, p.y))
		g.Add(node)
		
		node.type = nLINE;
		node.points = [Point(p.x, p.y + sizey)]
		g.Add(node)
		
		node.points = [Point(p.x + sizex, p.y + sizey)]
		g.Add(node)
		
		node.points = [Point(p.x + sizex, p.y)]
		g.Add(node)
		
		node.points = [Point(p.x, p.y)]
		g.Add(node)
	
	
	def down(self, x, y, keys):
		
		if self.debug :
			print "Down", x, y, keys
		
		if self.pressed == 1:
		  return 0
		
		fl.capture = 1
		
		self.path = []
		self.g = fl.glyph
		
		fl.SetUndo()
		c = fl.GetCanvas()
		fl.GetConvert(c)
		
		p = c.UnConvert(Point(x, y))
		p.x = int(int(p.x / self.sizex) * self.sizex)
		p.y = int(int(p.y / self.sizey) * self.sizey)
		
		self.position = p
		self.path.append(self.position)
		self.Show(c, 0)
		self.pressed = 1
		
		# determine drawmode
		
		temp = Glyph(self.g.layers_number)
		gtemp = Glyph(self.g)
		
		self.Draw(temp, self.position, self.sizex, self.sizey)
		gtemp.Bintersect(temp)
		
		if (len(gtemp.nodes) > 0):
			self.drawmode = 0
		else:
			self.drawmode = 1
			
		del temp
		del gtemp
		
		return 1
	
	
	def up(self, x, y, keys):
		
		if self.debug :
			print "Up: ",x, y, keys
		
		if self.pressed == 0:
		  return
		
		temp = Glyph(self.g.layers_number)
		
		for i in range(len(self.path)):
		  self.Draw(temp, self.path[i], self.sizex, self.sizey)
		
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
		
		if self.debug :
			print "Move", x, y, keys
		
		if self.pressed == 0:
		  return 0
		
		c = fl.GetCanvas()
		fl.GetConvert(c)
		
		p = c.UnConvert(Point(x, y))
		p.x = int(int(p.x / self.sizex) * self.sizex)
		p.y = int(int(p.y / self.sizey) * self.sizey)
		
		if self.position == p:
		  return 1
		
		self.position = p
		self.path.append(p)
		
		self.Show(c, len(self.path) - 1)
		return 1
	
	
	def paint(self, c):
		
		if self.debug :
			print "Paint", c
		
		fl.GetConvert(c)
		for i in range(len(self.path)):
		  self.Show(c, i)
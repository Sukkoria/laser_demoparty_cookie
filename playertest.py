# -*- coding: utf-8 -*-

from globalVars import *
import frame

SPEED = 4
SIZE = 20

class PlayerTest(object):
	
	def __init__(self, color=0xFFFF00):
		self.x, self.y = screen_size[0]/2, screen_size[1]/2
		self.angle = 0
                self.color = color

        def SetColor(self, new_color):
            self.color = new_color
		
	def Move(self,up_key,down_key,left_key,right_key):
		if up_key:
			self.y -= SPEED
		elif down_key:
			self.y += SPEED
		if left_key:
			self.x -= SPEED
		elif right_key:
			self.x += SPEED
			
		if self.x < 0:
			self.x = 0
		elif self.x >= screen_size[0]:
			self.x = screen_size[0]
		if self.y < 0:
			self.y = 0
		elif self.y >= screen_size[1]:
			self.y = screen_size[1]

        def SetPosition(self, x, y):
            self.x = x
            self.y = y

        def MoveWithPos(self, vx, vy):
            self.x += vx
            self.y += vy
	def Draw(self,f):
		xmin = self.x - SIZE
		xmax = self.x + SIZE
		ymin = self.y - SIZE
		ymax = self.y + SIZE
		f.PolyLineOneColor([(xmin,ymin),(xmin,ymax),(xmax,ymax),(xmax,ymin)], self.color,True)


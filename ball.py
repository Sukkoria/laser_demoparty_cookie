# -*- coding: utf-8 -*-

from globalVars import *
import frame
import math


class Ball(object):
	
	def __init__(self):
		self.x, self.y = ball_origin[0], ball_origin[1]
		self.zoom = 1
		
		
	def Move(self,xcoord,ycoord):
		
		self.x = xcoord
		self.y = ycoord
		#self.zoom = ?
		
		if self.x < 0:
			self.x = 0
		
		elif self.x >= screen_size[0]:
			self.x = screen_size[0]
		
		if self.y < 0:
			self.y = 0
		
		elif self.y >= screen_size[1]:
			self.y = screen_size[1]

	def Draw(self,f):
	
		
		xmin = 0
		xmax = BALL_SIZE_X * 2
		ymin = 0
		ymax = BALL_SIZE_Y * 2
		
		xmin = (xmin*self.zoom)
		ymin = (ymin*self.zoom) 
		xmax = (xmax*self.zoom) 
		ymax = (ymax*self.zoom)
		

		xmin += self.x 
		xmax += self.x
		ymin += self.y 
		ymax += self.y
		
		f.LineTo((xmin,ymin), 0x80000000)
		f.PolyLineOneColor([(xmin,ymin),(xmin,ymax),(xmax,ymax),(xmax,ymin)], 0xFFFFFF,True)

	
# coding=UTF-8
'''
Created on 25 janv. 2015

@author: pclf
'''

import gstt
import vectors
from globalVars import *


ZOOM_PLAYING = 1.6
ZOOM_GAMEOVER = 5.0
DZOOM_PLAYING = -.4
DZOOM_GAMEOVER = .1

# Finalement, on implémente le score ici
DIGITS_GRAPHICS = [
	[[(-10,-20), (10,-20), (10,20), (-10,20), (-10,-20)]],							#0
	[[(0,-20), (0,20)]],															#1
	[[(-10,-20), (10,-20), (10,0), (-10,0), (-10,20), (10,20)]],					#2
	[[(-10,-20), (10,-20), (10,20), (-10,20)], [(10,0), (-10,0)]],					#3
	[[(-10,-20), (-10,0), (10,0), (10,20)], [(10,-20), (10,0)]],					#4
	[[(10,-20), (-10,-20), (-10,0), (10,0), (10,20), (-10,20)]],					#5
	[[(-10,-20), (-10,20), (10,20), (10,0), (-10,0)]],								#6
	[[(-10,-20), (10,-20), (10,20)]],												#7
	[[(-10,-20), (10,-20), (10,20), (-10,20), (-10,-20)], [(-10,0), (10,0)]],		#8
	[[(10,0), (-10,0), (-10,-20), (10,-20), (10,20)]],								#9
	[[(-2,15), (2,15)]]	# Point
]


class Score(object):
	'''
	classdocs
	'''


	def __init__(self):
		'''
		Constructor
		'''
		self.value = 0
		self.zoom = ZOOM_PLAYING
		
	def Reset(self):
		self.value = 0
		
	def Increase(self, increasevalue):
		self.value += increasevalue
	
	def ZoomIn(self):
		self.zoom += DZOOM_GAMEOVER
		if self.zoom > ZOOM_GAMEOVER:
			self.zoom = ZOOM_GAMEOVER
	
	def ZoomOut(self):
		self.zoom += DZOOM_PLAYING
		if self.zoom < ZOOM_PLAYING:
			self.zoom = ZOOM_PLAYING

	def ZoomReset(self):
		self.zoom = ZOOM_PLAYING
		
	def Draw(self, f):
		value_temp = self.value
		rg_digit = 0
		chars = []
		if (value_temp // 10) == 1:
			while rg_digit < 2 or value_temp:
				chars.append(value_temp % 10)
				value_temp //= 10
				rg_digit += 1
		else:
			chars.append(value_temp % 10)
			
		self.DrawChars(f, chars)
	
	def DrawChars(self, f, chars):
		#TODO : gérer correctement les coordonnées
		l = len(chars)
		f.LineTo((score_pos[0],score_pos[1]), 0x80000000)
		for i, ch in enumerate(chars):
			x_offset = 12 * (l- 1 - 2*i)
			digit_pl_list = DIGITS_GRAPHICS[ch]
			
			for pl in digit_pl_list:
				pl_draw = []
				for xy in pl:
					xy_draw = vectors.Vector2D(score_pos[0],score_pos[1]) + vectors.Vector2D(xy[0] + x_offset,xy[1]) * self.zoom
					pl_draw.append(xy_draw.ToTuple())
				f.PolyLineOneColor(pl_draw, 0xFFFF00)
		
		
		
		
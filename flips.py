# -*- coding: utf-8 -*-

from globalVars import *
import frame
import math


class Flips(object):
	
	def __init__(self):
		self.lx, self.ly = FLIPS_lorigin[0], FLIPS_lorigin[1]
		self.rx, self.ry = FLIPS_rorigin[0], FLIPS_rorigin[1]
		self.speed = 7
		
		
	def Move(self,left_key,right_key,up_key,down_key):

		if left_key:
			self.ly -= self.speed
			if self.ly < 1:
				self.ly = 1
			
		if right_key:
			self.ly += self.speed
			if self.ly > screen_size[1] - PADDLE_height:
				self.ly = screen_size[1]  - PADDLE_height

		if up_key:
			self.ry -= self.speed
			if self.ry < 1:
				self.ry = 1			
				
		if down_key:
			self.ry += self.speed
			if self.ry > screen_size[1] - PADDLE_height:
				self.ry = screen_size[1]  - PADDLE_height

		return self.ly, self.ry
		
	def MoveJoy(self,left_key,right_key,up_key,down_key,lvertax):

		if left_key:
			self.ly -= self.speed
			if self.ly < 1:
				self.ly = 1
			
		if right_key:
			self.ly += self.speed
			if self.ly > screen_size[1] - PADDLE_height:
				self.ly = screen_size[1]  - PADDLE_height

		if up_key:
			self.ry -= self.speed
			if self.ry < 1:
				self.ry = 1			
		if down_key > 0.01:
			self.ry += self.speed
			if self.ry > screen_size[1] - PADDLE_height:
				self.ry = screen_size[1]  - PADDLE_height
		
		if lvertax:
			print lvertax
			if lvertax < 0:
				self.ly -= self.speed
				if self.ly < 1:
					self.ly = 1
			elif lvertax > 0.01:
				self.ly += self.speed
				if self.ly > screen_size[1] - PADDLE_height:
					self.ly = screen_size[1]  - PADDLE_height
			

		return self.ly, self.ry

	def Draw(self,f):

		f.LineTo((self.lx,self.ly), 0x80000000)
		f.PolyLineOneColor([(self.lx,self.ly),(self.lx,self.ly + PADDLE_height),(self.lx + PADDLE_width , self.ly + PADDLE_height),(self.lx + PADDLE_width,self.ly)], 0xFFFFFF,True)
			
		f.LineTo((self.rx,self.ry), 0x80000000)
		f.PolyLineOneColor([(self.rx,self.ry),(self.rx,self.ry + PADDLE_height),(self.rx + PADDLE_width , self.ry + PADDLE_height),(self.rx + PADDLE_width,self.ry)], 0xFFFFFF,True)
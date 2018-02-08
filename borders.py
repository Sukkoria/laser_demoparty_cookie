# -*- coding: utf-8 -*-

from globalVars import *
import frame
import math


class Borders(object):
	
	def __init__(self):
		pass


	def Draw(self,f):

		f.LineTo((1,1), 0x80000000)
		f.PolyLineOneColor([(1,1),(1,screen_size[1]),(screen_size[0],screen_size[1]),(screen_size[0],1)], 0xFFFFFF,True)

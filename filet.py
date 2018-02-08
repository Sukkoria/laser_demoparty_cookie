# -*- coding: utf-8 -*-

from globalVars import *
import frame
import math


class Filet(object):
	
	def __init__(self):
		pass


	def Draw(self,f):

		f.LineTo((1,1), 0x80000000)
		f.PolyLineOneColor([(screen_size[0]/2,screen_size[1]),(screen_size[0]/2,0)], 0xFFFFFF,True)

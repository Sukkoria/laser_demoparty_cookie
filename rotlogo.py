"""

Logo Animation

by Sam Neurohack 
from /team/laser

"""

from globalVars import *
import frame
import sys, math, random
import vectors
import gstt



class Logo(object):
	
	def __init__(self):

		self.width = screen_size[0]
		self.height = screen_size[1]
		
		
		self.centerX = self.width / 2
		self.centerY = self.height / 2
		
		self.fov = 256
		self.viewer_distance = 300.2
		
		self.angleX = 0
		self.angleY = 180
		self.angleZ = 180
		self.color = 0x000000
		
		

		self.LOGO = [
			# Etoile
			[[(-155,-95),(-135,-85)],0xFF00],
			[[(-155,-85),(-135,-95)],0xFF00],
			[[(-150,-100),(-140,-80)],0xFF00],
			# L/o
			[[(-140,-100),(-200,20),(120,20)],0xFF00],
			# aser
			[[(-140,-40),(-100,-40,),(-120,0),(-160,0),(-110,-20)],0xFFFF],
			[[(-40,-40),(-60,-40),(-90,-20),(-50,-20),(-80,0),(-100,0)],0xFFFF],
			[[(-30,-20),(10,-20),(0,-40),(-20,-40),(-30,-20),(-30,0),(-10,0)],0xFFFF],
			[[(20,0),(40,-40),(35,-30),(50,-40),(70,-40)],0xFFFF],
		]

		self.LOGO_OFFSET = vectors.Vector2D(400,320)


	def Move(self,centerX,centerY):
	
		self.centerX = centerX
		self.centerY = centerY	
		
		
	def Zoom(self, zoom):
	
		self.viewer_distance = zoom
				
				

	def Draw(self,f):
	
	
		'''
		Draw with Y rotation animation
		'''

		
		#self.angleX += 0.05
		self.angleY += 0.5
		#self.angleZ += 0.1
		
			
	
		for pl_color in self.LOGO:
			c = pl_color[1]
			xy_list = []
			for xy in pl_color[0]:

			
				x = xy[0]
				y = xy[1]
				z=0
				# 3D rotation along self.angleX, self.angleX, self.angleX
			
				rad = self.angleX * math.pi / 180
				cosa = math.cos(rad)
				sina = math.sin(rad)
				y2 = y
				y = y2 * cosa - z * sina
				z = y2 * sina + z * cosa


				rad = self.angleY * math.pi / 180
				cosa = math.cos(rad)
				sina = math.sin(rad)
				z2 = z
				z = z2 * cosa - x * sina
				x = z2 * sina + x * cosa


				rad = self.angleZ * math.pi / 180
				cosa = math.cos(rad)
				sina = math.sin(rad)
				x2 = x
				x = x2 * cosa - y * sina
				y = x2 * sina + y * cosa
			
			
				# 3D to 2D projection
				factor = self.fov / (self.viewer_distance + z)
				x = x * factor 
				y = - y * factor
			

				xy_list.append((self.LOGO_OFFSET + vectors.Vector2D(x,y)).ToTuple())


			f.PolyLineOneColor(xy_list, c)


	









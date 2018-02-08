"""

Spiral animation

by Sam Neurohack 
from /team/laser

 Based on Wireframe 3D cube simulation.
 Developed by Leonel Machava <leonelmachava@gmail.com>

 Wipeout style ship 

"""

from globalVars import *
import frame
import sys, math, random



SPEED = 4
SIZE = 40



class Saber2(object):
	
	def __init__(self):

		self.width = screen_size[0]
		self.height = screen_size[1]
		
		# (saberoriginx,saberoriginy,saberendx,saberendy)			
		self.saber=[(0,0,0),(0,150,0)]
		
		
		self.centerX = self.width / 2
		self.centerY = self.height / 2
		
		
		self.fov = 256
		self.viewer_distance = 50.2
		
		self.angleX = 0
		self.angleY = 0
		self.angleZ = 0
		self.color = 0xFF0000
		

	def Move(self,centerX,centerY):
	
		self.centerX = centerX
		self.centerY = centerY	

	def Mode(self,centerX,centerY):
	
		self.centerX = centerX
		self.centerY = centerY	
		
		
	def Acc(self,accX,accY,accZ):
	
		self.centerX += accX *100
		self.centerY += accY *100
		#self.centerZ += accZ *50
		
		if self.centerX < 10:
			self.centerX = 10
		if self.centerX > self.width -10:
			self.centerX = self.width -10
			
			
			
		if self.centerY < 150:
			self.centerY = 150
		if self.centerY > self.height -150:
			self.centerY = self.height -150
			
			
		
	def Change(self,angleX,angleY,angleZ):
			
		self.laspoints = []
	
		for v in self.saber:
	
				# Rotate the point around X axis, then around Y axis, and finally around Z axis.

				x = v[0]
				y = v[1]
				z = v[2]

				rad = angleX * math.pi / 180
				cosa = math.cos(rad)
				sina = math.sin(rad)
				y2 = y
				y = y2 * cosa - z * sina
				z = y2 * sina + z * cosa

				rad = angleY * math.pi / 180
				cosa = math.cos(rad)
				sina = math.sin(rad)
				z2 = z
				z = z2 * cosa - x * sina
				x = z2 * sina + x * cosa

				rad = angleZ * math.pi / 180
				cosa = math.cos(rad)
				sina = math.sin(rad)
				x2 = x
				x = x2 * cosa - y * sina
				y = x2 * sina + y * cosa


				""" Transforms this 3D point to 2D using a perspective projection. """
				factor = self.fov / (self.viewer_distance + z)
				x = x * factor + self.centerX
				y = - y * factor + self.centerY
				
				
				self.laspoints.append((x,y))

		
	def Zoom(self, zoom):
	
		self.viewer_distance = zoom


	def Draw(self,f):
	
	
	
		f.PolyLineOneColor(self.laspoints, 0x00FF00,True)
		
	









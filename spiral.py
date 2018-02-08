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



class Spiral(object):
	
	def __init__(self):

		self.width = screen_size[0]
		self.height = screen_size[1]
		
		
		self.centerX = self.width / 2
		self.centerY = self.height / 2
		
		self.rot = 1
		self.dist = 1
		
		self.fov = 256
		self.viewer_distance = 90.2
		
		self.angleX = 0
		self.angleY = 0
		self.angleZ = 0
		self.color = 0x000000
		

	def Move(self,centerX,centerY):
	
		self.centerX = centerX
		self.centerY = centerY	

	def Mode(self,centerX,centerY):
	
		self.centerX = centerX
		self.centerY = centerY	
		
		
	def Zoom(self, zoom):
	
		self.viewer_distance = zoom
				
				

	def Draw(self,f):
	
	
	
		self.laspoints = []
		self.rot -= 0.5
		self.dist += 0.5
		
		#f.LineTo((self.centerX,self.centerY), 0x000000)
		
		self.angleX += 0.1
		self.angleY += 0.1
		self.angleZ += 0.1
		
		for angle in range(0,800,5):
		
		
			rad = angle * math.pi / 180
			
			''' 2D Form spiral
			r = self.rot + (self.dist * rad)
			x = self.centerX + (r * math.cos(rad))
			y = self.centerY + (r * math.sin(rad))
			'''
			
			''' 3D Form Helix '''
			
			x = 10 * math.cos(6*rad)
			y = 10 * math.sin(6*rad)
			z = 10 * rad
			
			
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
			x = x * factor + self.centerX 
			y = - y * factor + self.centerY
			
			
			# Color cycle
			self.color += 420
			
			if self.color > 0xFFFFFF:
				self.color = 0x000000
				
			f.LineTo((x,y), self.color)
			


			
			#print self.laspoints	
		
		#f.PolyLineOneColor(self.laspoints, 0xFFFF00,True)
		#f.Lineto(())
		
	









"""

Orbits generators

by Sam Neurohack 
from /team/laser

"""

from globalVars import *
import frame
import sys, math, random




class Orbits(object):
	
	def __init__(self):

		self.width = screen_size[0]
		self.height = screen_size[1]
		
		# elliptical orbit equation : r = (SemiMajorAxis*(1 - eccentricity**2))/(1 + eccentricity * cos(angle))
		# for each planet : (Angle,SemiMajorAxis length, eccentricity)
		
		self.planets = [[0,100,0.4],[90,55,0.2],[230,46,0.5],[30,90,0.5],[190,60,0.4],[90,80,0.2]]
		
		
		self.centerX = 50 + self.width / 2
		self.centerY = self.height / 2

		
		self.fov = 256
		self.viewer_distance = 100.2
		
		self.angleX = 0
		self.angleY = 0
		self.angleZ = 0
		self.color = 0xFF0000
		self.speed = 0

	def Move(self,centerX,centerY):
	
		self.centerX = centerX
		self.centerY = centerY	

	def Speed(self,speed):
	
	
		self.speed = speed
		self.centerY = centerY	
		
		
	def Zoom(self, zoom):
	
		self.viewer_distance = zoom
				
				

	def Draw(self,f):
		
		#f.LineTo((self.centerX,self.centerY), 0x000000)
		
		self.angleX += 0.0
		self.angleY += 0.0
		self.angleZ += 0.0
		
		
		for planet in self.planets:
				

			planet[0] += random.randint(0,13)
			
			rad = planet[0] * math.pi / 180
			r = (planet[1]*(1 - planet[2]**2))/(1 + (planet[2] * math.cos(rad)))
			
			
			x = r * math.cos(rad)
			y = r * math.sin(rad)
			z = 0
			# print x,y,z
			
			
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
			
			#print x,y
			
				
			f.Line((x,y),(x+5,y+5), self.color)
			


		
	









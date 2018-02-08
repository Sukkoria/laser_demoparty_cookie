"""

3D Cube laser animation

by Sam Neurohack 
from /team/laser

 Based on Wireframe 3D cube simulation.
 Developed by Leonel Machava <leonelmachava@gmail.com>

 Wipeout style ship 

"""

from globalVars import *
import frame
import sys, math, random


class Butterfly(object):
	
	def __init__(self):

		self.width = screen_size[0]
		self.height = screen_size[1]

		self.entities = []
		
		for lifes in range(0,lifenb,1):
		
			# 0: random posX, 1: random posY, 2: wing position, 3: Color, 4: XDirection
			self.entities.append([random.randint(100,self.width-100),random.randint(100,self.height-100),random.random(),random.randint(45,16700000),random.randint(-2,2)])
			
		self.wingpos = random.random()
		self.vertices = [
		( 0.0 , 0.3603683 , 0.7174169 ), #1
		( 0.0 , -4.39773 , 0.09228338 ), #2	
		( self.wingpos , 0.3603683 , 0.3174169 ), #3
		( 0.0 , 0.3603683 , 0.7174169 ), #4
		( -self.wingpos , 0.4115218 , 0.1858825 ), #7
		( 0.0 , -4.39773 , 0.09228338 ) #2	
			]

		
		self.fov = 256
		self.viewer_distance = 70.2
		
		self.angleX = 0
		self.angleY = 120
		self.angleZ = 0
		
		self.color = 0x101010
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
		
		#self.angleX += 0.0
		#self.angleY += 0.0
		#self.angleZ += 0.0
		
		
		for entity in self.entities:
				

			entity[0] += entity[4] + random.randint(-1,1)			# change X/Y pos (Xdirection and little chaos)
			if random.randint(0,20) > 15:
				entity[1] += random.randint(-2,2)
			
			self.centerX = entity[0]
		 	self.centerY  = entity[1]
																	# remember : z position is zoom			
			
			
			entity[2] += 1											# change wing pos
			if entity[2] > 10:
				entity[2] = 0.0
			self.wingpos = entity[2]
			
			
			angleX = self.angleX									# entity rotated in Z to follow Xdirection			
			angleY = self.angleY

			if entity[4] > 0:
				angleZ = (self.angleZ + entity[4]*18)
			else:
				angleZ = -(self.angleZ + entity[4]*18)
			
			
			self.color = entity[3]	
			self.laspoints = []
			verticecounter = 0
			
			for v in self.vertices:
			
			
				# Rotate the point around X axis, then around Y axis, and finally around Z axis.

				x = v[0]
				y = v[1]
				z = v[2]
				if 	verticecounter == 2:
					x = self.wingpos 
				if 	verticecounter == 4:
					x = - self.wingpos 

	
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
				
				verticecounter +=1

		
			f.PolyLineOneColor(self.laspoints, self.color,True)

			

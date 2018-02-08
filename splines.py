"""

Splines : curves animation  

by Sam Neurohack 
from /team/laser

"""

from globalVars import *
import frame
import sys, math, random



class Splines(object):
	
	def __init__(self):

		self.width = screen_size[0]
		self.height = screen_size[1]
		
		
		self.centerX = self.width / 2
		self.centerY = self.height / 2
		
		self.fov = 256
		self.viewer_distance = 2.2
		self.a1 = 0
		self.a2 = 1
		self.a1ngleX = 0
		self.a1ngleY = 0
		self.a1ngleZ = 0
		self.spl1 = [ 0x00FF00 ,320, 300]					# Spline 1 init parameters i.e color, xstart, ystart,
		self.spl2 = [ 0xFF0000 ,320,300, 30,90,0.5]			# Spline 2 init parameters 

	def Move(self,centerX,centerY):
	
		self.centerX = centerX
		self.centerY = centerY	

	def Mode(self,centerX,centerY):
	
		self.centerX = centerX
		self.centerY = centerY	
		
		
	def Zoom(self, zoom):
	
		self.viewer_distance = zoom
				
				

	def Proj(self, x,y,z,angleX, angleY, angleZ):
		
		# 3D rotation along self.a1ngleX, self.a1ngleX, self.a1ngleX
			
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
			
			
		# 3D to 2D projection
		factor = self.fov / (self.viewer_distance + z)
		x = x * factor + self.centerX 
		y = - y * factor + self.centerY
	
		return (x,y)


				
	def Spline1(self, angle, angleX, angleY, angleZ):				# Generate one projected 2D point for given angle 
																	# Lissajou curve
			
		self.viewer_distance = 30
		rad = angle * math.pi / 180
			
		# 2D Form 
		x = (10 * math.cos(self.a1*rad))
		y = (10 * math.sin(rad))
		z=0
		
		return self.Proj(x,y,z,angleX, angleY, angleZ)




	def Spline2(self, angle, angleX, angleY, angleZ):				# Epitrochoid
	 
				
		
		self.viewer_distance = 70
		rad = angle * math.pi / 180
		
		R = 21
		r= 1
		#r = self.a2
		x = (R-r)*math.cos(rad)-self.a2*math.cos( (R+r)*rad / r )
		y = (R-r)*math.sin(rad)-self.a2*math.sin( (R+r)*rad / r )
		z=0
		
		'''	
		# Polar coordinates example : angle -> radius -> x,y
		
		rad = angle * math.pi / 180	
		r = (10*math.sin(rad)))

	
		# polar to x,y
		
		x = r * math.cos(rad)									
		y = r * math.sin(rad)
		z = 0

		'''
		
		return self.Proj(x,y,z,angleX, angleY, angleZ)


	def Draw(self,f):

		
		# SPLINE 1
		
		self.laspoints = []
			
		self.spl1[0] += 420											# animation parameter		
		self.a1 += 0.001
		if self.a1 >2:
			self.a1 =0
			
		if self.spl1[0] > 0xFFFFFF:									# Color cycle
			self.spl1[0] = 0x000000	
			
		for angle in range(0,800,5):
			
			x,y = self.Spline1(angle,0,0,0) 						# points 
			self.laspoints.append((x,y))

		print self.laspoints
		f.PolyLineOneColor(self.laspoints, self.spl1[0],True)		# Draw




		# SPLINE 2
		
		self.laspoints = []
											
		self.a2 += 0.1												# animation parameter	
		if self.a2 >20:
			self.a2 =0

		if self.spl2[0] > 0xFFFFFF:									# Color cycle
			self.spl2[0] = 0x000000	
			
		for angle in range(200,1100,2):
			
			x,y = self.Spline2(angle,0,0,0) 						# points 
			self.laspoints.append((x+150,y+150))

		
		f.PolyLineOneColor(self.laspoints, self.spl2[0],True)		# Draw









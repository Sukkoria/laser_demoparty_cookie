# coding=UTF-8
"""

Title Animation

by Sam Neurohack 
from /team/laser

"""

from globalVars import *
import frame
import sys, math, random
import vectors
import gstt
import threading

DEFAULT_COLOR = 0xFFFFFF

class Title(object):
	
	def __init__(self):

		self.width = screen_size[0]
		self.height = screen_size[1]

		
		self.fov = 256
		self.viewer_distance = 300.2
		
		self.angleX = 0
		self.angleY = 180
		self.angleZ = 180
                self.multicolor = False # Default
		self.tcolor = DEFAULT_COLOR # Default
		self.mode = 0
		
		
		self.ASCII_GRAPHICS = [


			[[(-50,30), (-30,-30), (30,-30), (10,30), (-50,30)]],							#0
			[[(-50,30), (-30,-30), (30,-30), (10,30), (-50,30)]],							#0
			[[(-20,30), (0,-30), (-20,30)]], 												#1
			[[(-30,-10), (0,-30), (30,-10), (30,0), (-30,30), (30,30)]],					#2
			[[(-30,-30), (0,-30), (30,-10), (0,0), (30,10), (0,30), (-30,30)]],				#3
			[[(30,10), (-30,10), (0,-30), (0,30)]],											#4
			[[(30,-30), (-30,-30), (-30,0), (0,0), (30,10), (0,30), (-30,30)]],				#5
			[[(30,-30), (0,-30), (-30,-10), (-30,30), (0,30), (30,10), (30,0), (-30,0)]],	#6
			[[(-30,-30), (30,-30), (-30,30)]],												#7
			[[(-30,30), (-30,-30), (30,-30), (30,30), (-30,30), (-30,0), (30,0)]],			#8
			[[(30,0), (-30,0), (-30,-10), (0,-30), (30,-30), (30,10), (0,30), (-30,30)]],	#9

			# A implementer	

			[[(-30,-10), (0,-30), (0,30)], [(-30,30), (30,30)]],							#;
			[[(-30,-10), (0,-30), (30,-10), (30,0), (-30,30), (30,30)]],					#<
			[[(-30,-30), (0,-30), (30,-10), (0,0), (30,10), (0,30), (-30,30)]],				#=
			[[(30,10), (-30,10), (0,-30), (0,30)]],											#>
			[[(30,-30), (-30,-30), (-30,0), (0,0), (30,10), (0,30), (-30,30)]],				#?
			[[(30,-30), (0,-30), (-30,-10), (-30,30), (0,30), (30,10), (30,0), (-30,0)]],	#@

			# Implementé
	
			[[(-30,30), (-30,-30), (30,-30), (30,30), (30,0), (-30,0)]],				#A
			[[(-30,30), (-30,-30), (30,-30), (30,30), (30,0), (-30,0)]],				#A
			[[(-30,30), (-30,-30), (30,-30), (30,30), (-30,30), (-30,0), (30,0)]],		#B
			[[(30,30), (-30,30), (-30,-30), (30,-30)]],									#C
			[[(-30,30), (-30,-30), (30,-30), (30,30), (-30,30)]],						#D
			[[(30,30), (-30,30), (-30,-0), (30,0), (-30,0), (-30,-30), (30,-30)]],		#E
			[[(-30,30), (-30,-0), (30,0), (-30,0), (-30,-30), (30,-30)]],				#F
			[[(0,0), (30,0), (30,30), (-30,30), (-30,-30),(30,-30)]],					#G
			[[(-30,-30), (-30,30), (-30,0), (30,0), (30,30), (30,-30)]],				#H
			[[(0,30), (0,-30)]],														#I
			[[(-30,30), (0,-30), (0,-30), (-30,-30), (30,-30)]],						#J
			[[(-30,-30), (-30,30), (-30,0), (30,-30), (-30,0), (30,30)]],				#K
			[[(30,30), (-30,30), (-30,-30)]],											#L
			[[(-30,30), (-30,-30), (0,0), (30,-30), (30,30)]],							#M
			[[(-30,30), (-30,-30), (30,30), (30,-30)]],									#N
			[[(-30,30), (-30,-30), (30,-30), (30,30), (-30,30)]],						#O
			[[(-30,0), (30,0), (30,-30), (-30,-30), (-30,30)]],							#P
			[[(30,30), (30,-30), (-30,-30), (-30,30), (30,30),(35,35)]],				#Q
			[[(-30,30), (-30,-30), (30,-30), (30,0), (-30,0), (30,30)]],				#R
			[[(30,-30), (-30,-30), (-30,0), (30,0), (30,30), (-30,30)]],				#S
			[[(0,30), (0,-30), (-30,-30), (30,-30)]],									#T
			[[(-30,-30), (-30,30), (30,30), (30,-30)]],									#U
			[[(-30,-30), (0,30), (30,-30)]],											#V
			[[(-30,-30), (-30,30), (0,0), (30,30), (30,-30)]],							#W
			[[(-30,30), (30,-30)], [(-30,-30), (30,30)]],								#X
			[[(0,30), (0,0), (30,-30), (0,0), (-30,-30)]],								#Y
			[[(30,30), (-30,30), (30,-30), (-30,-30)]],									#Z
			
			
			# A implementer	

			[[(-30,-10), (0,-30), (0,30)], [(-30,30), (30,30)]],							#[
			[[(-30,-10), (0,-30), (30,-10), (30,0), (-30,30), (30,30)]],					#\
			[[(-30,-30), (0,-30), (30,-10), (0,0), (30,10), (0,30), (-30,30)]],				#]
			[[(30,10), (-30,10), (0,-30), (0,30)]],											#^
			[[(30,-30), (-30,-30), (-30,0), (0,0), (30,10), (0,30), (-30,30)]],				#_
			[[(30,-30), (0,-30), (-30,-10), (-30,30), (0,30), (30,10), (30,0), (-30,0)]],	#`
			
			# Implementé
	
			[[(-20,20), (-20,-20), (20,-20), (20,20), (20,0), (-20,0)]],				#a
			[[(-20,20), (-20,-20), (20,-20), (20,20), (-20,20), (-20,0), (20,0)]],		#b
			[[(20,20), (-20,20), (-20,-20), (20,-20)]],									#c
			[[(-20,20), (-20,-20), (20,-20), (20,20), (-20,20)]],						#d
			[[(20,20), (-20,20), (-20,-0), (20,0), (-20,0), (-20,-20), (20,-20)]],		#e
			[[(-20,20), (-20,-0), (20,0), (-20,0), (-20,-20), (20,-20)]],				#f
			[[(0,0), (20,0), (20,20), (-20,20), (-20,-20),(20,-20)]],					#g
			[[(-20,-20), (-20,20), (-20,0), (20,0), (20,20), (20,-20)]],				#H
			[[(0,20), (0,-20)]],														#I
			[[(-20,20), (0,-20), (0,-20), (-20,-20), (20,-20)]],						#J
			[[(-20,-20), (-20,20), (-20,0), (20,-20), (-20,0), (20,20)]],				#K
			[[(20,20), (-20,20), (-20,-20)]],											#L
			[[(-20,20), (-20,-20), (0,0), (20,-20), (20,20)]],							#M
			[[(-20,20), (-20,-20), (20,20), (20,-20)]],									#N
			[[(-20,20), (-20,-20), (20,-20), (20,20), (-20,20)]],						#O
			[[(-20,0), (20,0), (20,-20), (-20,-20), (-20,20)]],							#P
			[[(20,20), (20,-20), (-20,-20), (-20,20), (20,20),(25,25)]],				#Q
			[[(-20,20), (-20,-20), (20,-20), (20,0), (-20,0), (20,20)]],				#R
			[[(20,-20), (-20,-20), (-20,0), (20,0), (20,20), (-20,20)]],				#S
			[[(0,20), (0,-20), (-20,-20), (20,-20)]],									#T
			[[(-20,-20), (-20,20), (20,20), (20,-20)]],									#U
			[[(-20,-20), (0,20), (20,-20)]],											#V
			[[(-20,-20), (-20,20), (0,0), (20,20), (20,-20)]],							#W
			[[(-20,20), (20,-20)], [(-20,-20), (20,20)]],								#X
			[[(0,20), (0,0), (20,-20), (0,0), (-20,-20)]],								#Y
			[[(20,20), (-20,20), (20,-20), (-20,-20)]],									#Z

			[[(-2,15), (2,15)]]															# Point a la place de {
		]


		self.value = ""



	def Text(self, text):
	
		gstt.tmessage = text
		#print "tmessage : ", text
		
	def Move(self,centerX,centerY):
	
		#print "Move to : ", str(centerX), " ", str(centerY)
		self.centerX = centerX
		self.centerY = centerY
		
	def MoveR(self,deltas):
	
		# deltas = (dX,dY)
		self.dX = deltas[0]
		self.dY = deltas[1]
		
	def Zoom(self, zoom,zoomR):
	
		self.viewer_distance = zoom
		self.zoomr = zoomR
		#print "zoom ", str(self.viewer_distance), "zoomr ", str(self.zoomr)	 	
		
	
	
	
	def StartAnim(self,tmessage,startpos,nextdemostate,length1,zoom1,zoom1R,move1R,length2,zoom2,zoom2R,move2R,length3,zoom3,zoom3R,move3R, colors = []):
	
	
		# Get and setup New Anim Parameters
		# Anim("Laser",(800,320),22,2,7000,-40,(-1,0),4,250,0,(-1,0),1.8,250,5,(-2,0)
		gstt.tmessage = ""
		print ""
		print "Text : ", tmessage
		self.Text(tmessage)
		self.Move(startpos[0],startpos[1])
		self.phases = ([length1,zoom1,zoom1R,move1R], [length2,zoom2,zoom2R,move2R], [length3,zoom3,zoom3R,move3R])
		self.nextdemostate = nextdemostate
		
		# Start with phase 0
		self.animstate = 0
		self.Anim(self.animstate)
		gstt.demostate = 200
		
                if (len(colors)==0):
                    #print("no color specified, keeping default :'(")
                    self.multicolor = False
                    self.tcolor = DEFAULT_COLOR
                elif (len(colors) == 1):
                    #print("a specific color")
                    self.multicolor = False
                    self.tcolor = colors[0]
                else:
                    #print("multicolors", colors)
                    self.multicolor = True
                    self.tcolor = colors
		
		
	def Anim(self,state):
	
	
		phase = self.phases[state]
		print "phase ", str(state), str(phase)
	
		
		# new Zoom and new dZoom
		self.Zoom(phase[1],phase[2])	
		self.MoveR(phase[3])
			
		self.animstate = state + 1
		
		
		# schedule starting new timer to switch next demo state:
		if self.animstate == 3:
			
			t = threading.Timer(phase[0], self.NextAnim, [self.nextdemostate])
			t.start() 


		else:
						
			# Schedule next anim phase after this phase length
			#print " starting new timer for next anim : ", str(self.animstate), str(self.phases[self.animstate])
			t = threading.Timer(phase[0], self.Anim, [self.animstate])
			t.start() 
			

	def NextAnim(self,state):	
		
						
			gstt.tmessage = ""
			if gstt.fs == GAME_FS_MENU:
					gstt.score.Reset()
					gstt.fs = GAME_FS_PLAY
					#gstt.demostate = state
	
			#print ("Next anim : switching to demostate ", str(state))
			gstt.demostate = state

			
			
			

			
	def Draw(self, f):
	
		message = gstt.tmessage	
										
		if gstt.tmessage <> "":
			self.DrawChars(f, message)
		
	def DrawChars(self,f , chars):


		self.viewer_distance += self.zoomr
				
		if self.viewer_distance < 250:
			 	self.viewer_distance = 250
		if self.viewer_distance > 8000:
			 	self.viewer_distance = 8000
			 	
		self.centerX += self.dX
		self.centerY += self.dY
		

		l = len(chars)
		i= 0		
		
		
		#f.LineTo((title_pos[0],title_pos[1]), 0x80000000)
		
		#self.angleX += 0.05
		self.angleY += 0.5
		#self.angleZ += 0.1
		
		
		for ch in chars:
			
			i +=1
			#print ch
                        if(ch == " "):
                            # Space doesn't need all those pretty calculations
                            print("space !")
                            #pass
                        else:

			#x_offset = 26 * (- (0.9*l) + 3-(2500*i))	
			
			#else:
			    x_offset = 26 * (- (0.9*l) + 3*i)						# texte centre en x automatiquement selon le nombre de lettres l
																	# texte en y selon text_pos dans globalVars
			#print x_offset
			
			    digit_pl_list = self.ASCII_GRAPHICS[ord(ch) - 47]
			
			    for pl in digit_pl_list:
			    	xy_list = []
				for xy in pl:
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
                                    try:
				        factor = self.fov / (self.viewer_distance + z)
                                    except:
                                        factor = 1
                                        #print("error, factor set to 1")
                                    #print("factor: " + str(factor) )
				    x = x * factor 
				    y = - y * factor
			
					
				    xy_list.append((self.centerX + x + x_offset,self.centerY + y))
					

                                if(self.multicolor):
                                    f.PolyLineOneColor(xy_list, self.tcolor[i-1])
                                else:
				    f.PolyLineOneColor(xy_list, self.tcolor)
		



	









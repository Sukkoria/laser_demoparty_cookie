# coding=UTF-8
'''
OneRay
Laser Tech Demo
By Sam Neurohack
LICENCE : CC

You get a basic pygame skeleton to handle the laser drawing with an onscreen simulator.
This Empty Laser is mainly a Laser Hexagon (see /tmp/lab github) structure with some extras, like alignement keys.

Many things are still in the todo list as how to store the align parameters in globalVars for the next run.

'''
print ""
print ""
print "GnomeDemo"
print "Initiate..."

import pygame
import math
import random
import itertools
import sys
import os
import thread
import threading

import time

import frame
from vectors import Vector2D
import renderer
import dac
from globalVars import *
#import sounds

# For MIDI
#import mido
#from Queue import Queue
#from threading import Thread
#import midi

#import pylibmc
#mc = pylibmc.Client(["127.0.0.1"], binary=True, behaviors={"tcp_nodelay": True, "ketama": True})


#import audio
#import osc
#from controller import setup_controls

# Import all objects generators


import gstt
import playertest
import points
import cube
import lastl
import score
import logo
import rotlogo
import ship
import track
import rotitlea
import spiral
import saber1
import saber2
import splines
import orbits
import butterfly
import grid
import smiley
import explode
import spikes
import clouds
import rainbow
import text
#import Hexaplopexa



#
# Subroutines
#

def StartMenu():

	print "StartMenu"
	gstt.fs = GAME_FS_MENU
	gstt.demostate = 0
	#gstt.lscore = 0
	#gstt.rscore = 0

	

def StartPlaying(first_time = False):

	
	gstt.score.Reset()
	gstt.fs = GAME_FS_PLAY
	
	#gstt.demostate = runningstate # Init in globalVars.py
        gstt.demostate = 10  # for test purposes !
	print ("switching to state : ", str(gstt.demostate))

	
def Animation(animstate, length, nextstate):


		print ""
		print "Animation :", str(animstate), " for ", str(length), " sec then demostate ", str(nextstate)
		 
		gstt.tmessage = ""
		
		gstt.demostate = animstate
		#print "demostate = ", str(animstate)
		
		t = threading.Timer(length, NextState, [nextstate])
		t.start() 		
		print "Animation !"


def NextState(state):
 	
 		print "switching to state : ", str(state)
 		gstt.demostate = state



	
def dac_thread():

	while True:
		try:

			d = dac.DAC(dac.find_first_dac())
			d.play_stream(laser)

		except Exception as e:
			
			#if etherIP <> "localhost":
				#import sys, traceback
				#print '\n---------------------'
				#print 'Exception: %s' % e
				#print '- - - - - - - - - - -'
				#traceback.print_tb(sys.exc_info()[2])
				#print "\n"
				pass

def DrawTestPattern(f):
	l,h = screen_size
	L_SLOPE = 30
	
	f.Line((0, 0), (l, 0), 0xFFFFFF)
	f.LineTo((l, h), 0xFFFFFF)
	f.LineTo((0, h), 0xFFFFFF)
	f.LineTo((0, 0), 0xFFFFFF)
	
	f.LineTo((2*L_SLOPE, h), 0)
	for i in xrange(1,7):
		c = (0xFF0000 if i & 1 else 0) | (0xFF00 if i & 2 else 0) | (0xFF if i & 4 else 0)
		f.LineTo(((2 * i + 1) * L_SLOPE, 0), c)
		f.LineTo(((2 * i + 2) * L_SLOPE, h), c)
	f.Line((l*.5, h*.5), (l*.75, -h*.5), 0xFF00FF)
	f.LineTo((l*1.5, h*.5), 0xFF00FF)
	f.LineTo((l*.75, h*1.5), 0xFF00FF)
	f.LineTo((l*.5, h*.5), 0xFF00FF)
		
def Align(f):
	l,h = screen_size
	L_SLOPE = 30
	
	f.Line((0, 0), (l, 0), 0xFFFFFF)
	f.LineTo((l, h), 0xFFFFFF)
	f.LineTo((0, h), 0xFFFFFF)
	f.LineTo((0, 0), 0xFFFFFF)
	laser = renderer.LaserRenderer(fwork_holder, gstt.centerx, gstt.centery, gstt.zoomx, gstt.zoomy, gstt.sizex, gstt.sizey)

	print str(gstt.centerx) + "," + str(gstt.centery) + "," + str(gstt.zoomx) + "," + str(gstt.zoomy) + "," + str(gstt.sizex) + "," + str(gstt.sizey)
	

app_path = os.path.dirname(os.path.realpath(__file__))


#
# Inits
#


# Pygame init


pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Bwarg!")
clock = pygame.time.Clock()

# Get variables (from globalvariables.py)
gstt.centerx = LASER_CENTER_X
gstt.centery = LASER_CENTER_Y
gstt.zoomx = LASER_ZOOM_X
gstt.zoomy = LASER_ZOOM_Y
gstt.sizex = LASER_SIZE_X
gstt.sizey = LASER_SIZE_Y
gstt.finangle = LASER_ANGLE


# WIPEOUT Variables

gstt.shipX = 400
gstt.shipY = 570

gstt.shipXspeed = 10
gstt.trackspeed = 0.00
gstt.maxspeed = 0.04

turn = 0.0
newturn = [random.uniform(-20.0,20.0),200]
turnsteps = newturn[1]
turnshift = (newturn[0] - turn) / turnsteps
gstt.lscore = 0

# Laser handler init

fwork_holder = frame.FrameHolder()
laser = renderer.LaserRenderer(fwork_holder, gstt.centerx, gstt.centery, gstt.zoomx, gstt.zoomy, gstt.sizex, gstt.sizey)

thread.start_new_thread(dac_thread, ())


update_screen = False


# All laser object generators init 

gstt.score = score.Score()
gstt.score.Reset()
#gstt.score2.Reset()

gstt.plyr = playertest.PlayerTest()

gstt.cb = cube.Cube()
gstt.cb.Change(0,0,0)

#gstt.lastl = lastl.LASTL()
#gstt.lastl.Project()

gstt.ship = ship.Ship()
gstt.trck = track.Track()
gstt.ship.Move(gstt.shipX,gstt.shipY)
gstt.trck.Speed(gstt.trackspeed)
gstt.ship.Change(4022,3780,3780)
gstt.trck.Turn(turn)

gstt.sprl = spiral.Spiral()
gstt.spln = splines.Splines()

gstt.sbr1 = saber1.Saber1()
gstt.sbr2 = saber2.Saber2()
gstt.sbr1.Change(0,0,0)
gstt.sbr2.Change(10,10,10)
gstt.sbr1.Move(-50 + screen_size[0] / 2, screen_size[1] / 2)
gstt.sbr2.Move(50 + screen_size[0] / 2, screen_size[1] / 2)

gstt.grdbtt = grid.Grid(screen_size[1]/2., "floor") #Should be <2.
gstt.grdbtt_sm = grid.Grid(screen_size[1]/1.5, "floor") #Should be <2.
gstt.grdup = grid.Grid(screen_size[1]/2, "ceiling")
gstt.grdrght = grid.Grid(screen_size[0]/1.5, "rightwall")
gstt.grdlft = grid.Grid(screen_size[0]/1.5, "leftwall")

gstt.xpld = explode.Explode((0,0), "up", 0xFF000)
gstt.xpld2 = explode.Explode((screen_size[0]/2,screen_size[1]/3), "up", 0xFF000)

gstt.show_grid_and_message = False
gstt.max_blink_my_game = 3
gstt.iter_blink_my_game = 0
gstt.show_a_game_and_lines = False

gstt.dvlsml = smiley.Smiley("devil", (screen_size[0]/2, screen_size[1]/2), 250)
gstt.max_devil_smiley = 50
gstt.iter_devil_smiley = 0

gstt.max_two_walls = 100
gstt.iter_two_walls = 0

gstt.spk = spikes.Spikes(7, screen_size[1]/1.5, 100, "horiz")
gstt.spk2 = spikes.Spikes(5, screen_size[1]/3, 100, "horiz")
gstt.max_spikes = 100
gstt.iter_spikes = 0

##gstt.hx = hexa.Hexa(50, 0xFF00FF)

gstt.rbw = rainbow.Rainbow(screen_size[1]/2, "floor")
gstt.max_rainbow = 100
gstt.iter_rainbow = 0

gstt.cldI = clouds.Clouds((50, 350),100, "I", 0xFFFFFF)

gstt.cldT = clouds.Clouds((250, 250),100, "T", 0xFFFFFF)
gstt.cldI2 = clouds.Clouds((450, 550),100, "I", 0xFFFFFF)

gstt.max_clouds = 150
gstt.iter_clouds = 0
#gstt.txt = text.Text("The end", 0xFF0000)

#gstt.logo = logo.Logo()
gstt.orbits = orbits.Orbits()
gstt.bttrfl = butterfly.Butterfly()
gstt.tmessage = ""
gstt.rttla = rotitlea.Title()

mydemo_titlepos_loading = (screen_size[0]/6, screen_size[1]/2)
mydemo_titlepos_4letters = (screen_size[0]/3, screen_size[1]/4)
mydemo_titlepos_2letters = (screen_size[0]/2.5, screen_size[1]/4)

#
# Almost running...
#

# Select with demostate to use after menu at launch

StartMenu()
	
keystates = pygame.key.get_pressed()
print("")
print("Starting...")
print "State after title : ", str(runningstate)


#
# Main loop
#

while gstt.fs != GAME_FS_QUIT:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gstt.fs = GAME_FS_QUIT
	
	keystates_prev = keystates[:]
	keystates = pygame.key.get_pressed()[:]

	# Game Menu

	if gstt.fs == GAME_FS_MENU:
	
		if keystates[pygame.K_ESCAPE] and not keystates_prev[pygame.K_ESCAPE]:
			gstt.fs = GAME_FS_QUIT
			print "ESCAPE : STOP AFTER CURRENT SCHEDULED TASKS"
			
		elif keystates[pygame.K_SPACE] and not keystates_prev[pygame.K_SPACE]:
			StartPlaying(True)
			
		if gstt.tmessage <> "Loading...":
                    # Text, pos,next demostate, lenght 
                        gstt.show_grid_and_message = True
			gstt.rttla.StartAnim("Loading...",mydemo_titlepos_loading,10,2,500,-80,(0,0),4,0,0,(0,0),0,0,0,(0,0))

			
			
	# Game Play
		
	elif gstt.fs == GAME_FS_PLAY:
		# Escape vers menu
	
		if keystates[pygame.K_ESCAPE] and not keystates_prev[pygame.K_ESCAPE]:
			print "ESCAPE : STOPPING AFTER CURRENT SCHEDULED TASKS"
			StartMenu()
			
		# anim playertest
	
		up_key = keystates[pygame.K_UP]
		down_key = keystates[pygame.K_DOWN]
		left_key = keystates[pygame.K_LEFT]
		right_key = keystates[pygame.K_RIGHT]
		
		#gstt.plyr.Move(up_key,down_key,left_key,right_key)
				
                # state 10 : Grid + Messages
		if gstt.demostate == 10: # Lets
		    gstt.rttla.StartAnim("Lets",mydemo_titlepos_4letters,11,
                            2,500,-80,(0,0),
                            4,0,0,(0,0),
                            0,0,0,(0,0))
	            gstt.grdbtt.Compute()			
                    pass
                if gstt.demostate == 11: # Play
		    gstt.rttla.StartAnim("play",mydemo_titlepos_4letters,12,
                            2,500,-80,(0,0),
                            4,0,0,(0,0),
                            0,0,0,(0,0))
	            gstt.grdbtt.Compute()			
                    pass
                if gstt.demostate == 12: # A game
		    gstt.rttla.StartAnim("a game",mydemo_titlepos_4letters,13,
                            0.3,500,-80,(0,0),
                            4,0,0,(0,0),
                            0,0,0,(0,0))
                    pass
                if gstt.demostate == 13:
                    gstt.show_a_game_and_lines = True
		    gstt.rttla.StartAnim("a game",mydemo_titlepos_4letters,14,
                            1.7,500,-80,(0,0),
                            4,0,0,(0,0),
                            0,0,0,(0,0)) 
                    pass
                if gstt.demostate == 14:
                    if(gstt.iter_blink_my_game <gstt.max_blink_my_game):
                        gstt.show_a_game_and_lines = False
                        gstt.iter_blink_my_game += 1
                        next_demostate = 15
                    else:
                        gstt.iter_blink_my_game = 0
                        next_demostate = 17
		    gstt.rttla.StartAnim("my game",mydemo_titlepos_4letters,next_demostate,
                            0.1,500,-80,(0,0),
                            4,0,0,(0,0),
                            0,0,0,(0,0))
                    pass

                if gstt.demostate == 15: # My game
		    gstt.rttla.StartAnim("my game",mydemo_titlepos_4letters,14,
                            0.1,500,-80,(0,0),
                            0,0,0,(0,0),
                            0,0,0,(0,0),
                            [0xFF00000,0xFF0000, 0x000000, 0xFFFFFF, 0xFFFFFF, 0xFFFFFF, 0xFFFFFF])
	            gstt.grdbtt.Compute()			
                    pass
                if gstt.demostate == 17: # Smiley !
                    if(gstt.iter_devil_smiley < gstt.max_devil_smiley):
                        gstt.iter_devil_smiley +=1
                    else:
                        gstt.iter_devil_smiley = 0 # To change demostate when drawing
                    pass 

                if gstt.demostate == 20: # Two walls + player !
                    gstt.plyr.SetPosition(screen_size[0]/2, gstt.iter_two_walls*screen_size[1]/gstt.max_two_walls)
                    gstt.grdrght.Compute()
                    gstt.grdlft.Compute()
                    if(gstt.iter_two_walls < gstt.max_two_walls):
                        gstt.iter_two_walls += 1
                    else:
                        gstt.iter_two_walls = 999
                    pass

                if gstt.demostate == 22:
                    if(gstt.iter_two_walls < gstt.max_two_walls):
                        gstt.iter_two_walls += 1
                    else:
                        gstt.iter_two_walls = 999
                    gstt.xpld.SetImpact((screen_size[0]/2,screen_size[1]))
                    gstt.xpld.SetColor(0xFFFF00)
                    if(gstt.iter_two_walls%2==0):
                        gstt.grdrght.SetColor(0xFFFF00)
                        gstt.grdlft.SetColor(0xFFFFFF)
                    else:
                        gstt.grdrght.SetColor(0xFFFFFF)
                        gstt.grdlft.SetColor(0xFFFF00)
                    gstt.grdrght.Compute()
                    gstt.grdlft.Compute()
                    gstt.xpld.Compute()
                    pass

                if gstt.demostate == 24:
                    if(gstt.iter_spikes<gstt.max_spikes):
                        gstt.iter_spikes += 1
                        gstt.plyr.SetPosition(screen_size[0]/2, screen_size[1]-gstt.iter_spikes*2)
                        #gstt.plyr.SetColor(0xFFFF00)
                    elif (gstt.iter_spikes == gstt.max_spikes):
                        gstt.iter_spikes += 1
                        print("change player color")
                        gstt.plyr.SetColor(0xFF0000)
                        gstt.spk.SetColor(0xFF0000)
                    elif(gstt.iter_spikes<gstt.max_spikes*1.5):
                        gstt.iter_spikes +=1
                        gstt.plyr.SetPosition(screen_size[0]/2, screen_size[1]-gstt.iter_spikes*2)
                        #gstt.plyr.SetColor(0xFFFF00)
                        #gstt.plyr.SetColor(0xFF0000)
                    else:
                        gstt.iter_spikes = 999
                    gstt.spk.Compute()
                    #gstt.spk2.Compute()


                if gstt.demostate == 30:
                    if (gstt.iter_clouds<gstt.max_clouds):
                        gstt.iter_clouds += 1
                        # init new player pos 
                        init_x = 50
                        init_y = screen_size[1]
                        end_y = 350 # Data from cldI
                        gstt.plyr.SetPosition(init_x, screen_size[1] - gstt.iter_clouds*(init_y - end_y)/gstt.max_clouds)
                        gstt.plyr.SetColor(0xFFAAAA)

                    else:
                        gstt.iter_clouds = 999
                    gstt.cldI.Compute()

                if gstt.demostate == 31:
                    if (gstt.iter_clouds<gstt.max_clouds):
                        gstt.iter_clouds += 1
                        # init new player pos 
                        init_x = 250
                        init_y = screen_size[1]
                        end_y = 250 # Data from cldI
                        gstt.plyr.SetPosition(init_x, screen_size[1] - gstt.iter_clouds*(init_y - end_y)/gstt.max_clouds)
                    else:
                        gstt.iter_clouds = 999
                    gstt.cldI.Compute()
                    gstt.cldI.ComputeRain()
                    gstt.cldT.Compute()

                if gstt.demostate == 32:
                    if (gstt.iter_clouds<gstt.max_clouds):
                        gstt.iter_clouds += 1
                        # init new player pos 
                        init_x = 450
                        init_y = screen_size[1]
                        end_y = 550 # Data from cldI
                        gstt.plyr.SetPosition(init_x, screen_size[1] - gstt.iter_clouds*(init_y - end_y)/gstt.max_clouds)
                    else:
                        gstt.iter_clouds = 999
                    gstt.cldI.Compute()
                    gstt.cldI.ComputeRain()
                    gstt.cldT.Compute()
                    gstt.cldT.ComputeRain()
                    gstt.cldI2.Compute()
                if gstt.demostate == 33:
                    if (gstt.iter_clouds<gstt.max_clouds):
                        gstt.iter_clouds += 1
                    else:
                        gstt.iter_clouds = 999
                    gstt.cldI.Compute()
                    gstt.cldI.ComputeRain()
                    gstt.cldT.Compute()
                    gstt.cldT.ComputeRain()
                    gstt.cldI2.Compute()
                    gstt.cldI2.ComputeRain()

                #if gstt.demostate == 35:
                    #pass # All code is in Draw
                

                if gstt.demostate == 40:
                    if (gstt.iter_rainbow<2*gstt.max_rainbow):
                        gstt.iter_rainbow += 1
                        #print ("rbw", gstt.iter_rainbow)
                        # init new player pos 
                        init_x = screen_size[0]/2
                        tmp_x = 0
                        if (gstt.iter_rainbow % 2 == 0):
                            tmp_x = - 100/gstt.iter_rainbow
                        else: 
                            tmp_x = 100/gstt.iter_rainbow

                        init_y = screen_size[1]
                        end_y = screen_size[1]/2
                        tmp_x_2 = (init_x + tmp_x)/2 + random.randint(0, screen_size[0])/2
                        tmp_y_2 = screen_size[1] - (init_y - end_y)*gstt.iter_rainbow/(gstt.max_rainbow*2) 
                        + random.randint(0,screen_size[1])/2
                        gstt.plyr.SetPosition(tmp_x_2, tmp_y_2)
                    else:
                        gstt.iter_rainbow = 999
                    gstt.plyr.SetColor(0xFFFFFF)
                    gstt.rbw.Compute()

                if gstt.demostate == 42:
                    if (gstt.iter_rainbow < gstt.max_rainbow):
                        gstt.iter_rainbow += 1
                        gstt.xpld2.SetColor("random")
                    else:
                        gstt.xpld2.SetColor("random")
                        gstt.iter_rainbow = 666

                    gstt.rbw.Compute()
                    gstt.xpld2.Compute()
                    pass
                if gstt.demostate == 69:
                    print("The end")
                    
                    #gstt.NextState(70)
                    #Animation(69, 30, 70)
                    pass
                #if gstt.demostate == 70:
		    #gstt.rttla.StartAnim("Thanks!",mydemo_titlepos_4letters,next_demostate,
                            #0.1,500,-80,(0,0),
                            #4,0,0,(0,0),
                            #0,0,0,(0,0), 
                            #[0xFF0000])
                    #pass

	elif gstt.fs == GAME_FS_GAMEOVER:

		if keystates[pygame.K_SPACE] and not keystates_prev[pygame.K_SPACE]:
			StartPlaying(False)

		elif keystates[pygame.K_ESCAPE] and not keystates_prev[pygame.K_ESCAPE]:
			StartMenu()
		



	# DISPLAY management

	# On efface l'ecran avant + Création de la nouvelle frame vide où les objets du jeu vont dessiner
	
	screen.fill(0)
	fwork = frame.Frame()
	
	# Alignement Case
	
	if keystates[pygame.K_p]:
		DrawTestPattern(fwork)
		
	if keystates[pygame.K_x]:
		Align(fwork)
		
	if keystates[pygame.K_r]:
		gstt.centerx += 20
		Align(fwork)

	if keystates[pygame.K_t]:
		gstt.centerx -= 20
		Align(fwork)
		
	if keystates[pygame.K_y]:
		gstt.centery += 20
		Align(fwork)

	if keystates[pygame.K_u]:
		gstt.centery -= 20
		Align(fwork)

	if keystates[pygame.K_f]:
		gstt.zoomx += 0.1
		Align(fwork)

	if keystates[pygame.K_g]:
		gstt.zoomx -= 0.1
		Align(fwork)
		
	if keystates[pygame.K_h]:
		gstt.zoomy += 0.1
		Align(fwork)

	if keystates[pygame.K_j]:
		gstt.zoomy -= 0.1
		Align(fwork)
	
	if keystates[pygame.K_c]:
		gstt.sizex -= 50
		Align(fwork)
		
	if keystates[pygame.K_v]:
		gstt.sizex += 50
		Align(fwork)
		
	if keystates[pygame.K_b]:
		gstt.sizey -= 50
		Align(fwork)
		
	if keystates[pygame.K_n]:
		gstt.sizey += 50
		Align(fwork)
		
	if keystates[pygame.K_l]:
		gstt.finangle -= 0.001
		Align(fwork)
		
	if keystates[pygame.K_m]:
		gstt.finangle += 0.001
		Align(fwork)

	else:


		display_plyr = gstt.fs == GAME_FS_PLAY or gstt.fs == GAME_FS_GAMEOVER  or gstt.fs == GAME_FS_MENU
		if display_plyr:
		
                        print("[+] " + str(gstt.demostate))
                        if gstt.demostate == 10:
                                gstt.plyr.Draw(fwork)

                        if gstt.demostate == 17:
                            gstt.dvlsml.Draw(fwork)
                            #print("devil")
                            if(gstt.iter_devil_smiley==0):
                                gstt.show_grid_and_message == False
                                gstt.demostate = 20
                        if gstt.demostate == 20:
                            gstt.grdrght.Draw(fwork)
                            gstt.grdlft.Draw(fwork)
                            gstt.plyr.Draw(fwork)
                            
                            if(gstt.iter_two_walls == 999):
                                gstt.demostate = 22
                                gstt.iter_two_walls = 0

                        if gstt.demostate == 22:
                            gstt.grdrght.Draw(fwork)
                            gstt.grdlft.Draw(fwork)
                            gstt.xpld.Draw(fwork)
                            if(gstt.iter_two_walls == 999):
                                gstt.demostate = 24

                        if gstt.demostate == 24:
                            gstt.plyr.Draw(fwork)

                            if (gstt.iter_spikes>gstt.max_spikes and gstt.iter_spikes%2==0):
                                pass
                            else:
                                gstt.spk.Draw(fwork)

                            if (gstt.iter_spikes == 999):
                                gstt.demostate = 30

                        if gstt.demostate == 30:
                            gstt.cldI.Draw(fwork)
                            gstt.plyr.Draw(fwork)
                            if (gstt.iter_clouds == 999):
                                gstt.demostate = 31
                                gstt.iter_clouds = 0

                        if gstt.demostate == 31:
                            gstt.cldI.Draw(fwork)
                            gstt.cldI.DrawRain(fwork)
                            gstt.cldT.Draw(fwork)
                            gstt.plyr.Draw(fwork)
                            if (gstt.iter_clouds == 999):
                                gstt.demostate = 32
                                gstt.iter_clouds = 0

                        if gstt.demostate == 32:
                            gstt.cldI.Draw(fwork)
                            gstt.cldI.DrawRain(fwork)
                            gstt.cldT.Draw(fwork)
                            gstt.cldT.DrawRain(fwork)
                            gstt.cldI2.Draw(fwork)
                            gstt.plyr.Draw(fwork)
                            if (gstt.iter_clouds == 999):
                                gstt.demostate = 33
                                gstt.iter_clouds = 0
                        if gstt.demostate == 33:
                            gstt.cldI.Draw(fwork)
                            gstt.cldI.DrawRain(fwork)
                            gstt.cldT.Draw(fwork)
                            gstt.cldT.DrawRain(fwork)
                            gstt.cldI2.Draw(fwork)
                            gstt.cldI2.DrawRain(fwork)
                            if (gstt.iter_clouds == 999):
                                gstt.demostate = 40
                                gstt.iter_clouds = 0
                        
                        #if gstt.demostate == 35:
                            #gstt.hx.Draw(fwork)

                        if gstt.demostate == 40:
                            #print("rbw", gstt.iter_rainbow)
                            gstt.rbw.Draw(fwork)
                            gstt.plyr.Draw(fwork)
                            if (gstt.iter_rainbow == 999):
                                gstt.demostate = 42
                                gstt.iter_rainbow = 0
                        if gstt.demostate == 42:
                            gstt.rbw.Draw(fwork)
                            gstt.xpld2.Draw(fwork)
                            if (gstt.iter_rainbow == 666):
                                gstt.demostate = 69
                                gstt.iter_rainbow = 0
                        if gstt.demostate == 69: # The end
                            #gstt.txt.Draw(fwork)
                            gstt.dvlsml.Draw(fwork)
                        #if gstt.demostate == 70: # End credits 17

			if  gstt.demostate == 200:						# 200 : Display title animation
				gstt.rttla.Draw(fwork)
                                #print(gstt.tmessage)
                                if(gstt.show_grid_and_message):
                                    gstt.grdbtt.Draw(fwork)
                                if(gstt.show_a_game_and_lines):
                                    fwork.Line((screen_size[0]/6,200), (screen_size[0]/3, 100), 0xFF0000) 
                                    fwork.Line((screen_size[0]/3,200),(screen_size[0]/6,100), 0xFF0000) 
				
				
				
			if  gstt.demostate == 110:						# 110 : Add countdown each Wipeout race beginning
				gstt.ttl.Draw(fwork)
				
			if  gstt.demostate == 120:						# 120 : LightSaber Dance with OSC control
				gstt.sbr1.Draw(fwork)
				gstt.sbr2.Draw(fwork)
				
			if gstt.fs == GAME_FS_MENU:
				gstt.rttla.Draw(fwork)	
	
	# Affecter la frame construite à l'objet conteneur de frame servant au système de rendu par laser
	
	
	fwork_holder.f = fwork
	#fwork.RenderScreen(screen)
	#pygame.display.flip() # Necessary to avoid blinking

	if update_screen:
		update_screen = False
		fwork.RenderScreen(screen)
		pygame.display.flip()
	else:
		update_screen = True

	
	# TODO : rendre indépendante la fréquence de rafraîchissement de l'écran par
	# rapport à celle de l'animation du jeu
	clock.tick(100)

pygame.quit()



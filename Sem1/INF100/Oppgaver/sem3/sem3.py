#!/usr/bin/env python3

"""
This is a simple Mario game.

Author: Hakon Tjeldnes
Last edited: October 2019
"""

import sys
import random
import time
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, NW

# Definse size of board and other constants
# NOTE: Change STEP_SIZE if your board does not show correctly in window
BOARD_WIDTH = 675# In points px
BOARD_HEIGHT = 770# In points px
INFO_HEIGHT = 40 # Top info board in points px
STEP_SIZE = 30 # Size of objects in points px
MAX_RAND_POS = int(BOARD_WIDTH / STEP_SIZE) # If you want random spawns
NAMING = { # Naming from map to full name, add here if you want more
                'M': "mario",
                'P': "peach",
                'B': "bowser",
                'G': "goomba",
                'K': "koopa",
                'C': "cap",
                'L': "mushroom",
                'V': "wall",
                'Y': "wall",
                'T': "gate"
            }

################### START HERE   -> #########################################

# 2
PICTURES = { # Naming from map to image path
                'M' : "gameImages/mario.png",
                'P' : "gameImages/peach.png",
                'B' : "gameImages/bowser.png",
                'G' : "gameImages/goomba.png",
                'K' : "gameImages/koopa.png",
                'C' : "gameImages/cap.png",
                'L' : "gameImages/mushroom.png",
                'V' : "gameImages/wall.png",
                'Y' : "gameImages/wall.png",
                'T' : "gameImages/gate.png",
                'H' : "gameImages/jumpingMario.png"
        }

# 1

def gameOverText(score):
    """
    Small function that takes the score variable as input, returns a message
    for the user including the score when the game ends.
    """
    return "Game over with score %s" % score
    
# 3
def go(key):
    """
    This function has key as input, which holds the value of the key you
    just pressed. The function then uses if loop to check if the pressed key
    was w, a, s, d or h, and changes the x and y value depending on which key
    was pressed. It then returns the x and y value.
    
    """
    
    if key == "w":
        x = 0
        y = -STEP_SIZE
    elif key == "s":
        x = 0
        y = STEP_SIZE
    elif key == "a":
        x = -STEP_SIZE
        y = 0
    elif key == "d":
        x = STEP_SIZE
        y = 0
    elif key == "h":
        x = 0
        y = 0
            
    return(x,y)
    
# 4
def readFile(filename):
    """
    Function that opens the requested file and iterates over every object
    in the txt file. It will then place the row and column value of the 
    different letters in different positions, in the txt file, and places 
    the row and column value as the key in a dictionary, and the letter itself
    as value. Returns the finished dictionary.
    """
    letters = {}
    with open(filename) as f:
        for line,text in enumerate(f):
            for pos, char in enumerate(text.strip()):
                if char != " ": 
                    letters[(pos,line)] = char 
    return letters

# 5
    
def nextStep(x1, y1, x2, y2, moveX, moveY):
    """
    Function that checks the value of input variables x1, x2, y1 and y2 
    and increases them with moveX or moveY. Return the new x and y values.
    """
    x1 += moveX
    x2 += moveX
    y1 += moveY
    y2 += moveY
       
    return x1, y1, x2, y2

def main():

    root = Tk() # Start graphics  window
    MarioGame("level1.txt") # Start Mario Game graphics inside root window
    root.mainloop() # Run graphics loop

########## Graphical user interface, touch at your own peril! ################

# INFO: This is a class, just like the class of people, we can instantiate 
# you and me as objects of class people.
#    
# self means (this sdobject within the instance of class), like I am my self of 
# class people.
# self.item must be defined in class, so self.item for level1.txt will be
# different than self.item for level2.txt.
# About classes: https://www.geeksforgeeks.org/self-in-python-class/
# TkInter documentation: https://docs.python.org/3/library/tk.html
class Board(Canvas):

    def __init__(self, level): # Python class initiation function
        super().__init__(width=BOARD_WIDTH, height=BOARD_HEIGHT,
            background="black", highlightthickness=0)

        self.initGame(level)
        self.pack()


    def initGame(self, level):
        '''initializes game'''

        self.inGame = True # TRUE = Not finished
        self.hasCap = False # super power
        self.jumping = False # is jumping or not
        self.jumptime = 0 # Store time when jump started here
        self.life  = 3 # Current number of lives
        self.score = 0 # Current score

        # variables used to move Mario object
        self.moveX = 0 # relative x direction coordinate
        self.moveY = 0 # relative y direction coordinate
        # load map
        game_map = readFile(level) # Read in map
        self.imagesDict = self.loadImages()
        self.createObjects(game_map)
        # Make key interupt binder
        self.bind_all("<Key>", self.onKeyPressed)
        # Debug specter mode
        self.specterMode = False # press ctrl + s to change to True
        # If you want a timer interrupt: self.after(DELAY, self.onTimer)
        # Then define function: onTimer(self): do stuff


    def loadImages(self):
        '''loads images from the disk'''

        try: # All possible images here
            imagesDict = {}
            for key in PICTURES:
                imagesDict[key] = self.loadImage(PICTURES[key])

            # Special case for jumping mario
            self.jmario = self.loadImage("gameImages/jumpingMario.png")
            return imagesDict

        except IOError as e:

            print(e)
            sys.exit(1)

    def loadImage(self, path):
        '''loads single image from the disk'''
        openImg = Image.open(path)
        openImg = openImg.resize((STEP_SIZE, STEP_SIZE), Image.ANTIALIAS)
        return(ImageTk.PhotoImage(openImg))

    def createObjects(self, game_map):
        '''creates objects on Canvas'''

        # Create score board
        self.create_text(30, 10, text="Score: {0}".format(self.score),
                         tag="score", fill="white")
        self.create_text(30, 30, text="Life: {0}".format(self.life),
                         tag="life", fill="white")
        # Create map
        for i in game_map: 
            map_type = game_map[i]
            xCoord = i[0]*STEP_SIZE
            yCoord = INFO_HEIGHT + i[1]*STEP_SIZE
            
            if map_type == "M": # special case to hide jumping mario under mario
                self.create_image(xCoord, yCoord, image=self.jmario,
                                  anchor=NW, tag="jmario", state="hidden")
                
            self.create_image(xCoord, yCoord, image=self.imagesDict[map_type],
            anchor=NW, tag=NAMING[map_type])
            
    def getCurrentMario(self):
        ''' Get normal or jumping mario id'''
        if self.jumping:
            return(self.find_withtag("jmario"))
        
        return(self.find_withtag("mario")) # normal mario


    def checkPeachCollision(self):
        '''checks if Mario collides with peach'''
        peach = self.find_withtag("peach")
        mario = self.getCurrentMario()
        x1, y1, x2, y2 = self.bbox(mario) # recatngle box around mario
        overlap = self.find_overlapping(x1, y1, x2, y2) # find overlaps
        
        for ovr in overlap: # Each that overlap mario
            for p in peach: # For each peach
                if p == ovr: # if peach is the overlap to mario
                    self.score += 10
                    self.delete(p)
                
    def checkMushromCollision(self):
        '''checks if Mario collides with mushroom'''

        mushroom = self.find_withtag("mushroom")
        mario = self.getCurrentMario()

        x1, y1, x2, y2 = self.bbox(mario)
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for ovr in overlap:
            for mush in mushroom:
                if mush == ovr:
                    self.life += 1
                    self.score += 1
                    self.delete(mush)
    
    def checkCapCollision(self):
        '''checks if Mario collides with cap'''
        caps = self.find_withtag("cap")
        mario = self.getCurrentMario()

        x1, y1, x2, y2 = self.bbox(mario)
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for ovr in overlap:
            for c in caps:
                if c == ovr:
                    self.score += 2
                    self.hasCap = True
                    self.delete(c)
    
    def checkFightCollision(self):
        '''checks if Mario collides with enemy'''
        koopa = self.find_withtag("koopa")
        goomba = self.find_withtag("goomba")
        bowser = self.find_withtag("bowser")
        mario = self.getCurrentMario()
        x1, y1, x2, y2 = self.bbox(mario)
        # BONUS: make fight happen with nextStep(), so enemy dies correct, and
        # not the step after you go on it.
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for k in koopa: # For koopas
            for ovr in overlap:
                if k == ovr:
                    print("fight")
                    if self.jumping:
                        self.score += 2
                        self.delete(k)
                    else:
                        print("loss life")
                        self.life -= 1
        for g in goomba: # For goombas
            for ovr in overlap:
                if g == ovr:
                    print("fight")
                    if self.jumping:
                        self.score += 1
                        self.delete(g)
                    else:
                        print("loss life")
                        self.life -= 1
        for b in bowser: # For bowser
            for ovr in overlap:
                if b == ovr:
                    print("fight")
                    if self.jumping and self.hasCap:
                        self.score += 5
                        self.delete(b)
                        gates = self.find_withtag("gate")
                        for gate in gates:
                            self.delete(gate)
                    else:
                        print("loss life")
                        self.life -= 2
        

    def moveMario(self):
        '''moves the Mario object'''        
        mario = self.find_withtag("mario")
        jmario = self.find_withtag("jmario") # jumping mario
        self.move(mario, self.moveX, self.moveY) # internal move function
        self.move(jmario, self.moveX, self.moveY) # internal move function
        
    def validStep(self): # <- True to go through walls
        '''checks for wall collisions'''
        walls = self.find_withtag("wall")
        walls = walls + self.find_withtag("gate")
        mario = self.getCurrentMario()
        x1, y1, x2, y2 = self.bbox(mario)
        x1, y1, x2, y2 = nextStep(x1, y1, x2, y2, self.moveX, self.moveY)
        overlap = self.find_overlapping(x1, y1, x2, y2)
        if (not self.specterMode):
            for dot in walls:
               for over in overlap:
                    if over == dot:
                      return(False)
        
        # Check if you are finished and outside map    
        if y1 > BOARD_HEIGHT - STEP_SIZE:
            self.inGame = False
        return(True)

    def onKeyPressed(self, e):
        '''controls direction variables with cursor keys'''
        key = e.keysym
        self.moveX, self.moveY = go(key) # get direction to go
        
        if key == 'h': #if jump
            self.jump(True) # Set jump to True in jump function
        if self.jump and (time.time() - self.jumptime > 0.3): # finished jump
            self.jump(False) # Set jump to False in jump function
        
        if key == 'S': # Capital s only, shift + s
            self.specterMode = not self.specterMode
        
        if self.validStep(): # If valid step
            self.update() # Check for collisions
        
        if self.life <= 0: # if dead
            self.inGame = False
            self.gameOver()
            
    def jump(self, case):
        ''' Set or reset jump '''
        self.jumping = case
        self.jumptime = time.time()
        mario = self.find_withtag("mario")
        jmario = self.find_withtag("jmario")
        if self.jumping:
            self.itemconfig(jmario, state = "normal")
            self.itemconfig(mario, state = "hidden")
        else:
            self.itemconfig(jmario, state = "hidden")
            self.itemconfig(mario, state = "normal")

    def update(self):
        ''' Do all item collision checks and draw updates '''
        if self.inGame:
            self.moveMario()
            self.checkMushromCollision()
            self.checkPeachCollision()
            self.checkCapCollision()
            self.checkFightCollision()
            self.drawScore()
        else:
            self.gameOver()
                
    def drawScore(self):
        '''draws score and life'''

        score = self.find_withtag("score")
        self.itemconfigure(score, text="Score: {0}".format(self.score))
        life = self.find_withtag("life")
        self.itemconfigure(life, text="Life: {0}".format(self.life))

    def gameOver(self):
        '''deletes all objects and draws game over message'''

        self.delete(ALL) # Delete all objects in canvas
        self.create_text(self.winfo_width() /2, self.winfo_height()/2,
            text=gameOverText(self.score), fill="white")


class MarioGame(Frame):
    def __init__(self, level):
        super().__init__() # load init from super class

        self.master.title('Mario 8-bit') # Title of window
        self.board = Board(level)
        self.pack()

if __name__ == '__main__' and len(PICTURES) > 0: # Call main if true
    main() 
else: # Else  you have not done task 2 yet
   print("Define PICTURES before you can start") 

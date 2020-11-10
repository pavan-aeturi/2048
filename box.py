import pygame
from colors import *
class Tile():
    def __init__(self,x,y,width,height, Number=0,fontsize=55):
        self.color = TILE_COLOR[Number]
        self.x = x
        self.y = y-2
        self.width = width
        self.height = height
        self.Number = Number
        self.fontsize=fontsize

    def draw(self,win,outline=EDGE_COLOR):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-8,self.y-8,self.width+15,self.height+15),10,7)
        self.drawbox(win)

    def changeNumber(self,Number,win):
    	self.Number=Number
    	self.drawbox(win)

    def drawbox(self,win):
        self.color = TILE_COLOR[self.Number]
        pygame.draw.rect(win, self.color, (self.x-2,self.y-2,self.width+4,self.height+4),0,5)
        FONT_COLOR=[]
        if self.Number>=8:
        	FONT_COLOR=FONT_WCOLOR
        else:
        	FONT_COLOR=FONT_BCOLOR
        if self.Number != 0:
            font = pygame.font.SysFont('Clear Sans', self.fontsize)
            text = font.render(str(self.Number), 1,FONT_COLOR )
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        pygame.display.update()

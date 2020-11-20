import pygame
from colors import *
class displayBlock():
	def __init__(self,x,y,height,width,textColor,text,NumberColor,Number,background,textfontSize=10,numberfontSize=30):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text
		self.textColor=textColor
		self.NumberColor=NumberColor
		self.Number=Number
		self.background=background
		self.textfontSize=textfontSize
		self.numberfontSize=numberfontSize


	def draw(self,win,outline=None):
		#Call this method to draw the button on the screen
		# if outline:
		# 	pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0,5)
		pygame.draw.rect(win, WHITE, (self.x,self.y,self.width,self.height),0,5)
		pygame.draw.rect(win, self.background, (self.x,self.y,self.width,self.height),0,5)

		if self.text != '':
			font = pygame.font.SysFont('Clear Sans', self.textfontSize)
			fontNum = pygame.font.SysFont('Clear Sans', self.numberfontSize)
			textNum=fontNum.render(str(self.Number),1,self.NumberColor)
			text = font.render(self.text, 1, self.textColor)
			win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)/4))
			win.blit(textNum, (self.x + (self.width/2 - textNum.get_width()/2), self.y + (self.height/2)))

		pygame.display.update()
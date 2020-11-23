import pygame
from colors import *
from box import Tile
from pygame.locals import *
from time import sleep
from matrix import matrix
from displayBlock import displayBlock
from button import button

def EndorContinueGame(HighestScore,Mtx,window):
	sleep(1.0)
	window.fill(WHITE)
	if Mtx.winner:	
		template=button(FONT_WCOLOR,200,200,200,200,"You won",50)
		template.draw(window)
	else:
		template=button(FONT_WCOLOR,200,200,200,200,"You Loose",50)
		template.draw(window)

	Try_Again=button(BLUE,100,500,150,50,"Try Again",FONT_WCOLOR)
	Exit=button(BLUE,350,500,150,50,"Exit",FONT_WCOLOR)
	Try_Again.draw(window)
	Exit.draw(window)
	HighestScore.Number=max(HighestScore.Number,Mtx.score)
	while True:
		try:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					return False
				if event.type==pygame.MOUSEBUTTONDOWN:
					if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
						if Try_Again.isOver(pygame.mouse.get_pos()):
							return True
						elif Exit.isOver(pygame.mouse.get_pos()):
							return False
		except:
			return False

def initialiseScoreBoard(window):
	nextBestMove=displayBlock(100,85,50,120,DBBLOCK_BG_COLOR,"BEST MOVE",WHITE,"L",FONT_DBCOLOR,18)
	score=displayBlock(236,85,50,120,DBBLOCK_BG_COLOR,"SCORE",WHITE,0,FONT_DBCOLOR,20)
	HighestScore=displayBlock(370,85,50,120,DBBLOCK_BG_COLOR,"BEST",WHITE,0,FONT_DBCOLOR,20)
	return score,HighestScore,nextBestMove

def main(score,HighestScore,nextBestMove,window):
	window.fill(WHITE)
	Img2048=pygame.image.load('2048.png')
	Img2048small=pygame.transform.smoothscale(Img2048,(150,60))
	window.blit(Img2048small, (220, 10))
	pygame.display.update()
	pygame.draw.rect(window,EDGE_COLOR,BASE)
	run=True
	Mtx=matrix()
	Mtx.buildTiles(window)
	Mtx.checkAddandUpdate(window)
	score.Number=0
	score.draw(window)
	HighestScore.draw(window)
	back_cnt=0
	while run:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				return False
			if Mtx.gameover:
				run=False
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					Mtx.leftMove(window)
				elif event.key==pygame.K_RIGHT:
					Mtx.rightMove(window)
				elif event.key==pygame.K_UP:
					Mtx.upMove(window)
				elif event.key==pygame.K_DOWN:
					Mtx.downMove(window)
				elif event.key==pygame.K_SPACE:
					Mtx.restore(window)
			score.Number=Mtx.score
			score.draw(window)
			
		
	return EndorContinueGame(HighestScore,Mtx,window)


if __name__=="__main__":
	try:
		pygame.init()
		window = pygame.display.set_mode((600,650))
		pygame.display.set_caption("2048")
		pygame.display.update()
		pygame.display.flip()
		score,HighestScore,nextBestMove=initialiseScoreBoard(window)
		while main(score,HighestScore,nextBestMove,window):
			pass
		pygame.quit()
	except:
		pass

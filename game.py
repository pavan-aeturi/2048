import pygame
from colors import *
from box import Tile
from matrix import matrix
from button import button

def main():
	window.fill(WHITE)
	pygame.draw.rect(window,EDGE_COLOR,BASE)
	run=True
	Mtx=matrix()
	Mtx.buildTiles(window)
	Mtx.add_new_tile()
	Mtx.updateGui(window)

	while run:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
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



	while True:
		try:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					pygame.quit()
				if event.type==pygame.MOUSEBUTTONDOWN:
					if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
						if Try_Again.isOver(pygame.mouse.get_pos()):
							main()
						elif Exit.isOver(pygame.mouse.get_pos()):
							pygame.quit()
		except:
			break


if __name__== "__main__":
	try:
		pygame.init()
		window = pygame.display.set_mode((600,650))
		pygame.display.set_caption("2048")
		pygame.display.update()
		pygame.display.flip()
		main()
	except:
		pass

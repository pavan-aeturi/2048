from box import Tile
import pygame
import random
class matrix():
	def __init__(self,dimX=4,dimY=4):
		self.length=dimX
		self.height=dimY
		self.gameover=False
		self.maxTileVal=0
		self.winner=False
		self.score=0
		self.mtx=[[0 for i in range(4)] for _ in range(4)]
		self.tiles =[[None for i in range(4)] for _ in range(4)]
		self.Bmem=[ None for j in range(5)]
		self.Fcnt=0
		self.Bcnt=0
		self.Fmem=[ None for _ in range(5) ]

	def buildTiles(self,win):
		for i in range(self.height):
			for j in range(self.length):
				self.tiles[i][j]=Tile(100+j*100,175+i*100,85,85,self.mtx[i][j])
		self.drawTiles(win)

	def drawTiles(self,win):
		for i in range(self.height):
			for j in range(self.length):
				self.tiles[i][j].draw(win)

	def changeTileNum(self,i,j,num,win):
		self.tiles[i][j].changeNumber(num,win)

	def stackLeft(self):
		nmtx=[[0 for i in range(4) ] for _ in range(4)]
		for i in range(4):
			finalPos=0
			for j in range(4):
				if self.mtx[i][j]!=0:
					nmtx[i][finalPos]=self.mtx[i][j]
					finalPos+=1
		self.mtx=nmtx

	def combineLeft(self):
		for i in range(4):
			for j in range(3):
				if self.mtx[i][j]!=0 and self.mtx[i][j]==self.mtx[i][j+1]:
					self.mtx[i][j]*=2
					self.mtx[i][j+1]=0
					self.score+=self.mtx[i][j]

	def transpose(self):
		nmtx=[[0 for i in range(4) ] for _ in range(4)]
		for i in range(4):
			for j in range(4):
				nmtx[i][j]=self.mtx[j][i]
		self.mtx=nmtx

	def rotateHorizontal(self):
		nmtx=[[0 for i in range(4) ] for _ in range(4)]
		for i in range(4):
			for j in range(4):
				nmtx[i][j]=self.mtx[i][3-j]
		self.mtx=nmtx

	def add_new_tile(self):
		newList=[]
		for i in range(4):
			for j in range(4):
				if self.mtx[i][j]==0:
					newList.append(i*4+j)
		r=random.randint(0,len(newList)-1)
		k=random.choice([2,4])
		self.mtx[int(newList[r]/4)][int(newList[r]%4)]=k
		self.maxTileVal=max(k,self.maxTileVal)

	def updateGui(self,win):
		for i in range(4):
			for j in range(4):
				self.changeTileNum(i,j,self.mtx[i][j],win)

	def maxTileNum(self):
		for i in range(4):
			for j in range(4):
				self.maxTileVal=max(self.mtx[i][j],self.maxTileVal)

	def emptyAvailable(self):
		for i in range(4):
			for j in range(4):
				if self.mtx[i][j]==0:
					return True
		return False
	def checkEqualConsecutiveTiles(self):
		for i in range(4):
			for j in range(3):
				if self.mtx[i][j]==self.mtx[i][j+1]:
					return True
		for i in range(4):
			for j in range(3):
				if self.mtx[j][i]==self.mtx[j+1][i]:
					return True
		return False

	def checkAddandUpdate(self,win):
		self.maxTileNum()
		if self.emptyAvailable() and self.maxTileVal!=1024:
			self.add_new_tile()
			self.updateGui(win)
		else:
			self.gameover=((not self.checkEqualConsecutiveTiles()) or self.maxTileVal==1024)
			self.winner=(self.maxTileVal==1024)

	def storeMoves(self):
		self.Bmem[(self.Bcnt)%5]=self.mtx
		self.Bcnt=(self.Bcnt + 1)%5

	def restore(self,win):
		if self.Bmem[(self.Bcnt-2)%5] is not None:
			self.mtx=self.Bmem[(self.Bcnt-2)%5]
			self.updateGui(win)
			self.FMem=self.Bmem[(self.Bcnt-1)%5]
			self.Fcnt=(self.Fcnt+1)%5
			self.Bmem[(self.Bcnt-1)%5]=None
			self.Bcnt=(self.Bcnt - 1)%5

	def leftMove(self,win):
		self.stackLeft()
		self.combineLeft()
		self.stackLeft()
		self.storeMoves()
		self.checkAddandUpdate(win)

		
	def rightMove(self,win):
		self.rotateHorizontal()
		self.stackLeft()
		self.combineLeft()
		self.stackLeft()
		self.rotateHorizontal()
		self.storeMoves()
		self.checkAddandUpdate(win)

	def upMove(self,win):
		self.transpose()
		self.stackLeft()
		self.combineLeft()
		self.stackLeft()
		self.transpose()
		self.storeMoves()
		self.checkAddandUpdate(win)

	def downMove(self,win):
		self.transpose()
		self.rotateHorizontal()
		self.stackLeft()
		self.combineLeft()
		self.stackLeft()
		self.rotateHorizontal()
		self.transpose()
		self.storeMoves()
		self.checkAddandUpdate(win)






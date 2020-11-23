from box import Tile
from Node import Node
from moves import *
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
		self.presentNode=None
		self.mtx=[[0 for i in range(4)] for _ in range(4)]
		self.tiles =[[None for i in range(4)] for _ in range(4)]
		self.Bmem=[ None for j in range(6)]
		self.Bcnt=0

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
		if self.mtx:
			self.storeMoves()
		self.maxTileNum()
		if self.emptyAvailable() and self.maxTileVal!=2048:
			self.add_new_tile()
			self.updateGui(win)
		else:
			self.gameover=(not self.checkEqualConsecutiveTiles()) or (self.maxTileVal==2048)
			self.winner=(self.maxTileVal==2048)
				
	def storeMoves(self):
		self.Bmem[(self.Bcnt)%6]=Node(self.mtx,self.score)
		self.Bcnt=(self.Bcnt + 1)%6

	def restore(self,win):
		if self.Bmem[(self.Bcnt-2)%6] is not None:
			self.mtx=self.Bmem[(self.Bcnt-2)%6].mtx
			self.score=self.Bmem[(self.Bcnt-2)%6].score
			self.updateGui(win)
			self.Bmem[(self.Bcnt-1)%6]=None
			self.Bcnt=(self.Bcnt - 1)%6

	def leftMove(self,win):
		self.mtx,self.score=getLeft(self.mtx,self.score)
		self.checkAddandUpdate(win)

		
	def rightMove(self,win):
		self.mtx,self.score=getRight(self.mtx,self.score)
		self.checkAddandUpdate(win)

	def upMove(self,win):
		self.mtx,self.score=getUp(self.mtx,self.score)
		self.checkAddandUpdate(win)

	def downMove(self,win):
		self.mtx,self.score=getDown(self.mtx,self.score)
		self.checkAddandUpdate(win)







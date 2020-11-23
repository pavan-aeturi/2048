from box import Tile
from Node import Node
from moves import *
import pygame
import random


class matrix():
	def __init__(self,dimX=4,dimY=4):
		self.length=dimX
		self.height=dimY
		self.nextBestMove='L'
		self.gameover=False
		self.maxTileVal=0
		self.winner=False
		self.score=0
		self.d_score=0
		self.u_score=0
		self.l_score=0
		self.r_score=0
		self.presentNode=None
		self.mtx=[[0 for i in range(4)] for _ in range(4)]
		self.d_mtx=[[0 for i in range(4)] for _ in range(4)]
		self.u_mtx=[[0 for i in range(4)] for _ in range(4)]
		self.l_mtx=[[0 for i in range(4)] for _ in range(4)]
		self.r_mtx=[[0 for i in range(4)] for _ in range(4)]
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
		self.mtx,self.score=self.l_mtx,self.l_score
		self.checkAddandUpdate(win)
		self.bestMove()
		
	def rightMove(self,win):
		self.mtx,self.score=self.r_mtx,self.r_score
		self.checkAddandUpdate(win)
		self.bestMove()

	def upMove(self,win):
		self.mtx,self.score=self.u_mtx,self.u_score
		self.checkAddandUpdate(win)
		self.bestMove()

	def downMove(self,win):
		self.mtx,self.score=self.d_mtx,self.d_score
		self.checkAddandUpdate(win)
		self.bestMove()

	def bestMove(self):
		self.l_mtx,self.l_score=getLeft(self.mtx,self.score)
		self.r_mtx,self.r_score=getRight(self.mtx,self.score)
		self.u_mtx,self.u_score=getUp(self.mtx,self.score)
		self.d_mtx,self.d_score=getDown(self.mtx,self.score)

		l_sum = 0
		l_nz = 0
		r_sum = 0
		r_nz = 0
		u_sum = 0
		u_nz = 0
		d_sum = 0
		d_nz = 0
		cur_max = 0
		# print("---------------------------------------------------------")
		# print("if left\n")
		for i in range(4):
			for j in range(4):
				# print(self.l_mtx[i][j],end=" ")
				l_sum+=self.l_mtx[i][j]
				if self.l_mtx[i][j]!=0:
					l_nz+=1
			# print("\n")
		if l_sum/l_nz > cur_max:
			self.nextBestMove = "L"
			cur_max = l_sum/l_nz


		# print("if right\n")
		for i in range(4):
			for j in range(4):
				# print(self.r_mtx[i][j],end=" ")
				r_sum+=self.r_mtx[i][j]
				if self.r_mtx[i][j]!=0:
					r_nz+=1
			# print("\n")
		if r_sum/r_nz > cur_max:
			self.nextBestMove = "R"
			cur_max = r_sum/r_nz

		# print("if up\n")
		for i in range(4):
			for j in range(4):
				# print(self.u_mtx[i][j],end=" ")
				u_sum+=self.u_mtx[i][j]
				if self.u_mtx[i][j]!=0:
					u_nz+=1
			# print("\n")
		if u_sum /u_nz> cur_max:
			self.nextBestMove = "U"
			cur_max = u_sum/u_nz

		# print("if down\n")
		for i in range(4):
			for j in range(4):
				# print(self.d_mtx[i][j],end=" ")
				d_sum+=self.d_mtx[i][j]
				if self.d_mtx[i][j]!=0:
					d_nz+=1
			# print("\n")
		if d_sum/d_nz > cur_max:
			self.nextBestMove = "D"
			cur_max = d_sum/d_nz

		# print("best move is {} at rating {}".format(self.nextBestMove,cur_max))
		# print("---------------------------------------------------------")






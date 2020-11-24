from moves import *
import copy

class Node():
	def __init__(self,mtx,score=0,parent=None,depth=0,builddepth=0):
		self.mtx=mtx
		self.depth=depth
		self.totalSum=self.gettSum()
		self.score=score
		self.children=self.buildChildren(builddepth);
		self.parentNode=parent
		self.MaxTile=self.getMaxTile()
		self.numberCount=self.getListTiles()
		
	def gettSum(self):
		s=0
		for i in range(4):
			for j in range(4):
				s+=self.mtx[i][j]
		return s

	def getMaxTile(self):
		s=0
		for i in range(4):
			for j in range(4):
				s=max(s,self.mtx[i][j])
		return s

	def getListTiles(self):
		cCount={2:0 ,4:0,8:0,16:0,32:0,64:0,128:0,256:0,512:0,1024:0,2048:0}
		for i in range(4):
			for j in range(4):
				if self.mtx[i][j] != 0:
					cCount[self.mtx[i][j]]+=1
		return cCount

	def insertRandomTile(self,nmtx,depth):
		l=[]
		if depth >0 :
			for i in range(4):
				for j in range(4):
					if nmtx[i][j]==0:
						nmtx[i][j]=2
						l.append(Node(copy.deepcopy(nmtx),parent=self,depth=self.depth+1,builddepth=depth-1))
						nmtx[i][j]=4
						l.append(Node(copy.deepcopy(nmtx),parent=self,depth=self.depth+1,builddepth=depth-1))
						nmtx[i][j]=0
		return l

	def getLeftp(self,depth):
		nmtx=self.mtx
		nmtx,score=getLeft(nmtx,self.score)
		return self.insertRandomTile(nmtx,depth)

	def getRightp(self,depth):
		nmtx=self.mtx
		nmtx,score=getRight(nmtx,self.score)
		return self.insertRandomTile(nmtx,depth)
	def getUpp(self,depth):
		nmtx=self.mtx
		nmtx,score=getUp(nmtx,self.score)
		return self.insertRandomTile(nmtx,depth)

	def getDownp(self,depth):
		nmtx=self.mtx
		nmtx,score=getDown(nmtx,self.score)
		return self.insertRandomTile(nmtx,depth)

	def buildChildren(self,depth=0):
		dictMoves={'L':[],'R':[],'U':[],'D':[]}
		if depth>0:
			dictMoves['L']=self.getLeftp(depth)
			dictMoves['R']=self.getRightp(depth)
			dictMoves['U']=self.getUpp(depth)
			dictMoves['D']=self.getDownp(depth)

		return dictMoves


from Node import Node
from moves import *

class Tree():
	def __init__(self,mtx):
		self.root=Node(mtx,depth=2)
		self.presentNode=self.root

	def goToparent(self):
		if self.presentNode.parentNode:
			self.presentNode=self.presentNode.parentNode
		else:
			print("No parent found")

	def goTochild(self,S,n):
		try:
			self.presentNode=self.presentNode.children[S][n]
		except :
			print("No such child present with parameters given")


mtx=[[2,4 ,0, 0], [2,4,0,0],[0,4,0,0],[0,4,8,0]]
tree=Tree(mtx)
tree.goTochild('U',0)
tree.goTochild('L',0)
print(tree.presentNode.mtx)
tree.goToparent()
print(tree.presentNode.mtx)

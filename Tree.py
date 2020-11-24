from Node import Node

class Tree():
	def __init__(self,mtx):
		self.root=Node(mtx,depth=0,builddepth=0)
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


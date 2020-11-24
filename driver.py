from Node import Node
from moves import *
import random
from Tree import Tree


def search(root,sum,maxdepth=2):
    print(root.mtx)
    if root.totalSum==sum:
        print("found")
        return True
    if root.totalSum>sum or root.depth>=maxdepth:
        print("backtrack")
        return False
    else:
        root.children=root.buildChildren(1)
        l=list(root.children.keys())
        random.shuffle(l)
        for key in l:
            possibleStates=root.children[key]
            random.shuffle(possibleStates)
            for i in range(len(possibleStates)):
                print(key)
                if search(possibleStates[i],sum):
                    return True
        return False

def insert_tile(mtx):
	l=[]
	for i in range(4):
		for j in range(4):
			if mtx[i][j]==0:
				l.append([i,j])
	if len(l)>0:
		r=random.randint(0,len(l)-1)
		mtx[l[r][0]][l[r][1]]=random.choice([2,4])

def main():
	mtx=[[0 for _ in range(4)] for i in range(4)]
	insert_tile(mtx)
	insert_tile(mtx)
	tree=Tree(mtx)
	search(tree.root,8)

if __name__=="__main__":
	main()

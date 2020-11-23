def stackLeft(mtx):
		nmtx=[[0 for i in range(4) ] for _ in range(4)]
		for i in range(4):
			finalPos=0
			for j in range(4):
				if mtx[i][j]!=0:
					nmtx[i][finalPos]=mtx[i][j]
					finalPos+=1
		return nmtx

def combineLeft(mtx,score):
	for i in range(4):
		for j in range(3):
			if mtx[i][j]!=0 and mtx[i][j]==mtx[i][j+1]:
				mtx[i][j]*=2
				mtx[i][j+1]=0
				score+=mtx[i][j]
	return mtx,score

def transpose(mtx):
	nmtx=[[0 for i in range(4) ] for _ in range(4)]
	for i in range(4):
		for j in range(4):
			nmtx[i][j]=mtx[j][i]
	return nmtx

def rotateHorizontal(mtx):
	nmtx=[[0 for i in range(4) ] for _ in range(4)]
	for i in range(4):
		for j in range(4):
			nmtx[i][j]=mtx[i][3-j]
	return nmtx

def getLeft(nmtx,score):
	mtx=nmtx
	mtx=stackLeft(mtx)
	mtx,score=combineLeft(mtx,score)
	mtx=stackLeft(mtx)
	return mtx,score

def getRight(nmtx,score):
	mtx=nmtx
	mtx=rotateHorizontal(mtx)
	mtx=stackLeft(mtx)
	mtx,score=combineLeft(mtx,score)
	mtx=stackLeft(mtx)
	mtx=rotateHorizontal(mtx)
	return mtx,score

def getUp(nmtx,score):
	mtx=nmtx
	mtx=transpose(mtx)
	mtx=stackLeft(mtx)
	mtx,score=combineLeft(mtx,score)
	mtx=stackLeft(mtx)
	mtx=transpose(mtx)
	return mtx,score

def getDown(nmtx,score):
	mtx=nmtx
	mtx=transpose(mtx)
	mtx=rotateHorizontal(mtx)
	mtx=stackLeft(mtx)
	mtx,score=combineLeft(mtx,score)
	mtx=stackLeft(mtx)
	mtx=rotateHorizontal(mtx)
	mtx=transpose(mtx)
	return mtx,score

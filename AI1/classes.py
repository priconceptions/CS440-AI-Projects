import Queue
import random
from pprint import pprint
class cell(object):
	def __init__(self, x, y, value, visit):
		self.x = x
		self.y = y
		self.value = value
		self.visit = visit
#for tree data structure
class node(object):
	def __init__(self, state, parent, action, cost, depth):
		self.state = state
		self.parent = parent
		self.action = action
		self.cost = cost
		self.depth = depth

class act_res(object):
	"""docstring for act-res"""
	def __init__(self, action, result):
		self.action = action
		self.result = result
		

def moveRight(cellMatrix, Cell, matSize):
	matSize = matSize - 1
	newXCoord = Cell.x  #row
	newYCoord = Cell.y + Cell.value #column
	if newXCoord <0 or newYCoord < 0 or newXCoord > matSize or newYCoord > matSize:
		return None
	newVal = cellMatrix[newXCoord][newYCoord].value
	newVisit = cellMatrix[newXCoord][newYCoord].visit + 1 
	newCell = cell(newXCoord, newYCoord, newVal, newVisit)
	act = act_res("right", newCell)
	return act

def moveLeft(cellMatrix, Cell, matSize):
	matSize = matSize - 1
	newXCoord = Cell.x #row
	newYCoord = Cell.y - Cell.value #column
	if newXCoord <0 or newYCoord < 0 or newXCoord > matSize or newYCoord > matSize:
		return None
	newVal = cellMatrix[newXCoord][newYCoord].value
	newVisit = cellMatrix[newXCoord][newYCoord].visit + 1 
	newCell = cell(newXCoord, newYCoord, newVal, newVisit)
	act = act_res("left", newCell)
	return act

def moveDown(cellMatrix, Cell, matSize):
	matSize = matSize - 1
	newXCoord = Cell.x + Cell.value #row
	newYCoord = Cell.y 
	if newXCoord <0 or newYCoord < 0 or newXCoord > matSize or newYCoord > matSize:
		return None
	newVal = cellMatrix[newXCoord][newYCoord].value
	newVisit = cellMatrix[newXCoord][newYCoord].visit + 1 
	newCell = cell(newXCoord, newYCoord, newVal, newVisit)
	act = act_res("down", newCell)
	return act

def moveUp(cellMatrix, Cell, matSize):
	matSize = matSize - 1
	newXCoord = Cell.x - Cell.value
	newYCoord = Cell.y
	if newXCoord <0 or newYCoord < 0 or newXCoord > matSize or newYCoord > matSize:
		return None
	newVal = cellMatrix[newXCoord][newYCoord].value
	newVisit = cellMatrix[newXCoord][newYCoord].visit + 1 
	newCell = cell(newXCoord, newYCoord, newVal, newVisit)
	act = act_res("up", newCell)
	return act



#TASK 2

def inQ(q, object):
	while q.empty() != True:
		v = q.get()
		if v.x == object.x and v.y == object.y and v.value == object.value:
			return True
	return False


def treeSearch(cellMatrix, q, randomGen, explored):
	head = cellMatrix[0][0]
	action1 = [moveRight(cellMatrix, cellMatrix[0][0], randomGen), moveLeft(cellMatrix, cellMatrix[0][0], randomGen), moveUp(cellMatrix, cellMatrix[0][0], randomGen), moveDown(cellMatrix, cellMatrix[0][0], randomGen)]
	headNode = node(head, None, action1, 0, 0)
	q.put(headNode)
	iter = 0
	while (True):
		iter = iter + 1
		if q.empty() == True:
			return "unsolvable"
		node1 = q.get()
		xCoord = (node1.state).x
		yCoord = (node1.state).y
		explored.append(node1.state)
		if iter > 2000:
			return "BROKE"
		for a in node1.action:
			if a:
				# print (a.result).x ,",", (a.result).y
				state = a.result
				newx = state.x
				newy = state.y
				newAct = [moveRight(cellMatrix, cellMatrix[newx][newy], randomGen), moveLeft(cellMatrix, cellMatrix[newx][newy], randomGen), moveUp(cellMatrix, cellMatrix[newx][newy], randomGen), moveDown(cellMatrix, cellMatrix[newx][newy], randomGen)]
				newDepth = node1.depth + 1
				child = node(state, node1, newAct, 0, newDepth)
				cellMatrix[newx][newy].visit = cellMatrix[newx][newy].visit + 1
				if child.state not in explored:
					if (child.state).x == randomGen-1 and (child.state).y == randomGen-1:
						#print "FOUND!!"
						goalVisit = 0
						ptr = child
						while (ptr.parent is not None):
							# print "HEREEE:",((ptr).state).x ,",", ((ptr).state).y
							ptr = ptr.parent
							#print "GOAL VISIT"
							#print ((child.parent).state).x ,",", ((child.parent).state).y
							goalVisit = goalVisit + 1
						cellMatrix[randomGen-1][randomGen-1].visit = goalVisit
						return "solved"
					q.put(child)
			else:
				continue

#RETURNS THE CELLmATRIX AND VALUE IN A CELLmATRIXvAL OBJECT
def evaluateTreeSearch(cellMatrix, randomGen):
	q = Queue.Queue()
	explored = []
	visitMat = [[0 for x in range(randomGen)] for y in range(randomGen)]
	s =  (treeSearch(cellMatrix, q, randomGen, explored))
	negSum = 0
	for a in range(randomGen):
		for b in range(randomGen):
			# print cellMatrix[a][b].visit
			visitMat[a][b] = cellMatrix[a][b].visit
			if cellMatrix[randomGen-1][randomGen-1].visit == 0:
				if visitMat[a][b] == 0:
					visitMat[a][b] = 'X'
					negSum = negSum + 1

	#Value of the function
	if negSum > 0:
		value = -1*negSum
	else:
		value = visitMat[randomGen-1][randomGen-1]
	valueMat = cellMatrixVal(visitMat, value)
	return valueMat



class cellMatrixVal(object):
	def __init__(self,matrix, value):
		self.matrix = matrix
		self.value = value

#TASK 3
def basicHillClimbing(cellMatrix, randomGen, iter):
	origNegSum = 0
	oVisitMat= [[0 for x in range(randomGen)] for y in range(randomGen)]
	negSum = 0
	for i in range(randomGen):
		for j in range(randomGen):
			# print cellMatrix[a][b].visit
			oVisitMat[i][j] = cellMatrix[i][j].visit
			if cellMatrix[randomGen-1][randomGen-1].visit == 0:
				if oVisitMat[i][j] == 0:
					oVisitMat[i][j] = 'X'
					origNegSum = origNegSum + 1
	if origNegSum > 0:
		origValue = -1*origNegSum
	else:
		origValue = oVisitMat[randomGen-1][randomGen-1]

	iterate = 0
	origCellMatVal = cellMatrixVal(cellMatrix, origValue)
	newvalue = 0

	while iterate < iter:
		cellMatrix = origCellMatVal.matrix
		iterate = iterate + 1
		randX = random.randint(0, randomGen-1)
		randY = random.randint(0, randomGen-1)
		while randX == randomGen-1 and randY == randomGen - 1:
			randX = random.randint(0, randomGen-1)
			randY = random.randint(0, randomGen-1)			

		for c in range(randomGen):
			for d in range(randomGen):
				cellMatrix[c][d].visit = 0
		randCell = random.randint(1, randomGen-1)
		cellMatrix[randX][randY].value = randCell
		q = Queue.Queue()
		explored = []
		s = treeSearch(cellMatrix, q, randomGen, explored)
		visitMat= [[0 for x in range(randomGen)] for y in range(randomGen)]
		negSum = 0
		for a in range(randomGen):
			for b in range(randomGen):
				# print cellMatrix[a][b].visit
				visitMat[a][b] = cellMatrix[a][b].visit
				if cellMatrix[randomGen-1][randomGen-1].visit == 0:
					if visitMat[a][b] == 0:
						visitMat[a][b] = 'X'
						negSum = negSum + 1
		# print "NEG suM IS ", (negSum > 0)
		if negSum > 0:
			newvalue = -1 * negSum
		else:
			newvalue = visitMat[randomGen-1][randomGen-1]
		l = origCellMatVal.value
		# print "Orig Val is: ", l
		# print "NEw suM IS ", (newvalue)
		if newvalue >= origCellMatVal.value :
			origCellMatVal.value = newvalue
			# print "NEWVALUE IS:", newvalue
			for a1 in range(randomGen):
				for b1 in range(randomGen):
					origCellMatVal.matrix[a1][b1] = cellMatrix[a1][b1] 
	hillClimb = cellMatrixVal(origCellMatVal.matrix, origCellMatVal.value)
	print hillClimb.value
	return hillClimb

#TASK 4
def hillClimbRandRestart(cellMatrix, randomGen, iterHillCLimb, iterPerHillClimb):
	origCellMatVal = evaluateTreeSearch(cellMatrix, randomGen)

	iterate = 0
	hillClimbIterate = 0
	newvalue = 0
	allHillClimbArray = []
	while hillClimbIterate < iterHillCLimb:
		hillClimbIterate = hillClimbIterate + 1
		for p in range(randomGen):
			for q in range(randomGen):
				randNum = random.randint(1, randomGen-1)
				cellMatrix[p][q].x = p
				cellMatrix[p][q].y = q
				cellMatrix[p][q].value = randNum
		valueOfMat = evaluateTreeSearch(cellMatrix, randomGen).value
		origCellMatVal = cellMatrixVal(cellMatrix, valueOfMat)
		#print "ORIGMATVAL", origCellMatVal.value
		while iterate < iterPerHillClimb:
			cellMatrix = origCellMatVal.matrix
			iterate = iterate + 1
			randX = random.randint(0, randomGen-1)
			randY = random.randint(0, randomGen-1)
			while randX == randomGen-1 and randY == randomGen - 1:
				randX = random.randint(0, randomGen-1)
				randY = random.randint(0, randomGen-1)			

			for c in range(randomGen):
				for d in range(randomGen):
					cellMatrix[c][d].visit = 0
			randCell = random.randint(1, randomGen-1)
			cellMatrix[randX][randY].value = randCell
			q = Queue.Queue()
			explored = []
			s = treeSearch(cellMatrix, q, randomGen, explored)
			visitMat= [[0 for x in range(randomGen)] for y in range(randomGen)]
			negSum = 0
			for a in range(randomGen):
				for b in range(randomGen):
					# print cellMatrix[a][b].visit
					visitMat[a][b] = cellMatrix[a][b].visit
					if cellMatrix[randomGen-1][randomGen-1].visit == 0:
						if visitMat[a][b] == 0:
							visitMat[a][b] = 'X'
							negSum = negSum + 1
			# print "NEG suM IS ", (negSum > 0)
			if negSum > 0:
				newvalue = -1 * negSum
			else:
				newvalue = visitMat[randomGen-1][randomGen-1]
			l = origCellMatVal.value
			# print "Orig Val is: ", l
			# print "NEw suM IS ", (newvalue)
			if newvalue >= origCellMatVal.value :
				origCellMatVal.value = newvalue
				# print "NEWVALUE IS:", newvalue
				for a1 in range(randomGen):
					for b1 in range(randomGen):
						origCellMatVal.matrix[a1][b1] = cellMatrix[a1][b1] 
		hillClimb = cellMatrixVal(origCellMatVal.matrix, origCellMatVal.value)
		allHillClimbArray.append(hillClimb)
	allVals = []
	for hillClimbs in allHillClimbArray:
		allVals.append(hillClimbs.value)
	print allVals
	return max(allVals)
	
#TASK 5
def basicHillClimbRandWalk(cellMatrix, randomGen, iter, prob):
	origCellMatVal = evaluateTreeSearch(cellMatrix, randomGen)
	iterate = 0
	newvalue = 0

	while iterate < iter:
		#cellMatrix = origCellMatVal.matrix
		iterate = iterate + 1
		randX = random.randint(0, randomGen-1)
		randY = random.randint(0, randomGen-1)
		for c in range(randomGen):
			for d in range(randomGen):
				cellMatrix[c][d].visit = 0
		randCell = random.randint(1, randomGen-1)
		cellMatrix[randX][randY].value = randCell
		q = Queue.Queue()
		explored = []
		s = treeSearch(cellMatrix, q, randomGen, explored)
		visitMat= [[0 for x in range(randomGen)] for y in range(randomGen)]
		negSum = 0
		for a in range(randomGen):
			for b in range(randomGen):
				# print cellMatrix[a][b].visit
				visitMat[a][b] = cellMatrix[a][b].visit
				if cellMatrix[randomGen-1][randomGen-1].visit == 0:
					if visitMat[a][b] == 0:
						visitMat[a][b] = 'X'
						negSum = negSum + 1
		# print "NEG suM IS ", (negSum > 0)
		if negSum > 0:
			newvalue = -1 * negSum
		else:
			newvalue = visitMat[randomGen-1][randomGen-1]
		l = origCellMatVal.value
		# print "Orig Val is: ", l
		# print "NEw suM IS ", (newvalue)

		probRand = random.random()
		if probRand > prob:
			if newvalue >= origCellMatVal.value :
				origCellMatVal.value = newvalue
				# print "NEWVALUE IS:", newvalue
				for a1 in range(randomGen):
					for b1 in range(randomGen):
						origCellMatVal.matrix[a1][b1] = cellMatrix[a1][b1] 


	hillClimb = cellMatrixVal(origCellMatVal.matrix, origCellMatVal.value)
	return hillClimb

#TASK 6
def simulatedAnnealing(cellMatrix, randomGen, temps)

# def geneticAlgo(cellMatrix1, cellMatrix2,randomGen,goodEnoughFitness):
# 	cellArr1 = []
# 	cellArr2 = []
# 	fitness1 = evaluateTreeSearch(cellMatrix1, randomGen)
# 	fitness2 = evaluateTreeSearch(cellMatrix2, randomGen)
# 	generation = 0
# 	for a in range(randomGen*randomGen):
# 		for b in range(randomGen*randomGen):
# 			cellArr1.append(cellMatrix1[a][b])
# 			cellArr2.append(cellMatrix2[a][b])

# 	while(goodEnoughFitness)




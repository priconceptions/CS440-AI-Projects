import Queue
import random
from pprint import pprint
import matplotlib.pyplot as plt
import math

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
		if (v.state).x == object.x and (v.state).y == object.y and (v.state).value == object.value:
			return True
	return False
def inExplored(explored, state):
	leng = len(explored)
	for a in range(leng):
		x = explored[a].x
		y = explored[a].y
		val = explored[a].value
		if state.x == x and state.y == y and state.value == val:
			return True
	return False

# def treeSearch(cellMatrix, q, randomGen, explored):
# 	head = cellMatrix[0][0]
# 	action1 = [moveRight(cellMatrix, cellMatrix[0][0], randomGen), moveLeft(cellMatrix, cellMatrix[0][0], randomGen), moveUp(cellMatrix, cellMatrix[0][0], randomGen), moveDown(cellMatrix, cellMatrix[0][0], randomGen)]
# 	headNode = node(head, None, action1, 0, 0)
# 	iter = 0
# 	while(True):
# 		if iter > 2000:
# 			return "BROKE"


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
				if  inExplored(explored, state)== False:
					child = node(state, node1, newAct, 0, newDepth)
					cellMatrix[newx][newy].visit = child.depth
				else:
					continue
				# print "VISIT = VISIT + 1"
				# print inExplored(explored, child.state)
				# print "HEREE: ", (q.empty())
					# print "HEREEEE", (child.state).x, (child.state).y
				if inExplored(explored, child.state) == False:
					if (child.state).x == randomGen-1 and (child.state).y == randomGen-1:
						# print "FOUND!!"
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
					# print((child.state).x, ",", (child.state).y)
					q.put(child)
			else:
				continue

#RETURNS THE CELLmATRIX AND VALUE IN A CELLmATRIXvAL OBJECT
def evaluateTreeSearch(cellMatrix, randomGen):
	q = Queue.Queue()
	# print "eval here", q.empty()
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
		visitMat[0][0] = 0
		value = -1*(negSum-1)
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
	#print hillClimb.value
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
	allVals.append(origCellMatVal.value)
	for hillClimbs in allHillClimbArray:
		allVals.append(hillClimbs.value)
	# print "~~~All vals", allVals
	return max(allVals)

#PLOT FOR 3 & 4
def plotter(hillClimbArr):
	#points[] = #array of points from functions
	plt.scatter(*zip(*hillClimbArr))
	# plt.plot(hillClimbArr, 'ro')
	plt.title('Basic hill climbing:')#,randomGen, " x ", randomGen)
	plt.ylabel('Evaluation function')
	plt.xlabel('Number of Iterations')
	# plt.xlim(1,50)
	plt.show()

def plotter2(hillClimbArr):
	#points[] = #array of points from functions
	#plt.scatter(*zip(*hillClimbArr))
	plt.scatter(*zip(*hillClimbArr))
	plt.title('Hill climb with random restarts:')#,randomGen, " x ", randomGen)
	plt.ylabel('Evaluation function')
	plt.xlabel('Number of Iterations of Hill Climb')
	# plt.xlim(1,50)
	plt.show()

def plotter3(hillClimbArr):
	#points[] = #array of points from functions
	#plt.scatter(*zip(*hillClimbArr))
	plt.scatter(*zip(*hillClimbArr))
	plt.title('Hill climb with random walk:')#,randomGen, " x ", randomGen)
	plt.ylabel('Evaluation function')
	plt.xlabel('Number of Iterations')
	# plt.xlim(1,50)
	plt.show()

def plotter4(hillClimbArr):
	#points[] = #array of points from functions
	#plt.scatter(*zip(*hillClimbArr))
	plt.scatter(*zip(*hillClimbArr))
	plt.title('Simulate Annealing:')#,randomGen, " x ", randomGen)
	plt.ylabel('Evaluation function')
	plt.xlabel('Number of Iterations')
	# plt.xlim(1,50)
	plt.show()

def plotter5(hillClimbArr):
	#points[] = #array of points from functions
	#plt.scatter(*zip(*hillClimbArr))
	plt.scatter(*zip(*hillClimbArr))
	plt.title('Genetic Algorithm')#,randomGen, " x ", randomGen)
	plt.ylabel('Evaluation function')
	plt.xlabel('Number of Iterations')
	# plt.xlim(1,50)
	plt.show()
	
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
def simulatedAnnealing(cellMatrix, randomGen, iter, iTemp, tempDecay):
	currentMat = cellMatrix
	currentVal = evaluateTreeSearch(cellMatrix, randomGen).value
	currentMatVal = cellMatrixVal(currentMat,currentVal)
	T = iTemp
	while(True):
		T = T*tempDecay
		if round(T, 5) == 0:
			return currentMatVal
		randX = random.randint(0, randomGen-1)
		randY = random.randint(0 ,randomGen-1)
		nexxtMat = currentMat
		for c in range(randomGen):
			for d in range(randomGen):
				nexxtMat[c][d].visit == 0
		randCell = random.randint(1, randomGen - 1)
		nexxtMat[randX][randY].value = randCell
		nexxtCellVal = evaluateTreeSearch(nexxtMat, randomGen).value

		nexxtMatVal = cellMatrixVal(nexxtMat, nexxtCellVal)

		deltaE = nexxtCellVal - currentVal
		if deltaE > 0:
			currentMat = nexxtMat
			currentVal = nexxtCellVal
			currentMatVal = nexxtMatVal
		else:
			probRand = random.random()
			prob = math.exp(deltaE/T)
			if probRand > prob:
				currentMat = nexxtMat
				currentVal = nexxtCellVal
				currentMatVal = nexxtMatVal


#TASK 7 - GENETIC ALGO
def TwoDto1D(cellMatrix, randomGen):
	arr = []
	for i in range(randomGen):
		for j in range(randomGen):
			arr.append(cellMatrix[i][j])
	return arr

def OneDto2D(arr, randomGen):
	cellMat = []
	new = []
	counter = 0
	for a in arr:
		new.append(a)
		counter = counter + 1
		if counter == randomGen:
			cellMat.append(new)
			new = []
			counter = 0
	return cellMat

def generatePopulation(numOfParents, randomGen, cellMatrix):
	population = []
	OneDCellMat = TwoDto1D(cellMatrix,randomGen)
	population.append(OneDCellMat)
	for i in range(numOfParents-1):
		aCellMatrix = [[cell(0,0,0,0) for i in range(randomGen)] for j in range(randomGen)]
		for p in range(randomGen):
			for q in range(randomGen):
				randNum = random.randint(1, randomGen-1)
				aCellMatrix[p][q].x = p
				aCellMatrix[p][q].y = q
				aCellMatrix[p][q].value = randNum
		aCellMatrix[randomGen-1][randomGen-1].value= 0
		aCellMatrix = TwoDto1D(aCellMatrix, randomGen)
		population.append(aCellMatrix)
	return population

def fitness(cellArr, randomGen):
	cellMat = OneDto2D(cellArr, randomGen)
	a = evaluateTreeSearch(cellMat, randomGen)
	return a.value

def readjustXY(childMat, randomGen):
	newChild = OneDto2D(childMat, randomGen)
	for p in range(randomGen):
		for q in range(randomGen):
			newChild[p][q].x = p
			newChild[p][q].y = q
	newChild = TwoDto1D(newChild, randomGen)
	return newChild

def reproduce(cellMatrix1, cellMatrix2, randomGen):
	n = len(cellMatrix1)
	c = random.randint(1, n-1)
	a = cellMatrix1[0:c]
	b = cellMatrix2[c:n]
	# print "total length", len(a)+len(b)
	child1 = a + b
	d = cellMatrix2[0:c]
	e = cellMatrix1[c:n]
	child2 = d + e
	# print "LENGTH OF CHILD1", len(child1)
	child1Fit = fitness(child1, randomGen)
	child2Fit = fitness(child2, randomGen)
	if child1Fit >= child2Fit:
		child1 = readjustXY(child1, randomGen)
		return child1
	else:
		child2 = readjustXY(child2, randomGen)
		return child2



def mutate(child, randomGen):
	i = random.randint(0, len(child) - 1)
	mutateCell = random.randint(1, randomGen - 1)
	child[i].value = mutateCell
	return child

def bestFitness(population, randomGen):
	allFitnesses = []
	for cellMat in population:
		a = fitness(cellMat, randomGen)
		allFitnesses.append(a)
	return max(allFitnesses)

		

def geneticAlgo(cellMatrix,randomGen, goodEnoughFitness, numOfParents, numOfIterations):
	population = generatePopulation(numOfParents, randomGen, cellMatrix)
	iterat = 0
	
	while (True):
		iterat = iterat + 1
		if (iterat > numOfIterations):
			theBestFitness = bestFitness(population, randomGen)
			# print "the Best fitness is", theBestFitness
			for ans in population:
				if fitness(ans, randomGen) == theBestFitness:
					ansMat = OneDto2D(ans, randomGen)
					ansVal = theBestFitness
					ansMatVal = cellMatrixVal(ansMat, ansVal)
					# print "RETURN HEREE"
					return ansMatVal

		newPopulation = []
		for i in range(len(population)):
			# print "RUN HERE???"
			xIndex = random.randint(0, len(population)-1)
			yIndex = random.randint(0, len(population)-1)
			child = reproduce(population[xIndex], population[yIndex], randomGen)
			randomProb = random.uniform(0, 1)
			probRand = random.random()
			if probRand > randomProb:
				child = mutate(child, randomGen)
			newPopulation.append(child)
		population = newPopulation
		if bestFitness(population, randomGen) >= goodEnoughFitness:
			for ans in population:
				if fitness(ans, randomGen) == bestFitness(population, randomGen):
					ansMat = OneDto2D(ans, randomGen)
					ansVal = bestFitness(population, randomGen)
					ansMatVal = cellMatrixVal(ansMat, ansVal)
					return ansMatVal
		
	theBestFitness = bestFitness(population, randomGen)
	for ans in population:
		if fitness(ans, randomGen) == theBestFitness:
			ansMat = OneDto2D(ans, randomGen)
			ansVal = theBestFitness
			ansMatVal = cellMatrixVal(ansMat, ansVal)
			return ansMatVal
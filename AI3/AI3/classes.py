import random
import math
from pprint import *
from decimal import *
#a cell structure

class cell(object):
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.type = 1
		self.highway = False
		self.start = False
		self.goal = False
		self.explored = False
		self.seqExplored = [False, False, False, False, False]

class map(object):
	def __init__(self, mapMatrix, start, goal):
		self.mapMatrix = mapMatrix
		self.start = start
		self.goal = goal

class utilityMatrix(object):
	def __init__(self, matrix, somethingElse):
		self.matrix = matrix
		self.somethingElse = somethingElse

def cost(cell1, cell2):
	costt = 0
	if cell1.type == 0 or cell2.type == 0:
		print "NOT TRAVERSABLE"
		print "cell1", cell1.row, ",", cell1.col
		print "cell2", cell2.row, ",", cell2.col
		return 100
	elif cell1.type == 1 and cell2.type == 1:
		if abs(cell1.row - cell2.row) == 1 and abs(cell1.col - cell2.col) == 1:
			costt = Decimal(math.sqrt(2))
		else:
			costt = Decimal(1)
	elif cell1.type == 2 and cell2.type == 2:
		if abs(cell1.row - cell2.row) == 1 and abs(cell1.col - cell2.col) == 1:
			costt = Decimal(math.sqrt(8))
		else:
			costt = Decimal(2)
	elif bool(cell1.type == 1) != bool(cell2.type == 1):
		if abs(cell1.row - cell2.row) == 1 and abs(cell1.col - cell2.col) == 1:
			costt = Decimal((math.sqrt(2) + math.sqrt(8))/2)
		else:
			costt = Decimal(1.5)
	if cell1.highway == True and cell2.highway == True:
		costt = Decimal(costt/4)
	return costt


def adjust(region, rows, columns):

	coord1 = list(region[0])
	coord2 = list(region[1])
	coord3 = list(region[2])
	coord4 = list(region[3])


	if coord1[0] < 0:
		adjVal = abs(coord1[0])
		coord1[0] = 0
		coord3[0] = coord3[0] + adjVal
	if coord1[1] < 0:
		adjVal = abs(coord1[0])
		coord1[1] = 0
		coord2[1] = coord2[1] + adjVal

	if coord2[0] < 0:
		adjVal = abs(coord2[0])
		coord2[0] = 0
		coord4[0] = coord4[0] + adjVal
	if coord2[1] > columns - 1:
		adjVal = coord2[1] - columns - 1
		coord2[1] = columns - 1
		coord1[1] = coord1[1] - adjVal

	if coord3[0] > rows - 1:
		adjVal = coord3[0] - rows - 1
		coord3[0] = rows -1
		coord1[0] = coord1[0] - adjVal
	if coord3[1] < 0:
		adjVal = abs(coord3[1])
		coord3[1] = 0
		coord4[1] = coord4[1] + adjVal

	if coord4[0] > rows - 1:
		adjVal = coord4[0] - rows - 1
		coord4[0] = rows - 1
		coord2[0] = coord2[0] - adjVal
	if coord4[1] > columns - 1:
		adjVal = coord4[1] - columns - 1
		coord4[1] = columns - 1
		coord3[1] = coord3[1] - adjVal

	newreg = [coord1, coord2, coord3, coord4]
	return newreg

def borderCell(cel, rows, columns):
	if cel[0] == 0:
		return True
	if cel[0] == rows - 1:
		return True
	if cel[1] == 0:
		return True
	if cel[1] == columns - 1:
		return True
	else:
		return False


def makePath(bordercell, rows, columns, mapMatrix):
	path = []
	direction ="something"
	if bordercell[0] == 0:
		#go down
		direction = "down"
		for i in range(20):
			newCell = [bordercell[0] + i, bordercell[1]]
			mapMatrix[bordercell[0] + i][bordercell[1]].highway = True
			path.append(newCell)
	elif bordercell[0] == rows - 1:
		#go up
		direction = "up"
		for i in range(20):
			newCell = [bordercell[0] - i, bordercell[1]]
			mapMatrix[bordercell[0] - i][bordercell[1]].highway = True
			path.append(newCell)
	elif bordercell[1] == 0:
		#go right
		direction = "right"
		for i in range(20):
			newCell = [bordercell[0], bordercell[1] + i]
			mapMatrix[bordercell[0]][bordercell[1] + i].highway = True
			path.append(newCell)
	elif bordercell[1] == columns - 1:
		#do left
		direction = "left"
		for i in range(20):
			newCell = [bordercell[0], bordercell[1] - i]
			mapMatrix[bordercell[0]][bordercell[1] - i].highway = True
			path.append(newCell)

	pathcount = 0

	while borderCell(path[-1], rows, columns) == False:
		if random.random() < 0.6:
			#move in the same direction
			if direction == "down":
				stepsToTake = 20
				lastcell =path[-1]
				if lastcell[0] + 20 > rows - 1:
					stepsToTake = rows - 1 - lastcell[0]
				# print stepsToTake
				for i in range(stepsToTake +1):
					newCell = [lastcell[0] + i, lastcell[1]]
					mapMatrix[lastcell[0] + i][lastcell[1]].highway = True
					path.append(newCell)
			elif direction == "up":
				stepsToTake = 20
				lastcell = path[-1]
				if lastcell[0] - 20 < 0:
					stepsToTake = lastcell[0]
				# print stepsToTake
				for i in range(stepsToTake + 1):
					newCell = [lastcell[0] - i, lastcell[1]]
					mapMatrix[lastcell[0] - i][lastcell[1]].highway = True
					path.append(newCell)
			elif direction == "right":
				stepsToTake = 20
				lastcell = path[-1]
				if lastcell[1] + 20 > columns - 1:
					stepsToTake = columns - 1 - lastcell[1]
				# print stepsToTake
				for i in range(stepsToTake + 1):
					newCell = [lastcell[0], lastcell[1] + i]
					mapMatrix[lastcell[0]][lastcell[1]+i].highway = True
					path.append(newCell)
			elif direction == "left":
				stepsToTake = 20
				lastcell = path[-1]
				if lastcell[1] - 20 < 0:
					stepsToTake = lastcell[1]
				# print stepsToTake
				for i in range(stepsToTake + 1):
					newCell = [lastcell[0], lastcell[1] - i]
					mapMatrix[lastcell[0]][lastcell[1] - i].highway = True
					path.append(newCell)
			pathcount = pathcount + 1
			continue

		if random.random() < 0.2:
			#move in the perpendicular direction
			if direction == "down":
				if random.random() < 0.5:
					#move right with 50 % prob
					stepsToTake = 20
					lastcell = path[-1]
					if lastcell[1] + 20 > columns - 1:
						stepsToTake = columns - 1 - lastcell[1]
					# print stepsToTake
					for i in range(stepsToTake + 1):
						newCell = [lastcell[0], lastcell[1] + i]
						mapMatrix[lastcell[0]][lastcell[1]+i].highway = True
						path.append(newCell)
				else:
					#move left with 50% prob
					stepsToTake = 20
					lastcell = path[-1]
					if lastcell[1] - 20 < 0:
						stepsToTake = lastcell[1]
					# print stepsToTake
					for i in range(stepsToTake + 1):
						newCell = [lastcell[0], lastcell[1] - i]
						mapMatrix[lastcell[0]][lastcell[1] - i].highway = True
						path.append(newCell)
			elif direction == "up":
				if random.random() < 0.5:
					#move right with 50 % prob
					stepsToTake = 20
					lastcell = path[-1]
					if lastcell[1] + 20 > columns - 1:
						stepsToTake = columns - 1 - lastcell[1]
					# print stepsToTake
					for i in range(stepsToTake + 1):
						newCell = [lastcell[0], lastcell[1] + i]
						mapMatrix[lastcell[0]][lastcell[1]+i].highway = True
						path.append(newCell)
				else:
					#move left with 50% prob
					stepsToTake = 20
					lastcell = path[-1]
					if lastcell[1] - 20 < 0:
						stepsToTake = lastcell[1]
					# print stepsToTake
					for i in range(stepsToTake + 1):
						newCell = [lastcell[0], lastcell[1] - i]
						mapMatrix[lastcell[0]][lastcell[1] - i].highway = True
						path.append(newCell)
			elif direction == "right":
				if random.random() <0.5:
					stepsToTake = 20
					lastcell =path[-1]
					if lastcell[0] + 20 > rows - 1:
						stepsToTake = rows - 1 - lastcell[0]
					# print stepsToTake
					for i in range(stepsToTake +1):
						newCell = [lastcell[0] + i, lastcell[1]]
						mapMatrix[lastcell[0] + i][lastcell[1]].highway = True
						path.append(newCell)
				else:
					stepsToTake = 20
					lastcell = path[-1]
					if lastcell[0] - 20 < 0:
						stepsToTake = lastcell[0]
					# print stepsToTake
					for i in range(stepsToTake + 1):
						newCell = [lastcell[0] - i, lastcell[1]]
						mapMatrix[lastcell[0] - i][lastcell[1]].highway = True
						path.append(newCell)
			elif direction == "left":
				if random.random() <0.5:
					stepsToTake = 20
					lastcell =path[-1]
					if lastcell[0] + 20 > rows - 1:
						stepsToTake = rows - 1 - lastcell[0]
					# print stepsToTake
					for i in range(stepsToTake +1):
						newCell = [lastcell[0] + i, lastcell[1]]
						mapMatrix[lastcell[0] + i][lastcell[1]].highway = True
						path.append(newCell)
				else:
					stepsToTake = 20
					lastcell = path[-1]
					if lastcell[0] - 20 < 0:
						stepsToTake = lastcell[0]
					# print stepsToTake
					for i in range(stepsToTake + 1):
						newCell = [lastcell[0] - i, lastcell[1]]
						mapMatrix[lastcell[0] - i][lastcell[1]].highway = True
						path.append(newCell)
			pathcount = pathcount + 1
			continue
	pathAndMatrix = utilityMatrix(mapMatrix, path)
	return pathAndMatrix

def createRandBorderCell(rows, columns):
	randx = 0
	randy = 0
	prob = random. random()
	if prob < 0.5:
		randx = random.randint(0, rows - 1)
		randy = 0
		if randx == 0 or randx == rows - 1:
			randy = random.randint(1, columns - 1)
		else:
			randy = random.choice([0, columns - 1])
	else:
		randy = random.randint(0, rows - 1)
		randx = 0
		if randy == 0 or randy == columns - 1:
			randx = random.randint(1, rows - 1)
		else:
			randx = random.choice([0, rows - 1])
	cell = [randx,randy]
	return cell


def intersect(path1, path2):
	intersection = [val for val in path1 if val in path2]
	if len(intersection) == 0:
		return False
	return True

def adjustPaths(allPaths, rows, columns, mapMatrix):

	for path in allPaths:
		exceptPath = list(allPaths)
		patha = exceptPath[0]
		pathb = exceptPath[1]
		pathc = exceptPath[2]
		if len(path) < 100:
			while len(path) < 100:
				for cell in path:
					# if cell not in patha and cell not in pathb and cell not in pathc:
					mapMatrix[cell[0]][cell[1]].highway = False
				allPaths.remove(path)
				newStart = createRandBorderCell(rows, columns)
				pathObj = makePath(newStart, rows, columns, mapMatrix)
				mapMatrix = pathObj.matrix
				path = pathObj.somethingElse
				allPaths.append(path) 

	path1 = allPaths[0]
	path2 = allPaths[1]
	path3 = allPaths[2]
	path4 = allPaths[3]
	intersect12 = [val for val in path1 if val in path2]
	while intersect(path1, path2) == True:
		intersect12 = [val for val in path1 if val in path2]
		for cell in path2:
			if cell not in intersect12:
				mapMatrix[cell[0]][cell[1]].highway = False
		newStart = createRandBorderCell(rows,columns)
		pathObj = makePath(newStart, rows, columns, mapMatrix)
		mapMatrix = pathObj.matrix
		index = allPaths.index(path2)
		allPaths.remove(path2)
		allPaths.insert(index,pathObj.somethingElse)
		path2 = allPaths[1]
	while intersect(path1, path3) == True:
		intersect13 = [val for val in path1 if val in path3]
		for cell in path3:
			if cell not in intersect13:
				mapMatrix[cell[0]][cell[1]].highway = False
		newStart = createRandBorderCell(rows,columns)
		pathObj = makePath(newStart, rows, columns, mapMatrix)
		mapMatrix = pathObj.matrix
		index = allPaths.index(path3)
		allPaths.remove(path3)
		allPaths.insert(index,pathObj.somethingElse)
		path3 = allPaths[2]
	while intersect(path1, path4) == True:
		intersect14 = [val for val in path1 if val in path4]
		for cell in path4:
			if cell not in intersect14:
				mapMatrix[cell[0]][cell[1]].highway = False
		newStart = createRandBorderCell(rows,columns)
		pathObj = makePath(newStart, rows, columns, mapMatrix)
		mapMatrix = pathObj.matrix
		index = allPaths.index(path4)
		allPaths.remove(path4)
		allPaths.insert(index,pathObj.somethingElse)
		path4 = allPaths[3]
	while (intersect(path2, path3) or intersect(path1, path3)):
		for cell in path3:
			if cell not in path2 and cell not in path1:
				mapMatrix[cell[0]][cell[1]].highway = False
		newStart = createRandBorderCell(rows,columns)
		pathObj = makePath(newStart, rows, columns, mapMatrix)
		mapMatrix = pathObj.matrix
		print path3 in allPaths
		index = allPaths.index(path3)
		allPaths.remove(path3)
		allPaths.insert(index,pathObj.somethingElse)
		path3 = allPaths[2]
	print intersect(path1, path2), ",", intersect(path1, path3),",", intersect(path1, path4),",", intersect(path2, path3)
	while (intersect(path2, path4) or intersect(path1, path4)):
		for cell in path4:
			if cell not in path2 and cell not in path1 and cell not in path3:
				mapMatrix[cell[0]][cell[1]].highway = False
		newStart = createRandBorderCell(rows,columns)
		pathObj = makePath(newStart, rows, columns, mapMatrix)
		mapMatrix = pathObj.matrix
		index = allPaths.index(path4)
		allPaths.remove(path4)
		allPaths.insert(index,pathObj.somethingElse)
		path4 = allPaths[3]
	while (intersect(path3, path4) or intersect(path2, path4) or intersect(path1, path4)):
		for cell in path4:
			if cell not in path3 and cell not in path2 and cell not in path1:
				mapMatrix[cell[0]][cell[1]].highway = False
		newStart = createRandBorderCell(rows,columns)
		pathObj = makePath(newStart, rows, columns, mapMatrix)
		mapMatrix = pathObj.matrix
		index = allPaths.index(path4)
		allPaths.remove(path4)
		allPaths.insert(index,pathObj.somethingElse)
		path4 = allPaths[3]
	allPathsObj = utilityMatrix(mapMatrix, allPaths)
	# pprint(allPathsObj.somethingElse)
	for eachPath in allPathsObj.somethingElse:
		for cell in eachPath:
			if mapMatrix[cell[0]][cell[1]].highway == False:
				mapMatrix[cell[0]][cell[1]].highway = True
	allPathsObj.matrix = mapMatrix
	return allPathsObj



def generateHighways(randBorderCells, rows, columns, mapMatrix):
	allPaths = []
	for bordercell in randBorderCells:
		pathObj = makePath(bordercell, rows, columns, mapMatrix)
		mapMatrix = pathObj.matrix
		path = pathObj.somethingElse
		allPaths.append(path)
	allPathsObj = adjustPaths(allPaths, rows, columns, mapMatrix)
	allPaths = allPathsObj.somethingElse
	mapMatrix = allPathsObj.matrix


def createBlockedCells(rows, columns, mapMatrix):
	for i in range(int(0.2*rows*columns)):
		randRows = random.randint(0, rows - 1)
		randCol = random.randint(0, columns - 1)
		if mapMatrix[randRows][randCol].highway == True:
			while(mapMatrix[randRows][randCol].highway == True):
				randRows = random.randint(0, rows - 1)
				randCol = random.randint(0, columns - 1)
			mapMatrix[randRows][randCol].type = 0 
		else:
			mapMatrix[randRows][randCol].type = 0




def initializeMap(rows, columns):
	mapMatrix = [[cell(0,0) for i in range(columns)] for j in range(rows)]
	for ro in range(rows):
		for co in range(columns):
			mapMatrix[ro][co].row = ro
			mapMatrix[ro][co].col = co
	# select eight coordinates randomly (xrand, yrand). For each coordinate pair (xrand, yrand), consider the 31x31 region centered
	# at this coordinate pair. For every cell inside this region, choose with probability 50% to mark it as
	# a hard to traverse cell.

	regions = []
	for a in range(8):
		rowrand = random.randint(0, rows - 1)
		colrand = random.randint(0, columns - 1)
		region1 = []

		coord1 = (rowrand - 15, colrand - 15)
		region1.append(coord1)
		coord2 = (rowrand - 15, colrand + 15)
		region1.append(coord2)
		coord3 = (rowrand + 15, colrand - 15)
		region1.append(coord3)
		coord4 = (rowrand + 15, colrand + 15)
		region1.append(coord4)
		region1 = adjust(region1, rows, columns)
		regions.append(region1)

	setHard = False
	# pprint(regions)
	for region in regions:
		rowTrav1 = region[0][0]
		rowTrav2 = region[2][0]
		colTrav1 = region[0][1]
		colTrav2 = region[1][1]
		for x in range(rowTrav1, rowTrav2):
			for y in range(colTrav1, colTrav2):
				if random.random() < 0.5:
					# print x, ",", y
					mapMatrix[x][y].type = 2


	randBorderCells = []
	for b in range(4):

		# choose random x and y on the border
		randx = 0
		randy = 0
		prob = random. random()
		if prob < 0.5:
			randx = random.randint(0, rows - 1)
			randy = 0
			if randx == 0 or randx == rows - 1:
				randy = random.randint(1, columns - 1)
			else:
				randy = random.choice([0, columns - 1])
			print randx, ",", randy
		else:
			randy = random.randint(0, rows - 1)
			randx = 0
			if randy == 0 or randy == columns - 1:
				randx = random.randint(1, rows - 1)
			else:
				randx = random.choice([0, rows - 1])
			print randx, ",", randy
		randBorderCells.append([randx,randy])
	generateHighways(randBorderCells, rows, columns, mapMatrix)
	createBlockedCells(rows, columns,mapMatrix)
	# setStartandGoal(rows, columns, mapMatrix)


	return mapMatrix
		
def distance(startx, starty, goalx, goaly):
	return math.sqrt(((startx - goalx)**2) + (starty - goaly)**2)



def allConditonsNotSatisfied(startx, starty, goalx, goaly, mapMatrix):
	if distance(startx,starty, goalx, goaly) < 100 or (mapMatrix[startx][starty].type == 0)  or  (mapMatrix[startx][starty].highway == True) or (mapMatrix[goalx][goaly].type == 0) or  (mapMatrix[goalx][goaly].highway == True):
		return True
	return False
def setStartandGoal(rows, columns, mapMatrix):
	if random.random() < 0.5:
		startx = random.randint(0, 19)
		starty = random.randint(0, 19)
	else:
		startx = random.randint(99, 119)
		starty = random.randint(139, 159)
	if random.random() < 0.5:
		goalx = random.randint(0, 19)
		goaly = random.randint(0, 19)
	else:
		goalx = random.randint(99, 119)
		goaly = random.randint(139, 159)
	print "MATH CHECK",distance(startx, starty, goalx, goaly)
	print allConditonsNotSatisfied(startx, starty, goalx, goaly, mapMatrix)
	while allConditonsNotSatisfied(startx, starty, goalx, goaly, mapMatrix) == True:

		if random.random() < 0.5:
			startx = random.randint(0, 19)
			starty = random.randint(0, 19)
		else:
			startx = random.randint(99, 119)
			starty = random.randint(139, 159)
		if random.random() < 0.5:
			goalx = random.randint(0, 19)
			goaly = random.randint(0, 19)
		else:
			goalx = random.randint(99, 119)
			goaly = random.randint(139, 159)

	# mapMatrix[startx][starty].start = True
	# print "START", startx, ",", starty
	# print "GOAL", goalx, ",", goaly
	# mapMatrix[goalx][goaly].goal = True
	startAndGoal = []
	start = [startx, starty]
	startAndGoal.append(start)
	goal = [goalx, goaly]
	startAndGoal.append(goal)
	# print "HEREEE IT IS", startAndGoal
	return startAndGoal

def generateMaps(rows, columns):
	allmaps = []
	for i in range(6):
		mapMatrix = initializeMap(rows, columns)
		for j in range(11):
			startAndGoal = setStartandGoal(rows, columns, mapMatrix)
			startx = startAndGoal[0][0]
			starty = startAndGoal[0][1]
			goalx = startAndGoal[1][0]
			goaly = startAndGoal[1][1]
			mapMatrix[startx][starty].start = True
			mapMatrix[goalx][goaly].goal =True
			map1 = map(mapMatrix, startAndGoal[0], startAndGoal[1])
			print "IT EXISTS", startAndGoal
			allmaps.append(map1)
			mapMatrix[startx][starty].start = False
			mapMatrix[goalx][goaly].goal =False
	return allmaps

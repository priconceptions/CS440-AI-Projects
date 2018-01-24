import random
import Tkinter
import Queue
from classes import *
from pprint import pprint

randomGen = random.choice([5, 7, 9, 11])
print "RandomGen is ::", randomGen

#defines matrix of cells
cellMatrix = [[cell(0,0,0,0) for i in range(randomGen)] for j in range(randomGen)]
Matrix = [[0 for x in range(randomGen)] for y in range(randomGen)]

for p in range(randomGen):
	for q in range(randomGen):
		randNum = random.randint(1, randomGen-1)
		cellMatrix[p][q].x = p
		cellMatrix[p][q].y = q
		cellMatrix[p][q].value = randNum

cellMatrix[randomGen-1][randomGen-1].value = 0

# q = Queue.Queue()
# explored = []
# visitMat= [[0 for x in range(randomGen)] for y in range(randomGen)]
# s =  (treeSearch(cellMatrix, q, randomGen, explored))
# negSum = 0
# for a in range(randomGen):
# 	for b in range(randomGen):
# 		# print cellMatrix[a][b].visit
# 		visitMat[a][b] = cellMatrix[a][b].visit
# 		if cellMatrix[randomGen-1][randomGen-1].visit == 0:
# 			if visitMat[a][b] == 0:
# 				visitMat[a][b] = 'X'
# 				negSum = negSum + 1

# #Value of the function
# if negSum > 0:
# 	value = -1*negSum
# else:
# 	value = visitMat[randomGen-1][randomGen-1]

print "VALUE IS ", evaluateTreeSearch(cellMatrix, randomGen).value

pprint (evaluateTreeSearch(cellMatrix, randomGen).matrix)

hillClimb = basicHillClimbing(cellMatrix, randomGen, 20)
print "HILL VALUE IS : ", hillClimb.value

hillClimbRestart = hillClimbRandRestart(cellMatrix, randomGen, 10, 20)
print "RAND RESTART HILL IS : ", hillClimbRestart

listVals = []
for iterat in range(50):
	hillClimbRandWalk = basicHillClimbRandWalk(cellMatrix, randomGen, iterat, 0.4)
	print iterat
	print "RAND WALK HILL IS : ", hillClimbRandWalk.value
#TASK 1
root = Tkinter.Tk()

for row in range(randomGen):
    for col in range(randomGen):
        Tkinter.Label(root, text ='(%s)' %(cellMatrix[row][col].value),
        	borderwidth = 5 ).grid(row = row, column = col)


root.mainloop()

#NEW HILL CLIMB MATRIX VISUALIZATION
root = Tkinter.Tk()

for row in range(randomGen):
    for col in range(randomGen):
        Tkinter.Label(root, text ='(%s)' %((hillClimb.matrix[row][col]).value),
        	borderwidth = 5 ).grid(row = row, column = col)


root.mainloop()
import random
import Tkinter
import Queue
from classes import *
from pprint import pprint
import matplotlib.pyplot as plt
import math
import time
from pprint import *
from matplotlib.colors import ListedColormap
from matplotlib import pyplot
import matplotlib as mpl
import numpy as np
from binaryHeap import *
from node import *
import matplotlib.pyplot as plt
import numpy as np
import time


# arr = initializeMap(120,160)

allMaps = generateMaps(120, 160)

amap = allMaps[0]
mapMat = amap.mapMatrix
start = amap.start
goal = amap.goal
s = [2,6]
print heuristicVal(s, start, goal)

#TESTING BINARY HEAP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cell1 = mapMat[0][0]
cell2 = mapMat[1][1]
cell3 = mapMat[1][2]
cell4 = mapMat[2][3]
node1 = Node(cell1)
node1.fCost = 3
node2 = Node(cell2)
node2.fCost = 4
node3 = Node(cell3)
node3.fCost = 1
node4 = Node(cell4)

nHeap = Heap()
nHeap.push(node1)
nHeap.push(node2)
nHeap.push(node3)

print search(nHeap, node4)

while len(nHeap)>0:
	print nHeap.pop().fCost

#TESTING BINARY HEAP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# TESTING GENERATE NEIGHBOURS METHOD~~~~~~~~~~~~~~~~~~~~~~~~~~
arra = generateNeighbours(node2, amap, 120, 160, 'U', 1)

for eachN in arra:
	ce = eachN.cell
	print ce.row, ",", ce.col
	print eachN.fCost
	print eachN.gCost
 
# TESTING GENERATE NEIGHBOURS METHOD~~~~~~~~~~~~~~~~~~~~~~~~~~


# anarray = seqHeuristic(allMaps[0], 'A', 120, 160, 1.2, 3)

# print anarray

#TESTING HEURISTIC ALGO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for amap in allMaps:
	file = open("map.txt", "w")
	value = ('startx', amap.start[0])
	s = str(value)
	file.write(s)
	file.write("\n")
	value = ('starty', amap.start[1])
	s = str(value)
	file.write(s)
	file.write("\n")
	value = ('goalx', amap.goal[0])
	s = str(value)
	file.write(s)
	file.write("\n")
	value = ('goaly', amap.goal[1])
	s = str(value)
	file.write(s)
	file.write("\n")

	ak = heuristicPath(amap, 'A', 120, 160, 1)
	uk = heuristicPath(amap, 'U', 120, 160, 1)
	wk = heuristicPath(amap, 'W', 120, 160, 2.5)
	t0 = time.time()
	sk = seqHeuristic(amap, 'A', 120, 160, 1.05, 3)
	print time.time() - t0, "seconds wall time"
	print ak

	arr = amap.mapMatrix
	nrows, ncols = 120,160
	dim = (nrows, ncols)
	image = np.zeros(dim)

	# Set every other cell to a random number (this would be your data)
	startCell = []
	goalCell = []
	for i in range(nrows):
		file.write("\n")
		for j in range(ncols):
			if arr[i][j].highway == True:
				image[i,j] = -5
				if arr[i][j].type == 1:
					value = ("a")
					s = str(value)
					file.write(s)
					file.write(" ")
				if arr[i][j].type == 2:
					value = ("b")
					s = str(value)
					file.write(s)
					file.write(" ")
				continue
			else:
				if arr[i][j].type == 1:
					image[i, j] = 5
					value = (1)
					s = str(value)
					file.write(s)
					file.write(" ")
	    		if arr[i][j].type == 2:
	    			image[i, j] = 2
	    			value = (2)
	    			s = str(value)
	    			file.write(s)
	    			file.write(" ")
	    		if arr[i][j].type == 0:
	    			image[i, j] = -2
					value = (0)
					s = str(value)
					file.write(s)
					file.write(" ")
	    		continue
	if ak != "FAILURE":
		for a in ak:
			ai = a[0]
			aj = a[1]
			image[ai,aj] = 8
	if uk != "FAILURE":
		for b in uk:
			ai = b[0]
			aj = b[1]
			image[ai,aj] = 10
	if wk != "FAILURE":
		for c in wk:
			ai = c[0]
			aj = c[1]
			image[ai,aj] = 12
	for d in sk:
		ai = d[0]
		aj = d[1]
		image[ai, aj] = 14
	image[amap.start[0], amap.start[1]] = 8
	image[amap.goal[0], amap.goal[1]] = 8
	# Reshape things into a 9x9 grid.
	image = image.reshape((nrows, ncols))


	# circle2 = plt.Circle((startCell[0], startCell[1]), 0.2, color='blue')
	# circle3 = plt.Circle((goalCell[0], goalCell[1]), 0.2, color='g', clip_on=False)



	row_labels = range(nrows)
	col_labels = range(ncols)
	plt.matshow(image)
	plt.xticks(range(ncols), col_labels)
	plt.yticks(range(nrows), row_labels)

	plt.show()





# print allMaps
# for a in allMaps:
# 	print a.start, a.goal
# for amap in allMaps:
# 	arr = amap.mapMatrix
# 	if arr == None:
# 		print "OH SHOT"

# 	# Make a 9x9 grid...
# 	nrows, ncols = 120,160
# 	dim = (nrows, ncols)
# 	image = np.zeros(dim)

# 	# Set every other cell to a random number (this would be your data)
# 	startCell = []
# 	goalCell = []
# 	for i in range(nrows):
# 		for j in range(ncols):
# 			if arr[i][j].highway == True:
# 				image[i,j] = -5
# 				continue
# 			else:
# 				if arr[i][j].type == 1:
# 					image[i, j] = 5
# 	    		if arr[i][j].type == 2:
# 	    			image[i, j] = 2
# 	    		if arr[i][j].type == 0:
# 	    			image[i, j] = -2
# 	    		continue
# 	image[amap.start[0], amap.start[1]] = 8
# 	image[amap.goal[0], amap.goal[1]] = 8
# 	# Reshape things into a 9x9 grid.
# 	image = image.reshape((nrows, ncols))


# 	# circle2 = plt.Circle((startCell[0], startCell[1]), 0.2, color='blue')
# 	# circle3 = plt.Circle((goalCell[0], goalCell[1]), 0.2, color='g', clip_on=False)



# 	row_labels = range(nrows)
# 	col_labels = range(ncols)
# 	plt.matshow(image)
# 	plt.xticks(range(ncols), col_labels)
# 	plt.yticks(range(nrows), row_labels)

# 	plt.show()

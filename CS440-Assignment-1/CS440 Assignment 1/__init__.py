import random
import Tkinter
import Queue
from classes import *
from pprint import pprint
import matplotlib.pyplot as plt
import math
import time
puzzle = raw_input("Enter the file to open or 123 for random: ")

if puzzle != '123':
	with open(puzzle) as textFile:
		matSize = textFile.readline()
		matSize = int(matSize)
		#next(textFile)
		lines = [line.split() for line in textFile]
		print lines

		# knownCellMat = [[cell(0,0,0,0) for i in range(setMatSize)] for j in range(setMatSize)]
		# knownMatrix = [[0 for x in range(setMatSize)] for y in range(setMatSize)]
	# pprint (lines)
	# print matSize
	
	cellMatrix = [[cell(0,0,0,0) for i in range(matSize)] for j in range(matSize)]
	print "WE ARE IN TASK 1. IN A FEW SECONDS, YOU WILL SEE THE VISUALIZATION OF THE MATRIX IN GUI. PLEASE PRESS X IN ORDER TO CONTINUE. THE MATRIX CAN BE SEEN IN TERMINAL BELOW."
	# pprint (lines)
	t0 = time.time()
	for p in range(matSize):
		for q in range(matSize):
			randNum = random.randint(1, matSize-1)
			cellMatrix[p][q].x = p
			cellMatrix[p][q].y = q
			cellMatrix[p][q].value = int(lines[p][q])
			cellMatrix[p][q].visit = 0

	cellMatrix[matSize-1][matSize-1].value = 0
	root = Tkinter.Tk()

	for row in range(matSize):
  	  for col in range(matSize):
  	      Tkinter.Label(root, text ='(%s)' %(cellMatrix[row][col].value),
    	    	borderwidth = 5 ).grid(row = row, column = col)


	root.mainloop()
	t1 = time.time()
	total = t1 - t0
	print "\n TOTAL TIME TO COMPUTE: ", total, "SECONDS"

	print "\n\n\nWE ARE NOW IN TASK 2. THE MATRIX IS EVALUATING THE VALUE OF THE PUZZLE."
	t3 = time.time()
	evalT = evaluateTreeSearch(cellMatrix, matSize)
	pprint (evalT.matrix)
	print "VALUE IS ", evalT.value
	t4 = time.time()
	total2 = t4-t3
	print "TOTAL TIME TO COMPUTE: ", total2, "SECONDS"
	print "\n"
	iterat = input('WE ARE NOW IN TASK 3. WE WILL BE EVALUATING WHAT THE FUNCTION VALUE. HOW MANY ITERATIONS DO YOU WANT THE FUNCTION TO RUN?')
	t5 = time.time()
	hillClimb = basicHillClimbing(cellMatrix, matSize, iterat)
	print "BASIC HILL CLIMB VALUE IS : ", hillClimb.value

	print "WE WILL NOW SEE THE FINAL PUZZLE CONFIGURATION. PLEASE PRESS X IN ORDER TO CONTINUE"
	root = Tkinter.Tk()

	for row in range(matSize):
  	  for col in range(matSize):
  	      Tkinter.Label(root, text ='(%s)' %(hillClimb.matrix[row][col].value),
    	    	borderwidth = 5 ).grid(row = row, column = col)


	root.mainloop()

	print "WE WILL NOW SEE HOW THE VALUE OF THE PUZZLE CHANGES AS WE GRADUALLY INCREASE THE NUMBER OF ITERATIONS UNTIL WE HAVE REACHED THE NUMBER OF ITERATIONS YOU DESCRIBED ABOVE"
	hillClimbArr = []
	for iterations in range(0,iterat,1):
		hillClimbVal = basicHillClimbing(cellMatrix, matSize, iterations)
		hillClimbArr.append((iterations,hillClimbVal.value))
	t6 = time.time()
	total3 = t6 - t5
	plotter(hillClimbArr)
	print "TOTAL TIME TO COMPUTE: ", total3, "SECONDS"

	print "\n\n\nNOW WE ARE IN TASK 4. THE FUNCTION WILL PERFORM RANDOM RESTARTS ON THE HILL CLIMBING PROCESS IN ORDER TO ESCAPE LOCAL EXTREMA. \n IN A SECOND, WE WILL ASK YOU HOW MANY ITERATIONS OF HILL CLIMB YOU WANT AND HOW MANY ITERATIONS PER HILL CLIMB"
	iterHillCLimb = input('HOW MANY HILL CLIMB PROCESSES DO YOU WANT TO PERFORM?')
	iterPerHillClimb = input('HOW MANY ITERATIONS PER HILL CLIMB DO YOU WANT TO PERFORM?')
	t7 = time.time()
	randRest = hillClimbRandRestart(cellMatrix, matSize, iterHillCLimb, iterPerHillClimb)
	print "\nRANDOM RESTART HILL CLIMB VALUE IS: ",randRest
	print "\nWE WILL NOW SEE HOW THE VALUE OF THE PUZZLE CHANGES AS WE GRADUALLY INCREASE THE NUMBER OF ITERATIONS OF HILL CLIMB AND ITERATIONS PER HILL CLIMB UNTIL WE HAVE REACHED THE NUMBER OF ITERATIONS YOU DESCRIBED ABOVE "
	
	randRestaryArr = []
	for iterations2 in range(iterHillCLimb):
		# print iterations2
 		hillClimbRestart = hillClimbRandRestart(cellMatrix, matSize, iterations2, iterPerHillClimb)
		randRestaryArr.append((iterations2,hillClimbRestart))
	print "RAND RESTART HILL IS : ", hillClimbRestart

	t8 = time.time()
	total4 = t8-t7
	plotter2(randRestaryArr)
	print "TOTAL TIME TO COMPUTE: ", total4, "SECONDS"


	print "\n\n\nNOW WE ARE IN TASK 5. THE FUNCTION WILL PERFORM RANDOM WALK, WHICH IS A DOWNHILL MOVEMENT WITH PROBABLITY P. \n IN A SECOND, WE WILL ASK YOU HOW MANY ITERATIONS OF HILL CLIMB AND PROBABILITY OF DOWN HILL MOVEMEMENT"
	t9 = time.time()
	iterRandWalk3 = input('HOW MANY ITERATIONS OF HILL CLIMB DO YOU WANT TO PERFORM?')
	prob = input('WHAT PROBABILITY DO YOU WAN TO PERFORM DOWN HILL MOVEMENT?')
	print "RANDOM WALK VALUE IS: ",basicHillClimbRandWalk(cellMatrix, matSize, iterRandWalk3, prob).value
	print"\nNOW, WE WILL SEE HOW THE VALUES CHANGE AS THE ITERATIONS GRADUALLY INCREASE"
	randWalk = []
	for iterations3 in range(iterRandWalk3):
		hillClimbRandWalk = basicHillClimbRandWalk(cellMatrix, matSize, iterations3, prob).value
		randWalk.append((iterations3,hillClimbRandWalk))
		# print "RAND WALK HILL IS : ", hillClimbRandWalk
	t10 = time.time()
	total5 = t10-t9
	plotter3(randWalk)
	print "TOTAL TIME TO COMPUTE: ", total5, "SECONDS"

	print "\n\n\nNOW WE ARE IN TASK 6. WE WILL SIMULATE ANNEALING AND SEE HOW THE PERFORMANCE IS.\n IN A SECOND, WE WILL ASK YOU TO PUT IN THE NUMBER OF ITERATIONS, THE INITIAL TEMPERATURE AND THE TEMPERATURE DECAY RATE."
	iterSimAnn = input('HOW MANY ITERATIONS DO YOU WANT TO PERFORM?')
	iTemp = input('WHAT IS THE INITIAL TEMPERATURE?')
	tempDecay = input('WHAT IS THE RATE OF DECAY OF TEMPERATURE?')
	t1 = time.time()
	print "SIMULATED ANNEALING VALUE IS: ", simulatedAnnealing(cellMatrix, matSize, iterSimAnn, iTemp, tempDecay).value

	print "\n NOW WE WILL SEE HOW THE VALUE CHANGES AS THE NUMBER OF ITERATIONS INCREASES"
	simAnn = []
	for iterations4 in range(iterSimAnn):
		sA=simulatedAnnealing(cellMatrix, matSize, iterations4, iTemp, tempDecay).value
		simAnn.append((iterations4,sA))
	t2 = time.time()
	total = t2 - t1
	plotter4(simAnn)
	print"TOTAL TIME: ", total

	print "\n\n\n NOW WE ARE IN TASK 7 . WE WILL SIMULATE A GENETIC ALGORITHM AND SHOW THE VALUE PRODUCED BY IT."
	numOfParents = input('HOW MANY PARENTS WOULD YOU LIKE TO PERFORM THE ALGORITHM OVER?')
	goodEnoughFitness = input('WHATS A GOOD ENOUGH FITNESS FOR YOU-- AKA PUT A REAL NUMBER VALUE THAT WILL BE < LENGTH OF MATRIX SQUARED')
	numOfIterations = input('HOW MANY ITERATIONS WOULD YOU LIKE TO RUN THIS ALGORITHM?')
	print "GENETIC ALGORITHM VALUE IS: ", geneticAlgo(cellMatrix, matSize, goodEnoughFitness, numOfParents, numOfIterations).value

	print "\n\n\n NOW WE WILL SEE HOW THE VALUE OF THE FUNCTION CHANGES AS WE INCREASE THE NUMBER OF ITERATIONS\n"
	genValue = []
	for iterations5 in range(numOfIterations):
		ans = (geneticAlgo(cellMatrix, matSize, goodEnoughFitness, numOfParents, iterations5).value)
		genValue.append((iterations5,ans))
	plotter5(genValue)
	print "\n\n NOW WE WILL SEE HOW GENETIC ALGORITHM PERFORMS AS WE INCREASE THE NUMBER OF PARENTS\n"
	genValP = []
	for iterations6 in range(numOfParents):
		ans = (geneticAlgo(cellMatrix, matSize, goodEnoughFitness, iterations6, numOfIterations).value)
		genValP.append((iterations6, ans))
	plotter5(genValP)

else:

	randomGen = random.choice([5, 7, 9, 11])
	#print "RandomGen is ::", randomGen
	randomGen = 50
	#defines matrix of cells
	cellMatrix = [[cell(0,0,0,0) for i in range(randomGen)] for j in range(randomGen)]

	print "WE ARE IN TASK 1. IN A FEW SECONDS, YOU WILL SEE THE VISUALIZATION OF THE MATRIX IN GUI. PLEASE PRESS X IN ORDER TO CONTINUE. THE MATRIX CAN BE SEEN IN TERMINAL BELOW."
	# pprint (lines)
	t0 = time.time()
	for p in range(randomGen):
		for q in range(randomGen):
			randNum = random.randint(1, randomGen-30)
			cellMatrix[p][q].x = p
			cellMatrix[p][q].y = q
			cellMatrix[p][q].value = randNum
			cellMatrix[p][q].visit = 0

	cellMatrix[randomGen-1][randomGen-1].value = 0
	root = Tkinter.Tk()

	for row in range(randomGen):
  	  for col in range(randomGen):
  	      Tkinter.Label(root, text ='(%s)' %(cellMatrix[row][col].value),
    	    	borderwidth = 5 ).grid(row = row, column = col)


	root.mainloop()

	for i in range(randomGen):
		for j in range(randomGen):
			print cellMatrix[i][j].value
		print "\n"
	t1 = time.time()
	total = t1 - t0
	print "\n TOTAL TIME TO COMPUTE: ", total, "SECONDS"

	print "\n\n\nWE ARE NOW IN TASK 2. THE MATRIX IS EVALUATING THE VALUE OF THE PUZZLE."
	t3 = time.time()
	evalT = evaluateTreeSearch(cellMatrix, randomGen)
	pprint (evalT.matrix)
	print "VALUE IS ", evalT.value
	t4 = time.time()
	total2 = t4-t3
	print "TOTAL TIME TO COMPUTE: ", total2, "SECONDS"
	print "\n"
	iterat = input('WE ARE NOW IN TASK 3. WE WILL BE EVALUATING WHAT THE FUNCTION VALUE. HOW MANY ITERATIONS DO YOU WANT THE FUNCTION TO RUN?')
	t5 = time.time()
	hillClimb = basicHillClimbing(cellMatrix, randomGen, iterat)
	print "BASIC HILL CLIMB VALUE IS : ", hillClimb.value
	print "WE WILL NOW SEE THE FINAL PUZZLE CONFIGURATION. PLEASE PRESS X IN ORDER TO CONTINUE"
	root = Tkinter.Tk()

	for row in range(randomGen):
  	  for col in range(randomGen):
  	      Tkinter.Label(root, text ='(%s)' %(hillClimb.matrix[row][col].value),
    	    	borderwidth = 5 ).grid(row = row, column = col)


	root.mainloop()

	# print "WE WILL NOW SEE HOW THE VALUE OF THE PUZZLE CHANGES AS WE GRADUALLY INCREASE THE NUMBER OF ITERATIONS UNTIL WE HAVE REACHED THE NUMBER OF ITERATIONS YOU DESCRIBED ABOVE"
	# hillClimbArr = []
	# for iterations in range(0,iterat,1):
	# 	hillClimbVal = basicHillClimbing(cellMatrix, randomGen, iterations)
	# 	hillClimbArr.append((iterations,hillClimbVal.value))
	# t6 = time.time()
	# total3 = t6 - t5
	# plotter(hillClimbArr)
	# print "TOTAL TIME TO COMPUTE: ", total3, "SECONDS"

	# print "\n\n\nNOW WE ARE IN TASK 4. THE FUNCTION WILL PERFORM RANDOM RESTARTS ON THE HILL CLIMBING PROCESS IN ORDER TO ESCAPE LOCAL EXTREMA. \n IN A SECOND, WE WILL ASK YOU HOW MANY ITERATIONS OF HILL CLIMB YOU WANT AND HOW MANY ITERATIONS PER HILL CLIMB"
	# iterHillCLimb = input('HOW MANY HILL CLIMB PROCESSES DO YOU WANT TO PERFORM?')
	# iterPerHillClimb = input('HOW MANY ITERATIONS PER HILL CLIMB DO YOU WANT TO PERFORM?')
	# t7 = time.time()
	# randRest = hillClimbRandRestart(cellMatrix, randomGen, iterHillCLimb, iterPerHillClimb)
	# print "\nRANDOM RESTART HILL CLIMB VALUE IS: ",randRest
	# print "\nWE WILL NOW SEE HOW THE VALUE OF THE PUZZLE CHANGES AS WE GRADUALLY INCREASE THE NUMBER OF ITERATIONS OF HILL CLIMB AND ITERATIONS PER HILL CLIMB UNTIL WE HAVE REACHED THE NUMBER OF ITERATIONS YOU DESCRIBED ABOVE "
	
	# randRestaryArr = []
	# for iterations2 in range(iterHillCLimb):
	# 	# print iterations2
 # 		hillClimbRestart = hillClimbRandRestart(cellMatrix, randomGen, iterations2, iterPerHillClimb)
	# 	randRestaryArr.append((iterations2,hillClimbRestart))
	# print "RAND RESTART HILL IS : ", hillClimbRestart

	# t8 = time.time()
	# total4 = t8-t7
	# plotter2(randRestaryArr)
	# print "TOTAL TIME TO COMPUTE: ", total4, "SECONDS"


	# print "\n\n\nNOW WE ARE IN TASK 5. THE FUNCTION WILL PERFORM RANDOM WALK, WHICH IS A DOWNHILL MOVEMENT WITH PROBABLITY P. \n IN A SECOND, WE WILL ASK YOU HOW MANY ITERATIONS OF HILL CLIMB AND PROBABILITY OF DOWN HILL MOVEMEMENT"
	# t9 = time.time()
	# iterRandWalk3 = input('HOW MANY ITERATIONS OF HILL CLIMB DO YOU WANT TO PERFORM?')
	# prob = input('WHAT PROBABILITY DO YOU WAN TO PERFORM DOWN HILL MOVEMENT?')
	# bascH = basicHillClimbRandWalk(cellMatrix, randomGen, iterRandWalk3, prob)
	# print "RANDOM WALK VALUE IS: ",bascH.value
	# print "WE WILL NOW SEE THE FINAL PUZZLE CONFIGURATION. PLEASE PRESS X IN ORDER TO CONTINUE"
	# root = Tkinter.Tk()

	# for row in range(randomGen):
 #  	  for col in range(randomGen):
 #  	      Tkinter.Label(root, text ='(%s)' %(bascH.matrix[row][col].value),
 #    	    	borderwidth = 5 ).grid(row = row, column = col)


	# root.mainloop()
	# print"\nNOW, WE WILL SEE HOW THE VALUES CHANGE AS THE ITERATIONS GRADUALLY INCREASE"
	# randWalk = []
	# for iterations3 in range(iterRandWalk3):
	# 	hillClimbRandWalk = basicHillClimbRandWalk(cellMatrix, randomGen, iterations3, prob).value
	# 	randWalk.append((iterations3,hillClimbRandWalk))
	# 	# print "RAND WALK HILL IS : ", hillClimbRandWalk
	# t10 = time.time()
	# total5 = t10-t9
	# plotter3(randWalk)
	# print "TOTAL TIME TO COMPUTE: ", total5, "SECONDS"

	# print "\n\n\nNOW WE ARE IN TASK 6. WE WILL SIMULATE ANNEALING AND SEE HOW THE PERFORMANCE IS.\n IN A SECOND, WE WILL ASK YOU TO PUT IN THE NUMBER OF ITERATIONS, THE INITIAL TEMPERATURE AND THE TEMPERATURE DECAY RATE."
	# iterSimAnn = input('HOW MANY ITERATIONS DO YOU WANT TO PERFORM?')
	# iTemp = input('WHAT IS THE INITIAL TEMPERATURE?')
	# tempDecay = input('WHAT IS THE RATE OF DECAY OF TEMPERATURE?')
	# t1 = time.time()
	# smAne = simulatedAnnealing(cellMatrix, randomGen, iterSimAnn, iTemp, tempDecay)
	# print "SIMULATED ANNEALING VALUE IS: ", smAne.value
	# print "WE WILL NOW SEE THE FINAL PUZZLE CONFIGURATION. PLEASE PRESS X IN ORDER TO CONTINUE"
	# root = Tkinter.Tk()

	# for row in range(randomGen):
 #  	  for col in range(randomGen):
 #  	      Tkinter.Label(root, text ='(%s)' %(smAne.matrix[row][col].value),
 #    	    	borderwidth = 5 ).grid(row = row, column = col)


	# root.mainloop()
	# print "\n NOW WE WILL SEE HOW THE VALUE CHANGES AS THE NUMBER OF ITERATIONS INCREASES"
	# simAnn = []
	# for iterations4 in range(iterSimAnn):
	# 	sA=simulatedAnnealing(cellMatrix, randomGen, iterations4, iTemp, tempDecay).value
	# 	simAnn.append((iterations4,sA))
	# t2 = time.time()
	# total = t2 - t1
	# plotter4(simAnn)
	# print"TOTAL TIME: ", total, "SECONDS"

	# print "\n\n\n NOW WE ARE IN TASK 7 . WE WILL SIMULATE A GENETIC ALGORITHM AND SHOW THE VALUE PRODUCED BY IT."
	# numOfParents = input('HOW MANY PARENTS WOULD YOU LIKE TO PERFORM THE ALGORITHM OVER?')
	# goodEnoughFitness = input('WHATS A GOOD ENOUGH FITNESS FOR YOU-- AKA PUT A REAL NUMBER VALUE THAT WILL BE < LENGTH OF MATRIX SQUARED')
	# numOfIterations = input('HOW MANY ITERATIONS WOULD YOU LIKE TO RUN THIS ALGORITHM?')
	# genAlgo = geneticAlgo(cellMatrix, randomGen, goodEnoughFitness, numOfParents, numOfIterations)
	# print "GENETIC ALGORITHM VALUE IS: ", genAlgo.value
	# print "WE WILL NOW SEE THE FINAL PUZZLE CONFIGURATION. PLEASE PRESS X IN ORDER TO CONTINUE"
	# root = Tkinter.Tk()

	# for row in range(randomGen):
 #  	  for col in range(randomGen):
 #  	      Tkinter.Label(root, text ='(%s)' %(genAlgo.matrix[row][col].value),
 #    	    	borderwidth = 5 ).grid(row = row, column = col)


	# root.mainloop()

	# print "\n\n\n NOW WE WILL SEE HOW THE VALUE OF THE FUNCTION CHANGES AS WE INCREASE THE NUMBER OF ITERATIONS\n"
	# t11 = time.time()
	# genValue = []
	# for iterations5 in range(numOfIterations):
	# 	ans = (geneticAlgo(cellMatrix, randomGen, goodEnoughFitness, numOfParents, iterations5).value)
	# 	genValue.append((iterations5,ans))
	# plotter5(genValue)
	# print "\n\n NOW WE WILL SEE HOW GENETIC ALGORITHM PERFORMS AS WE INCREASE THE NUMBER OF PARENTS\n"
	# genValP = []
	# for iterations6 in range(numOfParents):
	# 	ans = (geneticAlgo(cellMatrix, randomGen, goodEnoughFitness, iterations6, numOfIterations).value)
	# 	genValP.append((iterations6, ans))
	
	# t12 = time.time()
	# total9 = t12-t11 
	# plotter5(genValP)
	# print"TOTAL TIME:", total9, "SECONDS"
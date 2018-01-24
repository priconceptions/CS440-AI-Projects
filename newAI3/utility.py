#utility functions that help the implementation of the main functions

#a utilty object to store the matrix and anything else with it
class utilityMatrix(object):
	def __init__(self, matrix, somethingElse):
		self.matrix = matrix
		self.somethingElse = somethingElse

#returns true if the cell is a bordercell; False otherwise
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

#creates a random border cell; cell is of type list
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

#checks if 2 paths intersect
def intersect(path1, path2):
	intersection = [val for val in path1 if val in path2]
	if len(intersection) == 0:
		return False
	return True

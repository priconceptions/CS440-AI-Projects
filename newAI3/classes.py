import random
import math
from pprint import *
from decimal import *
from utility import *

class cell(object):
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.type = 1
		self.highway = False
		self.start = False
		self.goal = False

# the cost between traversing 2 cells as described
def cost(cell1, cell2):
	costt = 0
	if cell1.type == 0 or cell2.type == 0:
		print "NOT TRAVERSABLE"
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

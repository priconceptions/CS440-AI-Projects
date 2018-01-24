def summ(x,y):
	return x+y
def mult(x,y):
	return x*y

a = [summ, mult]
for i in range(2):
	print a[i](1,2)
w1 = 0.12
w2 = -1.3

for i in range(10):
	w1 = w1 + 1.0*(0.0-1.0)*(w1)
	w2 = w2 + 1.0*(0.0-1.0)*(w2)
print w1
print w2
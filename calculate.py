import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def birthday_paradox(n):
	probability = 1
	for i in range(1, n):
		probability = probability * (365 - i) / 365
	return 1 - probability
# arctan

def arctan(x, a, b, c, d, e, f):
	try :
		return (a/(b*np.pi))*np.arctan((x-c)*d/e) + f
	except ZeroDivisionError:
		return 0


#generate random float in range with 3 decimals of precision

def random_float(start, end):
	return round(np.random.uniform(start, end), 3)


data1 = [birthday_paradox(i) for i in range(0, 100)]
best_error = 0
while 1: 
	#TODO: make this more efficient
	#choose random values to compare 
	a = random_float(10, 15)
	b = random_float(8, 12)
	c = random_float(20, 25)
	d = random_float(7, 15)
	e = np.random.randint(1, 100)
	f = random_float(0, 1)
	data2 = [arctan(i, a, b, c, d, e, f) for i in range(0, 100)]
	# find error between data points
	error = 0
	for i in range(0, 100):
		error += abs(data1[i] - data2[i])
	if error < best_error or best_error == 0:
	#if error is less than last error, print the values
		best_error = error
		print('new best error: ' + str(best_error) + ' with a = ' + str(a) + ', b = ' + str(b) + ', c = ' + str(c) + ', d = ' + str(d) + ', e = ' + str(e) + ', f = ' + str(f))





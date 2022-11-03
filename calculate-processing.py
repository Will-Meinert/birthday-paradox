import numpy as np
import json
from multiprocessing import Process
import os

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
# load values.json error
with open('values.json', 'r') as f:
	values = json.load(f)
	best_json_error = values['error']

def main():
	best_error = 0

	while 1: 
		#TODO: make this more efficient
		#choose random values to compare 
		a = random_float(11, 14)
		b = random_float(9, 11)
		c = random_float(19, 24)
		d = random_float(6, 10)
		e = random_float(80, 96)
		f = 0.44
		data2 = [arctan(i, a, b, c, d, e, f) for i in range(0, 100)]
		# find error between data points
		error = 0
		for i in range(0, 100):
			error += abs(data1[i] - data2[i])
		if error < best_error or best_error == 0:
		#if error is less than last error, print the values
			best_error = error

			if best_error < best_json_error:
				print('new (json) best error: ' + str(error) + ' with a = ' + str(a) + ', b = ' + str(b) + ', c = ' + str(c) + ', d = ' + str(d) + ', e = ' + str(e) + ', f = ' + str(f))

				# read json file values and update with new values
				with open('values.json', 'r') as val:
					values = json.load(val)
					values['error'] = best_error
					values['a'] = a
					values['b'] = b
					values['c'] = c
					values['d'] = d
					values['e'] = e
					values['f'] = f
				# write new values to json file
				with open('values.json', 'w') as f:
					json.dump(values, f, indent=4)
			else:
				print('new (program life) best error: ' + str(error) + ' with a = ' + str(a) + ', b = ' + str(b) + ', c = ' + str(c) + ', d = ' + str(d) + ', e = ' + str(e) + ', f = ' + str(f))

if __name__ == '__main__':
#multiprocessing 
	processes = []
	for i in range(os.cpu_count()):
		print('starting process ' + str(i))
		processes.append(Process(target=main))

	for process in processes:
		process.start()

	for process in processes:
		process.join()

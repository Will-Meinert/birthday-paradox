import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

#calculate birthday paradox
def birthday_paradox(n):
	probability = 1
	for i in range(1, n):
		probability = probability * (365 - i) / 365
	# round to 2 decimal places
	return (1 - probability)

with open('data.txt', 'w') as f:
	for i in range(1, 100):
		f.write('x = ' + str(i) + ', y = ' + str(birthday_paradox(i)) + '\n')
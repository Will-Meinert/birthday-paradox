import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def birthday_paradox(n):
	probability = 1
	for i in range(1, n):
		probability = probability * (365 - i) / 365
	return 1 - probability


# arctan values
# error = 1.5972928762910859
a = 12.977
b = 10.285
c = 21.295
d = 9.33
e = 95
f = 0.447
def arctan(x, original: bool = False):
	if original:
		return (13/(10*np.pi))*np.arctan((x-23)*9/100) + 0.5
	else:
		return (a/(b*np.pi))*np.arctan((x-c)*d/e) + f

#calculate data
data1 = [birthday_paradox(i) for i in range(0, 100)]
data2 = [arctan(i) for i in range(0, 100)]
data3 = [arctan(i, True) for i in range(0, 100)]

#calculate error of data 2 and data 3 to the original data
error = 0
for i in range(0, 100):
	error += abs(data1[i] - data2[i])
print('dataset 2 error: ' + str(error))
error = 0
for i in range(0, 100):
	error += abs(data1[i] - data3[i])
print('dataset 3 error: ' + str(error))


#show data
plt.plot(data1)
plt.plot(data2)
plt.plot(data3)
plt.legend(['Birthday Paradox', 'Arctan', 'Original Arctan'])
plt.show()



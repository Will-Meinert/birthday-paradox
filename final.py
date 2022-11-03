import matplotlib.pyplot as plt
import numpy as np
import json

def birthday_paradox(n):
	probability = 1
	for i in range(1, n):
		probability = probability * (365 - i) / 365
	return 1 - probability


# arctan values
#error = 1.581772627328872
a = 13.646
b = 10.648
c = 20.901
d = 7.599
e = 80.128
f = 0.44

def arctan(x):
	return (a/(b*np.pi))*np.arctan((x-c)*d/e) + f

#calculate data
data1 = [birthday_paradox(i) for i in range(0, 100)]
data2 = [arctan(i) for i in range(0, 100)]

#calculate error of data 2 to the original data
error = 0
for i in range(0, 100):
	error += abs(data1[i] - data2[i])
print('dataset 2 error: ' + str(error))

#show data
plt.plot(data1)
plt.plot(data2)
plt.legend(['Birthday Paradox', 'Arctan'])
plt.show()



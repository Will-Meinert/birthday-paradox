import matplotlib.pyplot as plt
import numpy as np
import json
import math


def birthday_paradox(n):
	probability = 1
	for i in range(1, n):
		probability = probability * (365 - i) / 365
	return 1 - probability

def birthday_paradox_permute(n):
	return 1 - ((math.floor(math.factorial(365)/math.factorial(365 - n))/365**n))
	
# arctan values
# read arctan values from json file
with open('values.json', 'r') as val:
	values = json.load(val)
	a = values['a']
	b = values['b']
	c = values['c']
	d = values['d']
	e = values['e']
	f = values['f']

def arctan(x, original: bool = False):
	if original:
		return (13/(10*np.pi))*np.arctan((x-23)*9/100) + 0.5
	else:
		return (a/(b*np.pi))*np.arctan((x-c)*d/e) + f

#calculate data
data1 = [birthday_paradox(i) for i in range(0, 100)]
data2 = [arctan(i) for i in range(0, 100)]
data3 = [arctan(i, True) for i in range(0, 100)]
data4 = [birthday_paradox_permute(i) for i in range(0, 100)]

#calculate error of data 2 and data 3 to the original data
error = 0
for i in range(0, 100):
	error += abs(data1[i] - data2[i])
print('dataset 2 error: ' + str(error))
error = 0
for i in range(0, 100):
	error += abs(data1[i] - data3[i])
print('dataset 3 error: ' + str(error))

fig, ax = plt.subplots()
#show data
line1, = ax.plot(data1)
line2, = ax.plot(data2)
line3, = ax.plot(data3)
line4, = ax.plot(data4)

lines = [line1, line2, line3, line4]
lined = {}  # Will map legend lines to original lines.
leg = plt.legend(['Birthday Paradox', 'Arctan', 'Original Arctan', 'Birthday Paradox Permute'])
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)  # Enable picking on the legend line.
    lined[legline] = origline
def on_pick(event):
    # On the pick event, find the original line corresponding to the legend
    # proxy line, and toggle its visibility.
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # Change the alpha on the line in the legend so we can see what lines
    # have been toggled.
    legline.set_alpha(1.0 if visible else 0.2)
    fig.canvas.draw()

fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()



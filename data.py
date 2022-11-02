#calculate birthday paradox
def birthday_paradox(n):
	probability = 1
	for i in range(1, n):
		probability = probability * (365 - i) / 365
	return (1 - probability)

#write birthday paradox return values to file
with open('data.txt', 'w') as f:
	for i in range(1, 100):
		f.write('x = ' + str(i) + ', y = ' + str(birthday_paradox(i)) + '\n')
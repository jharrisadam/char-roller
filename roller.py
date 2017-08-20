# Rolls starting attributes for D&D 3.5 character creation.
# Returns 6 iterations of 4d6 dice, dropping the lowest result of each set.

from random import randint

def roll():
	answer = []
	for i in range(6):
		# Considered running this as a nested iterative range, but that seemed unnecessary.
		temp = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
		a = min(temp)
		temp.remove(a)
		temp = sum(temp)
		answer.append(temp)
	answer.sort(reverse=True)
	print(answer)

while True:
	roll_test = input("Roll stats? Y/N: ")
	if roll_test.lower().startswith('n'):
		break
	elif roll_test.lower().startswith('y'):
		roll()
	else:
		print("Please enter Y or N: ")

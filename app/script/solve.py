import numpy as np
def sqroot(answer):
	return "I cannot really find the sq root of " + answer
	#todo find sq root
def exp(answer):
	arr = answer.split()
	arr = [int(ch) for ch in arr]
	return np.array2string(np.exp(arr))
def cuberoot(answer):
	return "I cannot really find the cube root of " + answer
def greet(answer):
	return "Hello " + answer
def solve(question, answer):
	switcher = {
		'sqroot' : sqroot,
		'cuberoot' : cuberoot,
		'greetme' : greet,
		'expo' : exp
	}
	func = switcher.get(question, lambda:"Invalid Route")
	return func(answer)

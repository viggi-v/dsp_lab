def sqroot(answer):
	return "I cannot really find the sq root of " + answer
def cuberoot(answer):
	return "I cannot really find the cube root of " + answer

def solve(question, answer):
	switcher = {
		'sqroot' : sqroot,
		'cuberoot' : cuberoot
	}
	func = switcher.get(question, lambda:"Invalid Route")
	return func(answer)

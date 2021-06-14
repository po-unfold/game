from pushing_outshoot_unfold import Term
import random

term = Term()

def addition():
	a = random.randint(0, 10) # Pick a number between 0 and 10
	b = random.randint(0, 10) # Pick another number between 0 and 10
	real_answer = str(round(a + b))
	user_answer = input(f"What is {a} + {b}? ")
	if real_answer == user_answer:
		print(term.green('Correct!'))
	else:
		print(term.red(f'Incorrect! The correct answer was `{real_answer}`'))

def subtraction():
	a = random.randint(0,10) # Pick a number between 0 and 10
	b = random.randint(0,10) #Pick another number between 0 and 10
	real_answer = str(round(a - b))
	user_answer = input(f"What is {a} - {b}? ")
	if real_answer == user_answer:
		print(term.green('Correct!'))
	else:
		print(term.red(f'Incorrect! The correct answer was `{real_answer}`'))

def multiplication():
	a = random.randint(0,10) # Pick a number between 0 and 10
	b = random.randint(0,10) # Pick a number between 0 and 10
	real_answer = str(round(a * b))
	user_answer = input(f"What is {a} * {b}? ")
	if real_answer == user_answer:
		print(term.green('Correct!'))
	else:
		print('Incorrect')

def division():
	return
	a = random.randint(0,10) # Pick a number between 0 and 10
	b = random.randint(0,10) # Pick a number between 0 and 10
	answer = a / b
	if round(answer) == answer:
		answer = round(answer)
	real_answer = str(round(a / b))
	user_answer = input(f"What is {a} / {b}? ")
	if real_answer == user_answer:
		print(term.green('Correct!'))
	else:
		print(term.red(f'Incorrect! The correct answer was `{real_answer}`'))



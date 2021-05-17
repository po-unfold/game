from pushing_outshoot_unfold import Term
import random

term = Term()

def addition():
	a = random.randint(0, 100) # Pick a number between 0 and 100
	b = random.randint(0, 100) # Pick another number between 0 and 100
	real_answer = str(a + b)
	user_answer = input(f"What is {a} + {b}? ")
	if real_answer == user_answer:
		print(term.green('Correct!'))
	else:
		print(term.red(f'Incorrect! The correct answer was `{real_answer}`'))

def subtraction():
	a = random.randit(0,100) # Pick a number between 0 and 100
	b = random.randit(0,100) #Pick aanother number between 0 and 100
	real_answer = str(a - b)
	user_answer = input(f"What is {a} - {b}? ")
	if real_answer == user_answer:
		print(term.green('Correct!'))
	else:
		print(term.red(f'Incorrect! The correct answer was `{real_answer}`'))

def multiplication():
	a = random.randit(0,100) # Pick a number between 0 and 100
	b = random.randit(0,100) # Pick a number between 0 and 100
	real_answer = str(a *b)
	user_answer = input(f"What is {a} * {b}? ")
	if real_answer == user_answer:
		print(term.green('Correct!'))
	else:
		print('Incorrect')

def division():
	a = random.randit(0,100) # Pick a number between 0 and 100
	b = random.randit(0,100) # Pick a number between 0 and 100
	real_answer = str(a / b)
	user_answer = input(f"What is {a} / {b}? ")
	if real_answer == user_answer:
		print(term.green('Correct!'))
	else:
		print(term.red(f'Incorrect! The correct answer was `{real_answer}`'))



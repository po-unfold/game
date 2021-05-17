# key = {
# 	"What is the essential gas needed for us to breath?": "oxygen"
# }

# for i in range(10): # Ask 10 questions
# 	q, a = random.choice(list(key.items())) # pick a random q/a pair
# 	response = input(q).lower() # make it lowercase
# 	if response == a.lower():
# 		print('Correct!')
# 	else:
# 		print(f'Incorrect! The correct answer was {a}.')


import random
from pushing_outshoot_unfold import Term

term = Term()

user_start = input('Please type "start" to begin')

if uesr_start == 'start':
	question = random.randint(1,30)
	if question == '1':
		user_response = input(' What is the essential gas needed for us to breath?  ')
		if user_response == 'oxygen' or 'Oxygen':
			print('Correct!')
		else:
			print('Incorrect! correct answer is Oxygen')
	if question == '2':
		user_response = input('What is the name of the planet closet to the Sun?  ')
			if user_response == 'Mercury' or 'mercury':
				print('Correct!')
			else:
				print('Incorrect! correct answer is Mercury')
	if question == '3':
		user_response = input('How many teeth does an adult human have?   ')
			if user_response == '32':
				print('Correct!')
			else:
				print('Incorrect! correct answer is 32')
	if question == '4':
		user_response = input('Earth has how many layers?   ')
			if user_response == '3':
				print('Correct!(core, mantle, crust')
			else:
				print('Incorrect! correct answer is 3 (core, mantle, crust))
	if question == '5':
		user_response = input('What is the rarest blood type?  ')
			if user_response == 'AB negative':
				print('Correct!')
			else:
				print('Incorrect! correct answer is AB negative')
	if question == '6':
		user_response = input('What is the boiling point of water in degrees celsius?   ') 
			if user_response == '100 degrees celsius' or '100 degrees' or '100':
				print('Correct!')
			else:
				print('Incorrect! correct answer is 100 degrees')
	if question == '7':
		user_response = input('Animals that eat both plants and meat are called what?'  )
			if user_response == 'Omnivores' or 'omnivores' or 'Omnivore' or 'omnivore':
				print('Correct!')
			else:
				print('Incorrect! correct answer is Omnivores')
	if question == '8':
		






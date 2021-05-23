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

if user_start == 'start':
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
		user_response = input('True of False: sound travels faster in air than in water.')
		if user_response == 'True' or 'true':
			print('Correct!')
		else:
			print('Incorrect! correct answer is True')
	if question == '9':
		user_response = input('How many elements are in the periodic table as of 2020 ?   '') 
		if user_response == '118':
			print('Correct!')
		else:
			print('Incorrect! correct answer is 118')
	if question == '10':
		user_response = input('Where can you find the smallest bone in the human body?  ')
		if user_response == 'Ear' or 'ear':
			print('Correct!')
		else:
			print('Incorrect! correct answer is the ear')
	if question == '11':
		user_response = input('How many hearts does an octopus have?  ')
		if user_response == '3':
			print('Correct!')
		else:
			print('Incorrect! correct answer is 3')
	if question == '12':
		user_response = input('Can you hear anything in outer space?  ')
		if user_response == 'No':
			print('Correct!')
		else:
			print('Incorrect! correct answer is no')
	if question == '13':
		user_response = input('True or False: You hair and nails are made out of the same material.   ')
		if user_response == 'True' or 'true':
			print('Correct!')
		else:
			print('Incorrect! correct answer is true')
	if question == '14':
		user_response = input('How many bones are in the human body?   ')
		if user_response == '206':
			print('Correct!')
		else:
			print('Incorrect! correct answer is 206')
	if question == '15':
		user_response = input('What is the biggest planet in the solar system?   ')
		if user_response == 'Jupitor' or 'jupitor':
			print('Correct!')
		else:
			print('Incorrect! correct answer is Jupitor')
	if question == '16':
		user_response = input('What country was Marie Curie born in?    ')
		if user_response == 'Poland' or 'poland':
			print('Correct!')
		else:
			print('Incorrect! correct answer is Poland. ')
	if question == '17':
		user_response = input('What mineral is essential for bone health and growth?  ')
		if user_response == 'Calcium' or 'calcium':
			print('Correct!')
		else:
			print('Incorrect! correct answer is calcium')
	if question == '18':
		user_response = input('What are the three states of matter?  ')
		if user_response == 'solid' and 'liquid' and 'gas':
			print('Correct!')
		else:
			print('Incorrect!')
	if question == '19':
		user_response = input('What is the third planet in our solar system?   ')
		if user_answer == 'Earth' or 'earth':
			print('Correct!')
		else:
			print('Incorrect! correct answer is Earth. ')
	if question == '20':
		user_response = input('How many planets are in our solar sytem?  ')
		if user_response == '9' or 'nine':
			print('Correct!')
		else:
			print('Incorrect! correct answer is 9')
	if question == '21':
		user_response = input('What force keeps us from floating off the ground?  ')
		if user_response == 'Gravity' or 'gravity':
			print('Correct!')
		else:
			print('Incorrect! correct answer is gravity')
	if question == '22':
		user_response = input('How many days are in a year on Earth?   ')
		if user_response == '365' or '365 days':
			print('Correct!')
		else:
			print('Incorrect! correct answer is 365')
	if question == '23':
		user_response = input('What is solid water called?  ')
		if user_response == 'ice' or'Ice':
			print('Correct!')
		else:
			print('Incorrect! correct answer is ice')
	if question == '24':
		user_response = input('What food do we get from bees?  ')
		if user_response = 'Honey' or 'honey':
			print('Correct!')
		else:
			print('Incorrect! correct answer is honey')
	if question == '25':
		user_response = input('What gas do we breath out?(answer with full name)   ')
		if user_response == 'Carbon Dioxide' or 'carbon dioxide':
			print('Correct!')
		else:
			print('Incorrect! correct answer is carabon dioxide')
	if question == '26':
		user_response = input('True of False: Pluto is a dwarf planet.  ')
		if user_response == 'True' or 'true':
			print('Correct!')
		else:
			print('Incorrect! correct answer is true')
	if question == '27':
		user_response = input('What do all the planets in our solar system revolve around?   ')
		if user_response == 'the sun' or 'The Sun' or 'sun' of 'Sun':
			print('Correct!')
		else:
			print('Incorrect! correct answer is the Sun')
	if question == '28':
		user_response = input('How many ounces in a pound?   ')
		if user_response == '16':
			print('Correct!')
		else:
			print('Incorrect! correct answer is 16')
	if question == '29':
		user_response = input('What substance has the scientific formula of H2O?   ')
		if user_response == 'water' or 'Water':
			print('Correct!')
		else:
			print('Incorrect! correct answer is water.')
	if question == '30':
		user_response = input('Which planet is known as "The Red Planet"?   ')
		if user_response == 'Mars' or 'mars':
			print('Correct!')
		else:
			print('Incorrect! correct answer is Mars')

for i in range(5):
	questions(str(i))





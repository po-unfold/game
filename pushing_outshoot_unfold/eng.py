# User input first 
# 3 sections of homework: grammar (numbers 1-10, give 3 questions) , spelling (numbers 11-20, give 3 questions), definitions (numbers 21-30, give 3 questions)

user = input("Press enter to start the homework.")


def questions():
	problem = input('Choose a problem! Enter a number from 1-30 to select.')
	if problem == '1':
		answer = input("Question 1: Conjugate! Susan go to school. Write the corect form of the verb in lowercase:")
		if answer == 'goes':
			print('Correct!')
		else:
			print('Incorrect. The answer was :goes.' )
	if problem == '2':
		answer = input('Combine sentences: I like to walk. I like to read.')
		if answer == 'I like to walk and read.':
			print('Nice job!')
		else:
			print('The correct answer was: I like to walk and read. ')
	if problem == '3':
		answer = input('Which of these is a verb: Sally, Running, or Canada?')
		if answer == 'Running':
			print('You got it!')
		else:
			print('The correct answer was: Running.')
	if problem == '4':
		answer = input('Which is the noun: jumping, sleeping, or cat?')
		if answer == 'cat':
			print('Correct!')
		else:
			print('Incorrect. The correct answer was: John.')
	if problem == '5': 
		answer = input('Which is the pronoun: walking, John?')
		if answer == 'John':
			print('Nice job!')
		else:
			print('The correct answer was:John')
	if problem == '6':
		answer = input('Is the word: ran present, past, or future tense?')
		if answer == 'past':
			print('That\'s correct!')
		else:
			print('Not quite. The answer is: past tense.')
	if problem == '7':
		answer = input('Is New York a person,place, or thing?')
		if answer == 'Place':
			print('Good job!')
		else:
			print('The correct answer was: place')
	if problem == '8':
		answer = input('Which of these words is spelled correctly: misenformation or dissect?')
		if answer == 'dissect':
			print('Nice!')
		else:
			print('Not quite. The correct answer is: dissect.')
	if problem == '9':
		answer = input('Write this verb in present tense: ran')
		if answer == 'run':
			print('You got it!')
		else:
			print('The answer is: run.')
	if problem == '10':
		answer = input('Which of these famous works was written by Shakespeare: a. Romeo and Juliet or b. The Road Not Taken')
		if answer == 'a.':
			print('That\'s right!')
		elif answer == 'a':
			print('Correct!')
		else:
			print('Incorrect. The answer is: a.')
	if problem == '11':
		answer = input('True or false: Nothing Gold Can Stay was written by Robert Frost')
		if answer == 'true':
			print('Good job!')
		else:
			print('The correct answer is: True.')
	if problem == '12':
		answer = input('Correct this word: missstake.') 
		if answer == 'mistake':
			print('You got it!')
		else:
			print('The correct answer is: mistake')
	if problem == '13':
		answer = input('Conjugate the verb in present tense: I walking to the park.')
		if answer == 'walk':
			print('Nice job!')
		else:
			print('Not quite. The answer is: walk.')
	if problem == '14':
		answer = input('Which of these words is the noun: break, dog, or click?')
		if answer == 'dog':
			print('That\'s right!')
		else:
			print('The answer is: dog.')
	if problem == '15':
		answer = input('Which of these words is the adjective: run, lock, or red?')
		if answer == 'red':
			print('Good job!')
		else:
			print('Incorrect. The correct answer is: red.')
	if problem == '16':
		answer = input('Correct the sentence, write only the portion that needs to be corrected: Sam are playing outside.')
		if answer == 'is':
			print('Correct!')
		else:
			print('Not quite. The correct answer is: is.')
	if problem == '17':
		answer = input('Correct this word: Televeesion')
		if answer == 'Television':
			print('Correct!')
		else:
			print('Incorrect. Answer is: Television.')
	if problem == '18':
		answer = input('Which word is the verb: swim or scarf?')
		if answer == 'Swim':
			print('You got it!')
		else:
			print('The answer is: swim.')
	if problem == '19':
		answer = input('Correct the verb: Marie click her pen.')
		if answer == 'clicks':
			print('Good job!')
		elif answer == 'is clicking':
			print('Nice job!')
		else:
			print('Not quite. The answer is: clicks')
	if problem == '20':
		answer = input('Correct the verb: They are play.')
		if answer == 'playing':
			print('Good job!')
		else:
			print('Incorrect. The correct answer is: playing.')
	if problem == '21':
		answer = input('Change the verb: doing to past tense.')
		if answer == 'did':
			print('Nice job!')
		else:
			print('Not quite. The answer is: did.')
	if problem == '22':
		answer = input('Which of these words is spelled correctly: misstaken, misssspelled, or miraculous')
		if answer == 'Miraculous':
			print('Correct!')
		else:
			print('Incorrect. The correct answer is: Miraculous.')
	if problem == '23':
		answer = input('Write the present tense form of: swam')
		if answer == 'Swimming':
			print('That\'s right!')
		else:
			print('Not quite. The correct answer is: Swimming.')
	if problem == '24':
		answer = input('Correct this word: Pianow')
		if answer == 'Piano':
			print('You got it!')
		else:
			print('Not quite. The correct answer is: Piano.')
	if problem == '25':
		answer = input('Correct the verb: Sam is run to the post office.')
		if answer == 'running':
			print('Good job!')
		else:
			print('The corect answer is: running.')
	if problem == '26':
		answer = input('Who wrote the play Hamlet: a. Shakespeare b. Lois Lowry').
		if answer == 'a.':
			print('Nice job!')
		elif answer == 'a':
			print('You got it!')
		else:
			print('The answer is: a.')
	if problem == '27':
		answer = input('Which of these words is the adjective: tiny, water, or ball?')
		if answer == 'tiny':
			print('Correct!')
		else:
			print('Not quite. The answer is: tiny.')
	if problem == '28':
		answer = input('Fix this sentence: I am play in the sand.')
		if answer == 'playing':
			print('Nice job!')
		else:
			print('Not quite. The correct answer is: playing.')
	if problem == '29':
		answer = input('Which of these words is a place: Paris, jacket, or bottle?')
		if answer == 'Paris':
			print('That\'s right!')
		else:
			print('Incorrect. The correct answer is: Paris.')
	if problem == '30':
		answer = input('What is the definition of \'sorry\': a. a place b. an apology?')
		if answer == 'b.'
			print('You got it!')
		elif answer == 'b':
			print('Good job!')
		else:
			print('Not quite. The correct answer is: b.')

def ask_questions():
	for i in range(5):
		questions()
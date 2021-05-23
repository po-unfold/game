import random
import time

pause = lambda: time.sleep(1.5)

def day1():
	print('Pick 1 or 2')  
	user_answer = input('''1.Try to go to a different part of the house to see if the connection is better there.
2. Email your teacher about what's going on.''') 
	if user_answer == '1' or '2':
		print('Zoom finally worked! You got into your first class, pre-Algebra. You breathe a sigh of relief. Your heart was still racing rapidly and you have a bit of a headache from the stress of all that. However, after that first Zoom meeting, you kind of get the jist of things, and joining the rest of your Zoom meetings is easier. Nothing more to worry about for the rest of the day. Teachers were just going over work and explaining how Zoom classes would work. First day, complete. Phew!')	

def day2():
	user_supplies = input('Canned Food  or  Packs of Water')
	if user_supplies == 'Canned Food':
		canned_food = input('Beans and Tuna or Veggies and Soup')
		if canned_food == 'Beans and Tuna':
			print('You decided to pick beans and tuna because that was what you thought you grandparents, aunt, and cousins would make more use for.')
		elif canned_food == 'Veggies and Soup':
			print( 'You decided to pick veggies and soup because you didn\'t see any other options')
	if user_supplies == 'Packs of Water':
		user_water = input('1 or 2 packs of water?')
		if user_water == '1':
			print('You decide to get only 1 pack, because you only want to get what will last for good amount of time.')
		elif user_water == '2':
			print('You decide to get 2 just in case another problem arises.')
	print('Good Job! Time to go checkout and head back home.')

def day3():
	# user_word = input('Please type 'CHC':    ')
	# if user_word == 'CHC':
	outcome = random.randint(1,2)
	if outcome == 1:
		print('You are able to get 80% of your homework done. However, the second science homework is taking longer than you expected. It is now 5:55 p.m. You would need at least 30-40 more minutes to finish your homework, but you wouldn’t be able to turn it in on time. You just decide to turn in what you finished, really stressed and upset about now managing your time. ')
	if outcome == 2:
		print('After doing your 2 science homeworks first, you realize that you only have 30 minutes left to finish your algebra and english homework. You try to cram everything into the 30 minutes you have left and you turn everything in just in time, but your homework quality isn’t that great.')

def day4():
	user_input = input('HOW WILL YOU SOLVE THIS PROBLEM? Pick 1 or 2: 1.Create a handwritten planner.  2.Create a To-do list on your phone.      ')
	if user_input == '1':
		print('You use a ruler and a pen to make your planner look neat and make it easy to understand. You make a column for each day and list out your homeowrk for the week.  You decide to place it right next to your computer so it\'s easy to see.  Woo-hoo!  You feel good about yourself.')
	if user_input == '2':
		print(' You download a daily  weekly planner app on your phone. It has  cool designs and includes a monthly planner too. You allow the app to notify you every morning so you could go over your plans for the day. This is really helpful for you,  since you have your phone with you  most of the time.')


def day7():	
	look = input('''Where do you look first.  Pick option 1,2, or 3: 
	1. Behind the bush 
	2. Next to the steps of your porch 
	3. Right side of the garden 
	''')
	if look in ('1', '2'):
		print('Not there!')
	if look == '3':
		print('Good Job! You found her!')

	look = input('''Round 2: 
	1. Left side of the garden 
	2. Behind the bush 
	3. Behind the chicken coop 
	''')
	if look in ('1', '3'):
		print('Not there!')
	if look == '2':
		print('Good Job! You found her!')


	look = input('''Round 3: 
	1. Next to the step of your porch (wrong)
	2. Behind the chicken coop (right)
	3. Behind the bush (wrong) 
	''')
	if look in ('1', '3'):
		print('Not there!')
	if look == '2':
		print('Good Job! You found her!')

def day8():	
	yearbook = input('''Where do you look first.  Pick 1,2, or 3:
	1. 8th Grade Class Pictures
	2. Spirit Week
	3. 8th Grade Baby Pictures.
	''')

	if yearbook == '1':
		print('You scan through the faces of your classmates and friends. It hits you that you haven’t seen each other in person in a long time. You really miss talking to your friends and hanging out with them.')

	if yearbook == '2':
		print('When you were still in school, you were part of the soccer team. It was really fun going to the soccer games and practicing with your teammates. You hope that you’ll be able to meet up with your classmates soon after Covid-19 restrictions lighten up.')

	if yearbook == '3':
		print('You spot your baby pictures, and you burst out laughing. Your dad had selected your baby pictures for you. You didn’t even remember submitting it. In the pictures, you are sitting on the ground next to some foam building blocks. One of your hands holding a t.v remote in your mouth, and the other hand holding a foam building block next to your ear.')


def day9():
	cooking = input('''Two things stand out to you the most in the baking cookbook that your mom has. Pick 1 or 2: 
	1. Cupcakes 
	2. Strawberry Shortcake
	''')
	if cooking == '1':
		print('You, your sister, and your parents decide to make red velvet cupcakes with blue frosting to match the 4th of July theme. You decide to work on your frosting piping skills next time you make cupcakes. Nevertheless, everything turned out great.') 
	if cooking == '2':
		print('After struggling to cut the strawberries into even slices, you whip up the frosting. Some of it accidentally splattered on your sisters face. Oops! Then you layer each ingredient. First the cake, then whipped cream, then strawberries, then cake, then whipped cream, and finally, strawberries on top in a cool design.')
	print('It was fun for you to do this family activity, since sometimes you feel bored and isolated while in quarantine.')

def day13():
	...
	# halloween = input('What did you dress up as for halloween?     ')

	# At 8:00 p.m you join a Facetime meeting with your friends and show off your (insert user answer) costume. One of your friends dressed up as Hermione Granger from the Harry Potter series. Your other friend dressed up as Jim from The Office, and another dressed up as a blessing in disguise. That friend had taped the word blessing on her shirt and put on a funny mask to disguise their face. 
	# print("\U0001F923")Very  funny. 
	# winner = input('Who do you think won?   ')

	# Your friends totally agree that (insert user answer) won.

	# fun = input('Later that night your family decides to do a fun family activity. You have two options. Pick 1 or 2:
	# 1.Play monopoly 
	# 2.Watch a halloween movie     
	# ')

	# if fun == '1':
	# 	print('It was really fun, but you got annoyed like 50% of the time, because you kept landing on really expensive properties.')

	# if fun == '2':
	# 	movie = input('Which movie (your little sister is watching too)? Pick 1,2, or 3: 1.Hocus Pocus
	# 	2.The Nightmare Before Christmas
	# 	3.Spooky Buddies. 
	# 	if movie == '1' or '2':
	# 		print('Good Pick. Your family really enjoyed it!')
	# 	if movie == '3':
	# 		print('The puppies were cute, but you kind of regret not picking The Nightmare Before Christmas. Still fun though.')

def day14():
	dinner = input('''WHAT DO YOU PUT ON YOUR PLATE? 1.Turkey, Mashed Potatoes, Cranberry Sauce
	2.Turkey, Green Beans, Gravy
	3.Turkey, Gravy, Ham, Mashed Potatoes.
	''')
	if dinner == '1':
		print('Good choice. The cranberry sauce was actually better than you thought it would be.')
	if dinner == '2':
		print('The turkey and green beans weren\'t really enough for you to be full, so you grabbed some ham and mashed potatoes. YUM!')
	if dinner == '3':
		print('This meal was pretty heavy on the meat and gravy. You considered getting some green beans, but decided not to, since you were getting really full.')

def day15():	
	sister = input('It’s time to take care of your sister. She needs to get some homework done. Which will you do first? English or Math ?        ')

	if sister == 'english':
		print('You and your sister read a book together and you ask her to write/tell you a summary of it. Then, you guys work on some of her spelling words together.')

	if sister == 'math':
		print('Your sister struggles a little bit with math, so it takes a bit longer for her to finish her math homework. You occasionally get to some math problems that you struggle to explain to your little sister if she is confused.')

def day17():	
	action = input('''WHAT WILL YOU DO? Pick 1 or 2.
	1. Post about your fustrations on social media
	2. Tell your friend''')

	if action == '1':
		print('You decide to post a news article about the parties that people have been pulling. It made you feel good when you saw others posting about it too.')
	if action == '1':
		print('You decide to tell your friend about it. She agrees with you and expresses her fustration with it too. You\'re happy that you were able to let out her anger in a good way.')

def day19():		
	australia = input('''What will you do? Pick 1 or 2.
	1.Donate money to an organization
	2.Post about this issue on social media to bring awareness
	''')

	if australia == '1':
		print('You and your parents donate $300 dollars to help animals get refuge and help.')
	if australia == '2':
		print('More than 100 people saw your post, and now they are posting about it too.')

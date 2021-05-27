import random
import time
from . import Term
from .math import addition, subtraction, division, multiplication
from .eng import questions as english_questions
from .sci import ask_sci as sci

# It may help to push
# `ctrl K` and then `ctrl [`
# to collapse the functions
# to make it easier to readT

def ask_math(amount):
	for i in range(amount):
		types = [addition, subtraction, division, multiplication]
		type_to_do = random.randint(0, 3)
		types[type_to_do]()
def ask_eng(amount):
	for i in range(amount):
		english_questions()
def ask_sci(amount):
	for i in range(amount):
		sci()
term = Term()
goto = lambda day: day
pause = lambda: time.sleep(0)
red = lambda: print(term.red, end='')
bold = lambda: print(term.bold, end='')
blue = lambda: print(term.blue, end='')
green = lambda: print(term.green, end='')
orange = lambda: print(term.orange, end='')
purple = lambda: print(term.purple, end='')
italic = lambda: print(term.italic, end='')
normal = lambda: print(term.normal, end='')
italics = lambda: print(term.italic, end='')
underline = lambda: print(term.underline, end='')

def day1a():
	breakfast = input('''Pick either 1,2, or 3:
	1. Cereal and Milk
	2. Eggs and Bacon
	3. Pancakes/Waffles
	>>> ''')
	if breakfast == '1':
		cereal = input('''What cereal do you want??? Pick either 1,2, or 3.
	1. Captain Crunch
	2. Cinnamon Toast Crunch
	3. Honey Nut Cheerios
	>>> ''')
		if cereal == '1':
			print('Really yummy, but you forgot about how it always hurts the roof of your mouth :(')
		if cereal == '2':
			print('Cinnamon Toast Crunch is sooooo good. You wish you could have it for breakfast everyday, but you know your parents won\'t let you.')
		else:
			print('Nice and simple. You could never get tired of Honey Nut Cheerios. :)')
	elif breakfast == '2':
		bread = input('Do you want some toast with your eggs and bacon? Yes or No')
		if bread.lower()[0] == 'y':
			print('It was a nice addition to your breakfast and balanced the saltiness of the bacon.')
		else:
			print('A little bit too salty. Probably because you spinkled too much salt on top of your eggs. Ooops. You\'ll get it next time.')
	else:
		choice = input('''Pick either 1 or 2.
	1. Pancakes 
	2. Waffles
	>>> ''')
		if choice == '1':
			pancake_type = input('''You always say yes to pancakes. Now, what type of pancakes do you want? Pick either 1,2, or 3.
	1. Chocolate Pancakes
	2. Blueberry Pancakes
	3. Plain Buttermilk Pancakes
	>>> ''')
			if pancake_type == '1':
				print('You definately have a sweet tooth. Great choice!')
			if pancake_type == '2':
				print('The blueberries weren\'t really ripe enough, so some of them were sour. That\'s okay though. The pancakes were still amazing!')
			else:
				print('Original is good enough for you. Yummy!')
		else:
			print('Waffles are just the best. You know that your friend would not agree with you though.')	
def day1b():
	user_answer = input('''You can pick one of the following options:
	1. Try to go to a different part of the house to see if the connection is better there.

	2. Email your teacher about what's going on.
	>>> ''')

	if user_answer in ('1',  '2'):
		print(f'''{term.green('Zoom finally worked!')}

You got into your first class, pre-Algebra.

You breathe a sigh of relief. Your heart was still racing rapidly and you have a bit of a headache from the stress of all that.

However, after that first Zoom meeting, you kind of get the jist of things, and joining the rest of your Zoom meetings is easier.

Nothing more to worry about for the rest of the day. 

Teachers were just going over work and explaining how Zoom classes would work.

{term.green('First day, complete. Phew!')}''')	
	else:
		print(term.red('You didn\'t pick 1 or 2!!')+'\nUnfortunately, Zoom continues to give you problems.')

def day2a():
	user_supplies = input('1. Canned Food\n2. Packs of Water\n>>> ')
	if user_supplies == '1':
		canned_food = input('Do you pick:\n1. Beans and Tuna\n2. Veggies and Soup\n>>> ')

		if canned_food == '1':
			print('You decided to pick beans and tuna because that was what you thought you grandparents, aunt, and cousins would make more use for.')
		else:
			print( 'You decided to pick veggies and soup because you didn\'t see any other options')
	else:
		user_water = input('1 or 2 packs of water? ')
		if user_water == '1':
			print('You decide to get only 1 pack, because you only want to get what will last for good amount of time.')
		else:
			print('You decide to get 2 just in case another problem arises.')
	print('Good Job! Time to go checkout and head back home.')
def day2b():
	watch = input('''What should you watch? Pick either 1 or 2.
	1. Hulu
	2. Netflix
	>>> ''')
	if watch == '1':
		print('Nice! Your parents had purchased a Hulu membership a few weeks ago, and you\'ve been spending a lot of your time watching the movies on there.')

		show = input('''What movie/show do you want to watch?

	1. The Office
	2. Mean Girls
	>>> ''')
		if show == '1':
			print('All time classic. You\'ve already watched the whole thing like 5 times now, but you just love it so much!')

		else:
			print('You\'ve never watched Mean Girls before, and wanted to give it a try. You had heard many people talk about it. It was pretty good and enjoyable!')
	else:
		netflix = input('''What to watch???
	1. The Umbrella Academy
	2. Stranger Things
	>>> ''')
		if netflix == '1':
			print('You wanted to watch something new, so you chose The Umbrella Academy. It was amazing! You couldn\'t believe that you didn\'t want to watch it before!')
		else:
			print('Stranger Things is definately one of your most favorite shows. The storyline and characters are awesome!')

def day3a():
	ask_math(5)
	ask_eng(3)
	ask_sci(1)
	outcome = random.randint(1,2)
	if outcome == 1:
		print('You are able to get about 80% of your homework done.\nHowever, the second science homework is taking longer than you expected.\nIt is now 5:55 p.m. You would need at least 30-40 more minutes to finish your homework, but you wouldn’t be able to turn it in on time.\nYou just decide to turn in what you finished, really stressed and upset about now managing your time. ')
	elif outcome == 2:
		print('After doing your 2 science homeworks first, you realize that you only have 30 minutes\nleft to finish your algebra and english homework.\nYou try to cram everything into the 30 minutes you have left and you turn everything in\njust in time, but your homework quality isn\'t that great.')
def day3b():
	feeling = input('''How do you feel about this?Pick either 1 or 2.
	1. Upset
	2. Saw it coming, and accepting it.
	>>> ''')
	if feeling == '1':
		print('It is upsetting, and you\'d rather not think about it too much.')
	else:
		print('It wasnt like it wasn\'t going to happen. Of course it is upsetting, but what could you do about it.')

def day4a():
	user_input = input('HOW WILL YOU SOLVE THIS PROBLEM?\nPick 1 or 2:\n\t1.Create a handwritten planner.\n\t2.Create a To-do list on your phone.\n>>> ')
	if user_input == '1':
		print('You use a ruler and a pen to make your planner look neat and make it easy to understand.\nYou make a column for each day and list out your homeowrk for the week.\nYou decide to place it right next_ to your computer so it\'s easy to see.\nWoo-hoo!\nYou feel good about yourself.')
	if user_input == '2':
		print('You download a daily weekly planner app on your phone.\nIt has cool designs and includes a monthly planner too.\nYou allow the app to notify you every morning so you could go over your plans for the day.\nThis is really helpful for you, since you have your phone with you most of the day.')
def day4b():
	ask_math(5)
	ask_eng(5)
	ask_sci(5)

def day5a():
	post = input('Do you want to post about it on social media? Yes or No?')
	if post.lower() == 'yes':
		um = input('''Pick either 1 or 2.
	1. Post a news article
	2. Post Black Lives Matter artwork
	>>> ''')
		if um == '1':
			print('You are happy with your choice.')
		else:
			print('You spent some time finding a respectful and appropriate artwork to post and are happy with the result!')
	else:
		print('You decide to just take more time to process the situation.')
def day5b():
	you = input('''You have two answer options. Pick either 1 or 2.
	1. awesome
	2. I mean, who hasn't, right?
  >>> ''')
	if you == '1':
		print('You regret ending the conversation there, but you can’t come up with anything to say. Maybe next_ time, you think to yourself.')
	else:
		print('''
	F: other than that, it's kinda overwhelming with all the homework we have.

	Y: ‘yeah, I felt that way too. You should totally try to make a planner. It helped me a lot.

	F: Good idea, I should probably start doing that so I don’t fail my classes.

	F: I also have to take care of my baby sister so it’s hard sometimes to finish my homework.''')

		yes = input('''Pick a suggestion. Pick either 1,2, or 3.
	1. Make a weekly/monthly schedule.
	2. Find safe and fun activities for your sister to do while you're doing your homework.
	3. We can help eachother with homework on Zoom!
	>>> ''')

		if yes == '1':
			print('''F: That’s a great idea, thanks!
	Y: Np!''')
		elif yes == '2':
			print('''F: 'I don't know what activities though . . . I'll probably just search some up!'

	Y: Sounds great!''')

		else:
			print('''F: Yes, that would help a lot. Thanks!

	Y: Yeah, it'll be super fun!''')

def day6a():
	supply_stuff = input('WHAT SUPPLIES WILL YOU DROP OFF?\n>>> ')
	meal_stuff = input('WHAT MEALS WILL YOU GIVE THEM?\n>>> ')
	print(f"""Later that day, your parents drive you to your grandparents' house.

	Wearing gloves, you carry the box with the supplies and meals and place it in front of the front door.

	You ring the doorbell and run back to the front driveway, a safe distance away.

	Your aunt opens the door and waves at you, your cousins behind her, your grandparents watching from the window.

	You smile (the smile being hidden by the mask you’re wearing) and say hi to everyone, happy to see them again.

	On the way home, your aunt calls your parents and thanks them for the {meal_stuff} and the {supply_stuff}.""")
def day6b():
	active = input('''What should you do? Pick either 1 or 2.
	1. Start to go on walks
	2. Play outside with your sister more
	>>> ''')
	if active == '1':
		print('It was really enjoyable. It gives you time to relax and de-stress. Plus, it gives you time to get some exercise.')
	else:
		print('It was really nice to spend time with your sister. It was super fun!')

def day7a():	
	look = input('''Where do you look first? 
	1. Behind the bush 
	2. next_ to the steps of your porch 
	3. Right side of the garden 
	>>> ''')
	if look in ('1', '2'):
		print('Not there!')
	else:
		print('Good Job! You found her!')
	pause()

	look = input('''Round 2:
	1. Left side of the garden 
	2. Behind the bush 
	3. Behind the chicken coop 
	>>> ''')
	if look in ('1', '3'):
		print('Not there!')
	if look == '2':
		print('Good Job! You found her!')
	pause()

	look = input('''Round 3: 
	1. next_ to the step of your porch
	2. Behind the chicken coop
	3. Behind the bush
	>>> ''')
	if look in ('1', '3'):
		print('Not there!')
	if look == '2':
		print('Good Job! You found her!')
def day7b():
	ask_math(5)
	ask_eng(5)
	ask_sci(1)

def day8a():	
	yearbook = input('''Where do you look first.?
	1. 8th Grade Class Pictures
	2. Spirit Week
	3. 8th Grade Baby Pictures.
	>>> ''')

	if yearbook == '1':
		print('You scan through the faces of your classmates and friends. It hits you that you haven’t seen each other in person in a long time. You really miss talking to your friends and hanging out with them.')
	if yearbook == '2':
		print('When you were still in school, you were part of the soccer team. It was really fun going to the soccer games and practicing with your teammates. You hope that you’ll be able to meet up with your classmates soon after Covid-19 restrictions lighten up.')
	else:
		print('You spot your baby pictures, and you burst out laughing. Your dad had selected your baby pictures for you. You didn’t even remember submitting it. In the pictures, you are sitting on the ground next_ to some foam building blocks. One of your hands holding a t.v remote in your mouth, and the other hand holding a foam building block next_ to your ear.')
def day8b():
	party = input('''What do you want to do for your at home celebration? Pick either 1 or 2.
	1. Play a board game
	2. Bake something
	>>> ''')
	if party == '1':
		game = input(''' What game? Pick either 1,2, or 3.
	1. Game of Life
	2. Monopoly
	3. Sorry
	>>> ''')
		if game == '1':
			print('This has been your most favorite game ever since you were little. By the end of the game, you ended up haveing 6 children, haha!')
		elif game == '2':
			print('Fustrating, but fun :)')
		else:
			print('You forgot how bad you were at this game, haha. At least you had fun, though!')
	else:
		sell = input('''What do you want to bake?Pick either 1 or 2.
	1. Cookies
	2. Brownies
	>>> ''')
		if sell == '1':
			cookie = input('''What type of cookie? Pick either 1,2, or 3.
	1. Chocolate Chip Cookie
	2. Red Velvet White Chocolate Chip Cookie
	3. Sugar Cookie
	>>> ''')
			if cookie == '1':
				print('Classic and Yummy!')
			elif cookie == '2':
				print('You heard that red velvet is just chocolate dyed red, but it doesn\'t taste the same to you. Huh, still amazing and delicious!')
			else:
				print('The sugar cookies were really fun to decorate! Your favorite was your star shaped cookie.')
		else:
			print('Yum! The brownies were a success.')

def day9a():
	cooking = input('''Two things stand out to you the most in the baking cookbook that your mom has.\nWhat should you make?: 
	1. Cupcakes 
	2. Strawberry Shortcake
	>>> ''')
	if cooking == '1':
		print('You, your sister, and your parents decide to make red velvet cupcakes with blue frosting to match the 4th of July theme. You decide to work on your frosting piping skills next_ time you make cupcakes. Nevertheless, everything turned out great.') 
	if cooking == '2':
		print('After struggling to cut the strawberries into even slices, you whip up the frosting. Some of it accidentally splattered on your sisters face. Oops! Then you layer each ingredient. First the cake, then whipped cream, then strawberries, then cake, then whipped cream, and finally, strawberries on top in a cool design.')
	pause()
	print('It was fun for you to do this family activity, since sometimes you feel bored and isolated while in quarantine.')
def day9b():
	call = input('''You decide to call 2 people today. Who do you call first? Pick either 1 or 2.
	1. Friend
	2. Cousin
	>>> ''')
	if call == '2':
		print('You and your friend talk about what your friend will do for the 4th of July. Your friend gave you a pretty good idea to make some strawberry shortcake. Your friend also suggests for you to play a vido of 4th of July fireworks on your T.V, so you wouldn\'t miss out on fireworks this year. Good idea:)')
	if call == '2':
		print('You and your cousin talk about classes and homework. You guys are the same age, so you can relate a lot with eachother. It was funny to watch your cousin put halloween costumes on her dogs. Your favorite costume was the lion one.')

def day10a():	
	next_ = random.randint(1,2) # variables can't be named next so I added the underscore
	if next_ == '1':
		print('You’ve not been feeling yourself lately. It feels like you’re alone and isolated. You also haven’t had any social interaction outside of your family in a while. You’ve developed cabin fever. You need some way to vent out your emotions, but you don’t know how. You decide to search online about strategies you can use. One thing that caught your eye was journaling. You decide to give it a try.')

		journal = input('''What do you want to write about? Pick 1 or 2.              
		1. Struggles, Daily Emotions, How Different Interactions Made You feel
		2. Goals, Motivation, Daily Emotions''')

		if journal == '1':
			print(' You actually really like it. It was a nice way to track your mood and patterns. You decide to do it for a few more days to see how it goes.')
		else:
			print('It supprisingly did motivate you to be more productive. Cool! You decide to incorporate journaling more in your lifestyle.')

	if next_ == '2':
		print('''You decide to text your friend. . .
		Y: Hi, do you have time to talk?
		F: Yup, I have time to talk 90% of the time.
		Y: How have you been doing in quarantine? I think I’m starting to get cabin fever.
		F: Me too, I really hope that we can see each other in person soon.
		Y: Yeah, it's hard to not be able to meet up with friends. I feel trapped. 
		F: I totally understand. ''')
		c = input('Do you want to continue the conversation? Type \'yes\' or \'no\'.')
		if c == 'yes' or 'Yes':
			response = random.randit(1,2)
			if response == '1':
				print('''
				F: Quarantine has really taken a toll on people.
				Y: Yeah, many people are losing their jobs or are being laid off. 
				F: And a lot of those people have family to support or they are trying their best to get well off. 
				Y: Yes, and small businesses too. 
				F: Exactly, once restrictions lighten up and we are supposed to be home 24/7, then we should totally visit some small businesses and support them!
				Y: That sounds great, I’m looking forward to it.
				Y: Thanks for talking to me, it really helped.
				F: No problem, let's talk again tomorrow. It really helped me get some social interaction.''')

			if response == '2':
				print('''
				Y: Are you excited to be a freshman in high school?
				F: Super excited, but it’s not going to be the same experience as being in person.
				Y: Yeah, we have to miss out on Homecoming. I was really looking forward to it.
				F: It’s also our first year of high school, so it's kinda upsetting that we can’t have the full experience. Classes are going to be so different. 
				''')
		if c == 'no' or 'No':
			print('Y: Thanks for talking with me. I got to go now. Byeeeeee!')
def day10b():
	look = input('''Where do you look first? 
	1. Next to the book shelf 
	2. Behind the couch
	3. Under her bed
	>>> ''')
	if look in ('3', '2'):
		print('Not there!')
	if look == '1':
		print('Good Job! You found her!')
	pause()

	look = input('''Round 2:
	1. In your parent\'s closet 
	2. In the laundry room 
	3. In the kitchen cabinet 
	>>> ''')
	if look in ('1', '3'):
		print('Not there!')
	if look == '2':
		print('Good Job! You found her!')
	pause()

	look = input('''Round 3: 
	1. Under your desk
	2. In her toy container
	3. Behind your bedroom door
	>>> ''')
	if look in ('2', '3'):
		print('Not there!')
	if look == '1':
		print('Good Job! You found her!')

def day11a(): pass
def day11b():
	ask_eng(10)
						
def day12a():
	ask_math(2)
	ask_sci(5)
def day12b():
	print('TIME TO PLAY: THIS OR THAT!')
	one = input('Morning or Night?')

	two = input('Cat or Dog?')

	three = input('City or Country?')

	four = input('Text or Call?')

	five = input('Summer or Winter?')

	five = input('Love or Money?')

	six = input('Fire or Ice?')
	
	print('Hm, it was hard to choose for some of them.')

def day13a():
	costume = input('What did you dress up as for halloween?\n>>> ')
	pause()
	print(f"At 8:00 p.m you join a Facetime meeting with your friends and show off your {costume} costume. One of your friends dressed up as Hermione Granger from the Harry Potter series. Your other friend dressed up as Jim from The Office, and another dressed up as a blessing in disguise. That friend had taped the word blessing on her shirt and put on a funny mask to disguise their face.")
	pause()
	print("\U0001F923 Very funny.") 
	winner = input('Who do you think won?   ')
	pause()
	print(f"Your friends totally agree that {winner} won.")
	fun = input('''Later that night your family decides to do a fun family activity. You have two options.
	1.Play monopoly 
	2.Watch a halloween movie     
	>>> ''')
	pause()
	if fun == '1':
		print('It was really fun, but you got annoyed like 50% of the time, because you kept landing on really expensive properties.')
	else:
		movie = input('''Which movie (your little sister is watching too)?
		1. Hocus Pocus
		2. The Nightmare Before Christmas
		3. Spooky Buddies. 
		>>> ''')
		if movie in ('1', '2'):
			print('Good pick. Your family really enjoyed it!')
		else:
			print('The puppies were cute, but you kind of regret not picking The Nightmare Before Christmas. Still fun though.')
def day13b():
	print('SCAVENGER HUNT BEGINS! Find as many items as you can before the timer runs out!')
	scavenger = input('''
	THINGS YOU NEED TO FIND 

	1. a purple book
	2. a ghost
	3. something orange
	4. candy with a red wrapper
	5. a piece of string.
	
	Where will you look first? Pick either 1 or 2.
	1. the office 
	2. the kitchen
	 ''')
	if scavenger == '1':
		print('Sadly, you were only able to find a piece of string. You were hoping to find the book and something orange, but you didn\'t see any. Maybe your parents or sister got to it first.')
	if scavenger == '2':
		print('Wow, you found a ghost plushy, a KitKat, and a purple recipe book!')
	print('Dang it, you ran out of time! You compare the things you got with your family. You lost by one item! Your dad won the game. Maybe next year, haha :(')

def day14a():
	dinner = input('''WHAT DO YOU PUT ON YOUR PLATE?
	1.Turkey, Mashed Potatoes, Cranberry Sauce
	2.Turkey, Green Beans, Gravy
	3.Turkey, Gravy, Ham, Mashed Potatoes.
	>>> ''')
	if dinner == '1':
		print('Good choice. The cranberry sauce was actually better than you thought it would be.')
	if dinner == '2':
		print('The turkey and green beans weren\'t really enough for you to be full, so you grabbed some ham and mashed potatoes. YUM!')
	else:
		print('This meal was pretty heavy on the meat and gravy. You considered getting some green beans, but decided not to, since you were getting really full.')
def day14b(): pass

def day15a():	
	sister = input('It’s time to take care of your sister. She needs to get some homework done. Which will you do first? English or Math ?        ')
	if sister == 'english':
		print('You and your sister read a book together and you ask her to write/tell you a summary of it. Then, you guys work on some of her spelling words together.')
	else:
		print('Your sister struggles a little bit with math, so it takes a bit longer for her to finish her math homework. You occasionally get to some math problems that you struggle to explain to your little sister if she is confused.')
def day15b():
	ask_math(5)
	ask_eng(5)
	ask_sci(1)

def day16a():
	ask_eng(5)
def day16b():
	print('''Would You Rather! Let's Start!
	Pick either 1 or 2.')
	one = input('
	1. Go into the past to meet your ancestors
	
	or 
	
	2. Go into the future to meet your great-great-great grandchildren
	
	''')
	two = input('''
	1. Have more time
	
	or 
	
	2. Have more money
	
	''')
	three = input('''
	1. Be able to talk to animals
	
	or 
	
	2. Speak all foreign languages
	
	''')
	four = input('''
	1. Forever say EVERYTHING on your mind
	
	or
	
	2. Never speak again
	
	''')
	five = input('''
	1. Never make a phone call ever again
	
	or 
	
	2. Never text ever again
	
	''')

def day17a():	
	action = input('''WHAT WILL YOU DO?
	1. Post about your fustrations on social media
	2. Tell your friend
	>>> ''')

	if action == '1':
		print('You decide to post a news article about the parties that people have been pulling. It made you feel good when you saw others posting about it too.')
	else:
		print('You decide to tell your friend about it. She agrees with you and expresses her fustration with it too. You\'re happy that you were able to let out her anger in a good way.')
def day17b(): pass

def day18a():
	ask_eng(2)
	ask_math(2)
	ask_sci(2)
def day18b(): pass

def day19a():		
	australia = input('''What will you do? Pick 1 or 2.
	1.Donate money to an organization
	2.Post about this issue on social media to bring awareness
	>>> ''')
	if australia == '1':
		print('You and your parents donate some money to help animals get refuge and help.')
	else:
		print('More than 100 people saw your post, and now they are posting about it too. Good job!')
def day19b():
	ask_math(5)
	ask_eng(5)
	ask_sci(3)

def day20a():
	ask_math(5)
	ask_eng(4)
	ask_sci(2)
def day20b():
	support = input('Resturaunt or Bakery?                 ')
	if support == 'Resturaunt' or 'resturaunt':
		then = input('''Pick either 1 or 2.
	1. Italian Food
	2. Thai Food 
		>>> ''')
		if then == '1':
			print('Yum, you picked up some Shrimp Scampi and Fettucine Alfredo.')
		if then == '2':
			print('You got some Pad Thai and and Panang Curry. Yum!')
		if support == 'Bakery' or 'bakery':
			print('You decided to go to a bakery 5 minutes away from your house. You got an everything bagel, a plain bagel, chocolate chip cookie, a scone, and a slice of apple pie. Delicious!')

def day21a():
	addition()
	addition()
	addition()
	addition()
	addition()
	addition()
def day21b():
	ask_math(5)
	ask_eng(5)

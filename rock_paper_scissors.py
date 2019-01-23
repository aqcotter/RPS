#rock paper scissors
import random
print("Welcome to Rock, Paper, Scissors")
try:
	plays = int(input("How many times would you like to play?"))
except:
	plays = int(input("Please use numeric characters (ex.1, 3, 5).  How many times would you like to play?"))
times_played = 0
computer_score = 0
user_score = 0

#FUNCTIONS
def game(user_choice, computer_choice):
	#randomly get computer choice
	winner = ""
	if user_choice == computer_choice:
		winner = False
	elif user_choice == "rock" and computer_choice == "paper":
		winner = "computer"
	elif user_choice == "rock" and computer_choice == "scissors":
		winner = "user"
	elif user_choice == "paper" and computer_choice == "rock":
		winner = "user"
	elif user_choice == "paper" and computer_choice == "scissors":
		winner = "computer"
	elif user_choice == "scissors" and computer_choice == "rock":
		winner = "computer"
	elif user_choice == "scissors" and computer_choice == "paper":
		winner = "user"
	return winner

def tiebreaker():
	user_answer = input("Tie! Play a tie breaker? (yes or no)")
	user_answers = ["yes", "no"]
	global user_score
	global computer_score
	computer_choices = ["rock", "paper", "scissors"]
	if user_answer not in user_answers:
		user_answer = input("Please answer YES or NO.  Would you like to play again?").lower()
	if user_answer == "yes":	
		user_choice = input("Heck yes! Choose wisely ... rock, paper, or scissors?").lower()
		print("You chose: ", user_choice)
		computer_choice = computer_choices[random.randint(0,2)]
		print("Computer chose", computer_choice)
		result = game(user_choice, computer_choice)
		if result: 
			if result == "computer":
				print("Computer won. GAME OVER.")
				computer_score=computer_score+1
			if result == "user":
				print("You win! GAME OVER.")
				user_score=user_score+1
		else:
			tiebreaker()
	else:
		print("GAME OVER. Bye bitch.")
#END OF FUNCTIONS

while times_played < plays:
	user_choice = input("Choose rock, paper, or scissors: ").lower()
	print("You chose", user_choice)
	computer_choices = ["rock", "paper", "scissors"]
	if user_choice not in computer_choices:
		user_choice=input("Your choice was not one of 'rock', 'paper', or 'scissors'. Please choose again: ").lower()
	computer_choice = computer_choices[random.randint(0,2)]
	print("Computer chose", computer_choice)
	result = game(user_choice, computer_choice)
	if result: 
		if result == "computer":
			print("Computer won.")
			computer_score=computer_score+1
			times_played=times_played+1
		if result == "user":
			print("You win!")
			user_score=user_score+1
			times_played=times_played+1
	else:
		print("It's a tie.")

winner_states = [ "WOOHOO! YOU'RE A WINNER!", "Well DONE. You've WON!", "By George, you've done it! Congratulations, you won!", "Artificial Intelligence? More like Artifical LOSER, you beat the computer!!", "Winner, winner, chicken dinner! You win!"]
loser_states = [ "Boooo, you stink!", "Ya lost, ya filthy animal!", "Oh noooooo, the computer beat you!", "Womp, womp, womppppp.  You lost.", "OH NO! YOU LOSE."]
if user_score > computer_score:
	print(winner_states[random.randint(0,4)])
if computer_score > user_score:
	print(loser_states[random.randint(0,4)])
if user_score == computer_score:
	tiebreaker()
			
print("You:", user_score, "Computer:", computer_score)


#Make a function to continue on 'play again' 




import random
from art import logo

def number():  
  #print(f"psst the number is {no} ")
  return no

def difficulty():
  if choose=='easy':
    lives=10
    print(f"You have {lives} attempts remaining to guess the number.")
    return lives
  elif choose=='hard':
    lives=5
    print(f"You have {lives} attempts remaining to guess the number.")
    return lives

def make_guess():
  global no_attempts
  if your_guess>number():
    no_attempts-=1
    if no_attempts==0:
      print("You've run out of guesses, you lose")
    else:
      print("Too high. \nGuess Again ")
      print(f"You have attempts {no_attempts} remaining to guess the number")
  elif your_guess<number():
    no_attempts-=1
    if no_attempts==0:
      print("You've run out of guesses, you lose")
    else:
      print("Too low. \nGuess Again ")
      print(f"You have attempts {no_attempts} remaining to guess the number")
  if your_guess==number():
    no_attempts=0
    print(f"You got it! The answer was {number()} ")


print(logo)
#Welcome message
welcome=input("Welcome to the Number Guessing Game!")
Computer_thinking=print("I am thinking of a number between 1 and 100")
#Number guessed by the program
no=random.randint(1,100)
no_to_guess=number()
#Choose difficulty
choose=input("Choose a difficulty. Type 'easy' or 'hard': ")
no_attempts=difficulty()
#User's guess
while no_attempts>0:
  your_guess=int(input("Make a guess: "))
  answer_guess=make_guess()





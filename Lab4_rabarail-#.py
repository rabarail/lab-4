"""Program name: Guess the number - Hangman Style
AUthor: Rajani Baraili
Purpose: guess random number between 1 and 15. Each guess reveals part of hangman drawing.
Starter code: None
Date:02/09/2026"""
import random
random_number = random.randint(1, 15)
print("Welcome to Guess the Number - Hangman Style!")
print("I have selected a random number between 1 and 15.")      
print("You have 6 attempts to guess the number.")
hangman_stages = [
"""
_________
|        |
|
|
|
|
============ """
,  """
_________
|        |
|        0
|
|
|
============ """
, """   
_________
|        |
|        0
|        |
|
|
============ """
, """   
_________
|        |
|        0
|       /|
|
|
============ """
, """   
_________
|        |
|        0
|       /|\ 
|
|
============ """
, """   
_________
|        |
|        0
|       /|\ 
|       /
|
============ """
, """
_________
|        |
|        0
|       /|\ 
|       / \ 
|
============ 

"""
]
attempts = 0
while attempts < 6:
    guess = int(input("Pease enter your guess: "))
    if guess == random_number:
        print("Congratulations! You've guessed the number correctly!")
        break
    elif guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    print(hangman_stages[attempts])
    attempts += 1
if attempts == 6:
    print("Game Over! You've used all your attempts. The correct number was:", random_number)
    
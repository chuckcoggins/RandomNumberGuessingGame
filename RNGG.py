# This is a Random Number Guessing Game
import random

print('Please type in your name:')
name = input()

print('Hello, ', name, 'Welcome to the Random Number Guessing Game! \n')

randomSecNum = random.randint(1, 20)

print(name, 'I am thinking of a number between 1 and 20, can you guess what it is?')

# Player gets 6 chances to guess correctly
for takenGuesses in range(1, 7):
    print('Take a guess!')
    guess = int(input())
    if guess < randomSecNum:
        print('Nope, your guess is too low!')
    elif guess > randomSecNum:
        print('Nope, your guess is too high!')
    else:
        break  # this condition happens if the guess is correct

if guess == randomSecNum:
    print('Nice Job,', name + '! You guessed the correct number in', str(takenGuesses), 'tries!')
else:
    print('You lose! The number I was thinking of was', str(randomSecNum))

# RandomNumberGuessingGame
A Random Number is created. You guess it.

This was part of another project from another Udemy.com class I am taking.
It is a Random Number Generator Guessing Game.

The idea is the game creates a random number using random.randit(1, 20) and I store that number in the randomSecNum variable.
Then the user makes a guess and that number is stored in the variable guess.
If the guess is to low it says its too low, if it is too high it prints it is too high.

Our main loop is using range(1, 7):
which gives our users 6 chances to guess the number correctly.
We used the range(1, 7) instead of just doing range(6) so we would be able to then tell the user how many guess it took them to get the correct answer.

If the user does not figure out the correct number in 6 tries it will tell them they lose and it will tell them what the correct answer (randomSecNum) was.

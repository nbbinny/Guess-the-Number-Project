import random


play_again = 'yes'

while play_again == 'yes' :
    secret_number = random.randint(1,10)
    num_guesses = 0
    while num_guesses < 3:
        guess = input("Guess a number between 1 and 10:")
        guess = int(guess)
        num_guesses += 1
        if guess == secret_number: 
            print("Correct! You guessed the number in", num_guesses, "attempts")
            break
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    else:
        print("Sorry, you ran out of guesses. The secret number was", secret_number)
        play_again = input("Do you want to play again? (yes or no)")
        



        


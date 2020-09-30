import random

# decide the range of random number
secret = random.randrange(1, 101)

# vaiables 
guess = 0 # Storing a guesses
tries = 0 # counting no of guesses

#running a loop for running our game continously
while guess != secret:
    guess = int(input("Make a guess: "))
    tries = tries + 1
    
    # checking the guesses
    if guess > secret:
        print("Too High!")
    elif guess < secret:
        print("Too Low!")
    else:
        print("You got it!")

# printing the number of tries
print("Number of tries:", tries)

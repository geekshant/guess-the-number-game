# we are going to write a programm that generates a random number and ask the user to guess it

# if the player's guess is higher than the actual number, the programm displays "lower number please". similarly, if the user's guess is too low, the programm displays " higher number please" when the user guess the correct number, the programm displays the number of guesses the player used to arrive at the number. 

import random

n = random.randint(0, 100)

user = -1

guess = 0

while(user != n):
    guess += 1
    user = int(input("guess a number: "))
    
    if(user>n):
       print("lower number please")
    
    elif(user<n):
        print("higher number please")
    
    else:
        print(f"you have guessed the correct number and you took the {guess} chances to guess the number")
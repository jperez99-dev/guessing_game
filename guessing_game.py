#This is a simple guessing game
import random

def guessNumber():
    randomNumber = random.randrange(1,10)
    answer = False
    count = 0
    while answer == False:
        
        try:
            guess = int(input("Please choose a number 1 - 10 "))
            if guess < 1 or guess > 10:  
                raise ValueError
        except ValueError as err:
           print(f"Error: Please enter a numeber 1-10. {err} ")
        else:
            if guess == randomNumber:
                
                print("Congrats you guessed right!")
                print(f"It took you {count} tries")
                print("Thanks for playing!")
                break
            elif guess < randomNumber:
                    print("It's higher")
            else: 
                print("It's lower")
        count+=1

def start_game():
    print("Welcome to my guessing game!")
    guessNumber()


start_game()
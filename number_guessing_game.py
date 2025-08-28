###################################  Number Guessing Project  #####################################################
import random

print("Welcome to the number guessing Game \nyou have only 5 chance to win the Game and make money")
low = int(input("Enter the lower limit of the number:"))
high = int(input ("Enter the higher limit of the number :"))

number = random.randint(low,high)
total_chances = 5
guess_cout = 0

while guess_cout<total_chances:
    guess  = int(input ("Enter your guess:"))
    guess_cout +=1

    if guess== number :
        print(f" congratulations! you won the Game ,You guess the correct number is {number} in guess_count {guess_cout},  ")
        break
    elif guess < number :
        print("Your guess is low , try again")
    
    elif guess >number:
        print("Your guess is high , try again") 
    
    elif guess_cout == total_chances:
        print(f"Sorry! you lost the Game ,The correct number is {number} you lost your all chances.")



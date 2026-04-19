import random
a=random.randint(1,100)
import time
ctrl=0
#Control Variable
G=0
#Number Of guesses
while ctrl==0:
    time.sleep
    b=int(input("Guess the number from 1 to 100: "))
    if b==a:
        print("You win")
        G+=1
        print("Your guesses:",G)
        ctrl+=1
    if b < a:
        print("too low!")
        G+=1
    if b > a:
        print("too high!")
        G+=1
print("rock, paper, scissors")
import random
import math
import time
Y=0
C=0
b=0
ctrl=0
q=input("Play? Press q to quit: ")
while ctrl==0:
    if q!="q":
        time.sleep(1)
        a=random.randint(1,3)
        #1=Rock
        #2=Paper
        #3=Scissors
        b=(input("R, P, or S? or type score: "))
        if b=="score":
            print("Your Score:",Y)
            print("The computer's Score:",C)
        if b=="q":
            ctrl+-1
        if  b=="R" and a==1:
          print("Tie!")
        if  b=="R" and a==2:
            C+=1
            print("You lose")
        if  b=="R" and a==3:
           Y+=1
           print("You win!")
        if b=="P" and a==1:
            Y+=1
            print("You win!")
        if b=="P" and a==2:
            print("Tie")
        if b=="P" and a==3:
           C+=1
           print("You lose")
        if b=="S" and a==1:
            C+=1
            print("You Lose")
        if b=="S" and a==2:
            Y+=1
            print("You win")
        if b=="S" and a==3:
            print("Tie")
        if ctrl==1:
            print("Thanks for playing!")
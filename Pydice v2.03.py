#v1.0 d2, d4, d6, d8, d10, d12 aded
#v1.1 d100 and d3 added
#Made 2/7/2026
#v2.0. All the if var=="" removed. Me just add a var to represent the number of sides
#v2.0 The code was compacted from over 80 lines to just 15 by this change.
#v2.01 Merged with Die of Fate V1.0
#ctrl and a are both control variables
#V1.2.03 Debugged. Compacted to 93 Lines. Efficiency Improved
import random
import time
ctrl=0
print("Type in the number for the mode you want")
print("1. Die roller")
print("2. Die of fate")
d=input("Mode?: ")
var2=0
a=0
if d=="1":
    a=int(input("Type in the number of sides you want on your die: "))
    while ctrl==0:
        b=input("Roll?(y/n): ")
        if b=="y" or b=="Y":
            ctrl=0
            print(random.randint(1,a))
        if b=="n" or b=="N":
            break
            ctrl+=1
if d=="2":
    print("Welcome to the Die of fate")
    sides = int(input("Select how many sides you want on the die (Max is 10): "))
    print("Sides:",sides)
    print("You will now decide what you want on each side of the Die:")
    s1 = input("Side1: ")
    if sides>1:
        s2 = input("Side2: ")
        if sides>2:
            s3 = input("Side3: ")
            if sides>3:
                s4 = input("Side4: ")
                if sides>4:
                    s5 = input("Side5: ")
                    if sides>5:
                        s6 = input("Side6: ")        
                        if sides>6:
                            s7 = input("Side7: ")
                            if sides>7:
                                s8 = input("Side8: ")
                                if sides>8:
                                    s9 = input("Side9: ")
                                    if sides>9:
                                        s10 = input("Side10: ")
    while a==0:
        A=input("Roll your die?(Y or N): ")
        if A=="Y" or A=="y":
            var1 = random.randint(1,sides)
            if var1 == 1:
                    var2=s1
                    print("Roll:",s1)
            if var1 == 2:
                var2=s2
                print("Roll:",s2)
            if var1 == 3:
                print("Roll:",s3)
                var2=s3
            if var1 == 4:
                var2=s4
                print("Roll:",s4)
            if var1 == 5:
                var2=s5
                print("Roll:",s5)
            if var1 == 6:
                print("Roll:",s6)
                var2=s6
            if var1 == 7:
                print("Roll:",s7)
                var2=s7
            if var1 == 8:
                print("Roll:",s8)
                var2=s8
            if var1 == 9:
                print("Roll:",s9)
                var2=s9
            if var1 == 10:
                print("Roll:",s10)
                var2=s10
                
        if A=="N" or A=="n":
                a+=0
                ctrl+=0
                print("Code ended. BTW ur die doesn't save :(")    
                break
                
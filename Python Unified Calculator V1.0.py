import math
import operator
#Pyqc Update log:
#V1.0 +,-, *, /, exponents and sqrt all added. Only beetween 2 numbers though
#v1.1 Real calculator added Mode 7.
#v1.2 Expression Evaluator
#v1.24 MErged with Python Quadratics calculator v1.62
calc=[]
hist=[]
ctrl=0
calcindex= {
  "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow
}
print("Welcome to python calculator V1.0")
print("Modes: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponent")
print("6. Roots")
print("7. Sandbox Calculator")
print("8. Expression evaluator")
print("9. Go to Pyq V1.61 for formula solving")
print("10. Update log")
while ctrl==0:
    a=int(input("Put in number of function: "))    
    if a==1:
        print("Addition: ")
        b=int(input("First number: "))
        c=int(input("Second number: "))
        print(b+c)
        hist.append(b+c)
    if a==2:
        print("Subtraction: ")
        b=int(input("First number: "))
        c=int(input("Second number: "))
        print(b-c)
        hist.append(b-c)
    if a==3:
        print("Multiplication: ")
        b=int(input("First number: "))
        c=int(input("Second number: "))
        print(b*c)
        hist.append(b*c)
    if a==4:
        print("Division: ")
        b=int(input("First number: "))
        c=int(input("Second number: "))
        print(b/c)
        hist.append(b/c)
    if a==5:
        print("Exponent: ")
        b=int(input("Base: "))
        c=int(input("Power: "))
        print(b**c)
        hist.append(b**c)
    if a==6:
        print("Roots: ")
        b=int(input("Number: "))
        c=int(input("Root: "))
        print(b**(1/c))
        hist.append(b**(1/c))
    #Sandbox Calculator
    if a==7:
        print("Python Sandbox Calculator: ")
        clc=0
        while clc==0:
            n1 = input("Enter Expression: ")
            calc.append(n1)
            expression = n1 
            print(calc)
            print(eval(expression))
    if a==8:
        print("Expression Evaluator: ")
        clc=0
        s1=input("Left side of equation: ")
        s2=input("Right side of equation: ")
        evl1=eval(s1)
        evl2=eval(s2)
        if evl1==evl2:
            print(evl1,"=",evl2, ",True")
        else:
            print(evl1,"!=",evl2,",False")
    if a==10:
        print("Update log:")
        print("Pyqc Update log:")
        print("V1.0 +,-, *, /, exponents and sqrt all added. Only beetween 2 numbers though")
        print("v1.1 Real calculator added Mode 7.")
        print("v1.2 Expression Evaluator")
        print("v1.24 Merged with Python Quadratics calculator v1.62")
    c=input("Check history? (y/n): ")
    if c=="y":
        print(hist)
#Pyq Calc v1.61:

#v1.1 this calculator calculates the quadratic formula (QF)
#v1.2 vertex finder (VTXF) added (-b/2a) Finished 1/27/2026
#v1.3 the formula is incorrect, now it is fixed
#v1.4 Efficiency improved
#v1.52 Circle point finder added
#v1.54 Code made loopable
#v1.54 Efficiency Improved. F-c Added.
#v1.54 Instead ofl isting functinos in a sentance, they are listed like bullet points
#v1.6: efficiency Imporved. Old code:
#input("Type value of b on next line")
#b=int(input())
#New version:
#b=int(inout(Type the value of b))
#v1.61 Debugging and Improved efficiency
#5/15/2026 Merged with Python calculator v1.2
    b=0
    c=0
    r=0
    h=0
    k=0
    import time
    if a==9:
        print("Welcome to Python Quadratics Calulator v1.54!")
        print("List of Functions:")
        print("1. QF: Quadratic Formula") 
        print("2. VTXF: Finds the vertex of a parabola")
        print("3. C: Tells you if a point is inside a circle(You put in the equation) ")
        print("4. LCM: FInds least common multiple")
        print("5. F-c: Converts Farenheight to Celcius and vice versa")
        ctrl=0
        while ctrl==0:
          #the calculator runs 2 equations one with b+ and one with b-
            var=input("Select Function and Type number or Abbreviation: ")
            if var=="quit" or var=="Quit":
                ctrl+=1
                print("Code ended. Hit execute to run again")
                print("Made by Delancey B.")
            if var=="QF" or var=="1":
                print("Quadratic Formula Selected")
                b=int(input("Type value of b: "))
                a=int(input("Type value of a: "))
                c=int(input("Type value of c: "))
                w= math.pow(b,2) -4*a*c
                print(w)
                e=w**(0.5) 
                print(e)
                r=(-b + e) / (2*a)
                print("X=",r)
                u=(-b-e) / (2*a)
                print("X=",u)
            if var=="VTXF" or var=="2":
                print("Vertex Finder Seleced")
                A=int(input("type value of A: "))
                B=int(input("Type value of B: "))
                time.sleep(1.5)
                X= (-1 * B) / (2 * A)
                print("The X value of the vertex is", X)
                print("Type in the a,b, and c values of the Quadratic Equation")
                J=int(input("Type value of a: "))
                K=int(input("Type value of b: "))
                L=int(input("Type value of c: "))
                T= math.pow(X,2)
                #Debugging Tool
                print(T)
                Y= T * J + K * X + L
                #Debugging tool
                print("The Y value of the Vertex is", Y)
                print("The vertex is", (X , Y))
            if var=="C" or var=="3":
                print("this code is for a circle with any center you chose") 
                print("Equation:(H-X)^2 +(K-Y)^2 <= r^2")
                x=int(input("Input a X value: "))
                y=int(input("input a Y value: "))
                r=int(input("Input a radius: "))
                h=int(input("Put x coord of circle center: "))
                k=int(input("put y coord of circle center: "))
                b=(x-h)
                c=(y-k)
                if (b**2) + (c**2) >=(r**2) or (b**2) + (c**2) ==(r**2):
                    print("The coordinate lies within the circle")
                if (b**2) + (c**2) <=(r**2):
                    print("The coordinate lies outside the circle")
                time.sleep(0.5)
            if var=="LCM" or var=="4":
                print("This finds the lcm of the 2 numbers you input")
                a=int(input("Number 1: " ))
                b=int(input("Number 2: " ))
                print("lcm:",math.lcm(a,b))
            if var=="F-C" or var=="5":
                a=input('Do you want F->C or C-->F (write FC or CF) ')
            if a=="CF":
                b=int(input("Put in the degrees Celcius: "))
                c= (b*1.8) + 32
                print(c,"degrees Faerenheight")
            if a=="FC":
                b=int(input("Put in degrees Farenheight: "))
                c=(b -32) /1.8
                print(c,"Degrees celcius")
            updl=input("Check update log?: ")
            if updl=="y" or updl=="Y":
                    print("v1.1 this calculator calculates the quadratic formula (QF)")
                    print("v1.2 vertex finder (VTXF) added (-b/2a) Finished 1/27/2026")
                    print("v1.3 the formula is incorrect, now it is fixed")
                    print("v1.4 Efficiency improved")
                    print("v1.52 Circle point finder added")
                    print("v1.54 Code made loopable")                        
                    print("v1.54 Efficiency Improved. F-c Added.")
                    print("v1.54 Instead of listing functions in a sentence, they are listed like bullet points")
                    print("v1.6: efficiency Improved. Old code:")
                    print('input("Type value of b on next line")')
                    print("b=int(input())")
                    print("New version:")
                    print('b=int(input("Type the value of b"))')
                    print("v1.61 Debugging and Improved efficiency")
                    print("5/15/2026 Merged with Python calculator v1.2")
            else: 
                ctrl=0
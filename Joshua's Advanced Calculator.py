from math import *
import time
import random

ExitTerms = ["back", "go back", "exit", "no", "stop", "leave"]
GreetingTerms = ["Alright", "Hello", "Hey", "Okay", "Hi", "Good to see you", "Greetings"]
RPSTerms = ["rock", "paper", "scissor", "r", "p", "s", "rocks", "papers", "scissors"]
userid = random.randint(1, 999999)

RTOWins = 0
RPSWins = 0

def InputSummator():
  Integer = input()
  if str.lower(Integer) in ExitTerms:
    return
  try:
    Integer = int(Integer)
    Sum = abs(1 + Integer) * (Integer/2)
    print("Computing...")
    time.sleep(1)
    print(f"""
  Your sum is: {Sum}
  """)
  except:
    InputSummator()
  
def InputFarToCel():
  constant = 5/9
  Temp = input()
  if str.lower(Temp) in ExitTerms:
    return
  try:
    Temp = float(Temp)
    NewTemp = (Temp - 32) * constant
    print("Computing...")
    time.sleep(1)
    print(f"""
  {Temp}° Fahrenheit is {NewTemp}° Celsius.
  """)
  except:
    InputFarToCel()
  
def InputCelToFar():
  constant = 9/5
  Temp = input()
  if str.lower(Temp) in ExitTerms:
    return
  try:
    Temp = float(Temp)
    NewTemp = Temp * constant + 32
    print("Computing...")
    time.sleep(1)
    print(f"""
  {Temp}° Celsius is {NewTemp}° Fahrenheit.
  """)
  except:
    InputCelToFar()
  
def RandomToOne():
  Guess = input("Predicted Repetitions: ")
  if str.lower(Guess) in ExitTerms:
    return
  try:
    Guess = int(Guess)
  except:
    RandomToOne()
    
  global RTOWins
  numberval = 0
  repetitions = 0
  while numberval <= 1:
    print("Computing...")
    time.sleep(1)
    addednum = random.random()
    print(f"""
  Old number: {numberval}
  Added Number: {addednum}
  Current Number: {numberval + addednum}
  Repetitions: {repetitions + 1} / {Guess}
    """)
    numberval += addednum
    repetitions += 1
  if Guess == repetitions:
    print(f"""
  You correctly guessed {repetitions} repetitions and won!
    """)
    RTOWins += 1
    if RTOWins == 1:
      print(f"""
  You now have {RTOWins} 'Random To One' win.
    """)
    else:
      print(f"""
  You now have {RTOWins} 'Random To One' wins.
    """)
  else:
    print(f"""
  Unfortunately, you lost! 
  Predicted Repetitions: {Guess}
  Actual Repetitions: {repetitions}
    """)
    
def RandomTen():
  number = random.randint(1, 10)
  print(f"Your random number from 1-10 is {number}!")
 
def RandomNumberGenerator():
  lbset = False
  ubset = False
  
  while lbset == False:
    lowerbound = input("Lower bound: ")
    if str.lower(lowerbound) in ExitTerms:
      return
    try:
      lowerbound = int(lowerbound)
      lbset = True
    except:
      continue
  
  while ubset == False:
    upperbound = input("Upper bound: ")
    if str.lower(upperbound) in ExitTerms:
      return
    try:
      upperbound = int(upperbound)
      ubset = True
    except:
      continue
    
    print("Computing...")
    time.sleep(1)
    
    try:
      randomnum = random.randint(lowerbound, upperbound)
      print(f"""
  Upper bound: {upperbound}
  Lower bound: {lowerbound}
  Random Number: {randomnum}
    """)
    except:
      print(f"Invalid bounds!")
      RandomNumberGenerator()
      
def RockPaperScissors():
  Move = str.lower(input("Your move: "))
  ComputerMove = random.randint(1, 3)
  global RPSWins
  if Move in ExitTerms:
    return
  elif Move in RPSTerms:
    print("Computing...")
    time.sleep(1)
    if Move == "r" or Move == "rock" or Move == "rocks":
      if ComputerMove == 1:
        print("""
  Your move: Rock
  Computer's move: Rock
  Result: You Tied.
        """)
        RockPaperScissors()
      elif ComputerMove == 2:
        print("""
  Your move: Rock
  Computer's move: Paper
  Result: You Lost!
        """)
      elif ComputerMove == 3:
        print("""
  Your move: Rock
  Computer's move: Scissors
  Result: You Won!
        """)
        RPSWins += 1
        if RPSWins == 1:
          print(f"""
  Congratulations! You now have {RPSWins} 'Rock Paper Scissors' Win!
  """)
        else:
          print(f""""
  Congratulations! You now have {RPSWins} 'Rock Paper Scissors' Wins!
  """)
    elif Move == "p" or Move == "paper" or Move == "scissors":
      if ComputerMove == 1:
        print("""
  Your move: Paper
  Computer's move: Rock
  Result: You Won!
        """)
        RPSWins += 1
        if RPSWins == 1:
          print(f"""
  Congratulations! You now have {RPSWins} 'Rock Paper Scissors' Win!
  """)
        else:
          print(f"""
  Congratulations! You now have {RPSWins} 'Rock Paper Scissors' Wins!
  """)
      elif ComputerMove == 2:
        print("""
  Your move: Paper
  Computer's move: Paper
  Result: You Tied.
        """)
        RockPaperScissors()
      elif ComputerMove == 3:
        print("""
  Your move: Paper
  Computer's move: Scissors
  Result: You Lost!
        """)
    elif Move == "s" or Move == "scissor" or Move == "scissors":
      if ComputerMove == 1:
        print("""
  Your move: Scissors
  Computer's move: Rock
  Result: You Lost!
        """)
      elif ComputerMove == 2:
        print("""
  Your move: Scissors
  Computer's move: Paper
  Result: You Won!
        """)
        RPSWins += 1
        if RPSWins == 1:
          print(f"""
  Congratulations! You now have {RPSWins} 'Rock Paper Scissors' Win!
  """)
        else:
          print(f"""
  Congratulations! You now have {RPSWins} 'Rock Paper Scissors' Wins!
  """)
      elif ComputerMove == 3:
        print("""
  Your move: Scissors
  Computer's move: Scissors
  Result: You Tied.
        """)
        RockPaperScissors()
  else:
    RockPaperScissors()
      
  
def HexidecimalConverter():
  Integer = input("Your number: ")
  if str.lower(Integer) in ExitTerms:
    return
  try:
    Hex = hex(int(Integer))
    print("Computing...")
    time.sleep(1)
    print(f"""
  Hexadecimal conversion: {Hex}
  """)
  except:
    HexidecimalConverter()
      
def ManualHexaConverter():
  HexCode = "0123456789ABCDEF"
  HexDecode = ""
  Integer = input("Your number: ")
  if str.lower(Integer) in ExitTerms:
    return
  try:
    Integer = int(Integer)
    if Integer == 0:
      HexDecode = "0"
    else:
      while Integer > 0:
        Integer, remainder = divmod(Integer, 16)
        HexDecode += HexCode[remainder]
    HexDecode = HexDecode[::-1]
    print(f"""
  Hexadecimal conversion: 0x{HexDecode}
  """)
  except:
    ManualHexaConverter()

def UniqueWPSCalculator():
  Sentence = str.lower(input())
  UniqueWordTable = []
  UniqueWords = 0
  try:
    print("Computing...")
    time.sleep(1)
    for word in Sentence.split():
      if word in UniqueWordTable:
        continue
      else:
        UniqueWordTable.append(word)
        UniqueWords += 1
    if len(UniqueWordTable) == 1:
      print(f""""
  Your sentence only has {UniqueWords} unique word!
  """)
    else:
      print(f"""
  Your sentence  has {UniqueWords} unique words!
  """)
  except:
    print("Error occurred. Type new sentence.")
    UniqueWPSCalculator()
     
  
def BinaryToDecimal():
  Binary = input("Binary Integer: ")
  if str.lower(Binary) in ExitTerms:
    return
  try:
    Decimal = int(Binary, 2)
    print("Computing...")
    time.sleep(1)
    print(f"""
  Binary Integer: {Binary}
  Decimal Integer: {Decimal}
  """)
  except:
    print("Error occurred. Enter valid binary integer.")
    BinaryToDecimal()

def DecimalToBinary():
  Decimal = input("Decimal Integer: ")
  if str.lower(Decimal) in ExitTerms:
    return
  try:
    Decimal = int(Decimal)
    Binary = bin(Decimal)
    print("Computing...")
    time.sleep(1)
    print(f"""
  Decimal Integer: {Decimal}
  Binary Integer: {Binary}
  """)
  except:
    BinaryToDecimal() 

print(f"""
Hello Player {userid}!
What should I call you?
""")

PlayerName = input("My name is ")

while True:
  greetnum = random.randint(0, int(len(GreetingTerms)) - 1)
  Greeting = GreetingTerms[greetnum]
  print(f"""
{Greeting} {PlayerName}, which application would you like to use?

'ISF' - Integer Summation Function
'UWC' - Unique Words Per Sentence Calculator
'CTF' - Celsius to Fahrenheit Converter
'FTC' - Fahrenheit to Celsius Converter
'HEX' - Hexadecimal Converter
'BTD' - Binary to Decimal Converter
'DTB' - Decimal to Binary Converter
'R10' - Random Number (1-10) Generator
'RNG' - Random Number (#-#) Generator
'RTO' - Random To One Game
'RPS' - Rock Paper Scissors Game
  """)
  
  while True:
    DesiredFunction = str.lower(input())
    DesiredFunction = DesiredFunction.replace(" ", "")
    if DesiredFunction == "intsum" or DesiredFunction == "integersummation" or DesiredFunction == "integersummationfunction" or DesiredFunction == "isf":
      print("""
You've selected the 'Integer Summation function'
For what integer do you want the sum of it's consecutive integers? (Type # or Back)
       """)
      InputSummator()
      time.sleep(1)
      break
    elif DesiredFunction == "ctf" or DesiredFunction == "celsiustofahrenheit" or DesiredFunction == "celsiustofahrenheitconverter":
      print("""
You've selected the 'Celsius to Fahrenheit converter'.
Type # or 'Back'
      """)
      InputCelToFar()
      time.sleep(1)
      break
    elif DesiredFunction == "ftc" or DesiredFunction == "fahrenheittocelsius" or DesiredFunction == "fahrenheittocelsiusconverter":
      print("""
You've selected the 'Fahrenheit to Celsius converter'.
Type # or 'Back'
      """)
      InputFarToCel()
      time.sleep(1)
      break
    elif DesiredFunction == "rto" or DesiredFunction == "randomtoone" or DesiredFunction == "rt1" or DesiredFunction == "randomto1":
      print("""
You've selected the 'Random To One game'.
The goal of the game is to guess how many repetition cycles it will take until the number exceeds one.
Type # or 'Back'
      """)
      RandomToOne()
      time.sleep(1)
      break
    elif DesiredFunction == "r10" or DesiredFunction == "randomten":
      print("You've selected the 'Random Number (1-10) Generator'.")
      RandomTen()
      time.sleep(1)
      break
    elif DesiredFunction == "rng" or DesiredFunction == "randomnumber" or DesiredFunction == "randomnumbergenerator":
      print("""
You've selected the 'Random Number Generator'.
Type # or 'Back'
      """)
      RandomNumberGenerator()
    elif DesiredFunction == "rps" or DesiredFunction == "rockpaperscissors" or DesiredFunction == "roshambo" or DesiredFunction == "rockpaperscissor":
      print("""
You've selected the 'Rock Paper Scissors game'.
Enter move or 'Back'
      """)
      RockPaperScissors()
      time.sleep(1)
      break
    elif DesiredFunction == "hex" or DesiredFunction == "hexadecimal" or DesiredFunction == "hexconverter" or DesiredFunction == "hexadecimalconverter" or DesiredFunction == "hxc":
      print("""
You've selected the 'Hexadecimal converter'.
Enter # or 'Back'
      """)
      ManualHexaConverter()
      time.sleep(1)
      break
    elif DesiredFunction == "uwc" or DesiredFunction == "uwpsc" or DesiredFunction == "uwps" or DesiredFunction == "uniquewords" or DesiredFunction == "uniquewordscalculator" or DesiredFunction == "uniquewordspersentence" or DesiredFunction == "uniquewordspersentencecalculator":
      print("""
You've selected the 'Unique Words calculator'.
Type your sentence
      """)
      UniqueWPSCalculator()
      time.sleep(1)
      break
    elif DesiredFunction == "btd" or DesiredFunction == "binaryconverter" or DesiredFunction == "bc" or DesiredFunction == "binarytodecimal" or DesiredFunction == "binarytodecimalconverter" or DesiredFunction == "btdc":
      print("""
You've selected the 'Binary to Decimal converter'.
Enter integer or 'Back'
      """)
      BinaryToDecimal()
      time.sleep(1)
      break
    elif DesiredFunction == "dtb" or DesiredFunction == "decimalconverter" or DesiredFunction == "dc" or DesiredFunction == "decimaltobinary" or DesiredFunction == "decimaltobinaryconverter" or DesiredFunction == "dtbc":
      print("""
You've selected the 'Decimal to Binary converter'.
Enter # or 'Back'
      """)
      DecimalToBinary()
      time.sleep(1)
      break
    else:
      continue

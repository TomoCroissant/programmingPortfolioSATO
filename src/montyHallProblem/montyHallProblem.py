#Tomo Sato | Feb 16 2023 | Monty Hall Problem
import random

#main playing loop
playingGame = True
#loops to receive input again if user input is invalid. When the user's input is valid, breaks loop and continues with game. When invalid, loops back to receiving an input. Outside each loop it is set back to true so it can enter the loop in next game.
inFirstGuessLoop = True
inNewGuessLoop = True
inPlayAgainLoop = True

#Counters for statistics
playCount = 0
totalWinCount = 0
doorFrequency = [0, 0, 0]
switchCount = 0
switchWin = 0
switchLoss = 0
stayCount = 0
stayWin = 0
stayLoss = 0

#statistics function
def stats():
  print("\nYour Statistics:")
  #print("You have played", playCount, "games")
  print("Door relative frequency (door1:door2:door3):", str(doorFrequency[0]) + ":" + str(doorFrequency[1]) + ":" + str(doorFrequency[2]))

  if(totalWinCount == 0): #can't divide by 0 for percent
    print("You have won", str(totalWinCount) + "/" + str(playCount), "games")
  else:
    print("You have won", str(totalWinCount) + "/" + str(playCount), "games", "(" + str(round((totalWinCount/playCount)*100, 1)) + "%)")
  
  print("You have switched your guess", str(switchCount), "times")
  if(switchWin == 0): #can't divide by 0 for percent
    print("Switch-win to switch-loss ratio", str(switchWin) + ":" + str(switchLoss))
  else:
    print("Switch-win to switch-loss ratio", str(switchWin) + ":" + str(switchLoss), "(" + str(round((switchWin/switchCount)*100, 1)) + "% win)")
    
  print("You have kept your guess", str(stayCount), "times")
  if(stayWin == 0): #can't divide by 0 for percent
    print("Stay-win to stay-loss ratio", str(stayWin) + ":" + str(stayLoss))
  else:
    print("Stay-win to stay-loss ratio", str(stayWin) + ":" + str(stayLoss), "(" + str(round((stayWin/stayCount)*100, 1)) + "% win)")

#explain stats function
def explainStats():
  print("\n'Door relative frequency' is how often each randomly-selected door contained the car.")
  print("'Switch-win to switch-loss ratio' is how often you won after changing your original guess compared to how often you lost after changing your original guess.")
  print("'Stay-win to stay-loss ratio' is how often you won after keeping your original guess compared to how often you lost after keeping your original guess.")
  print("(all percents are rounded to the first decimal)")

#intructions function:
def instructions():
  print("Welcome to the Monty Hall Problem!\nYou are the contestant of a game show!\nThere are 3 doors; 2 contain goats and 1 contains a car.\nYour goal is to win the car by guessing the correct door.\nYou will begin by guessing a door.\nI will then reveal to you one of the incorrect doors and you will have the option to guess again.")

instructions()
  
#playing game:  
while playingGame == True:
  #randomize doors and update counters based on random door
  door1 = False
  door2 = False
  door3 = False
  randomDoor = random.randint(0, 2)
  if(randomDoor == 0):
    door1 = True
    answer = 1
    doorFrequency[0] += 1
  elif(randomDoor == 1):
    door2 = True
    answer = 2
    doorFrequency[1] += 1
  elif(randomDoor == 2):
    door3 = True
    answer = 3
    doorFrequency[2] += 1

  
  while (inFirstGuessLoop == True):
    #take in first guess
    guess = str(input("\nStart by guessing a door (input 1, 2, or 3):\n1:🚪 2:🚪 3:🚪\n"))

    #reveals a door that is not the door that the player selected. Checks if valid input
    if(guess != "1" and guess != "2" and guess != "3"): #invalid inputs
      print("invalid input")
    else: #valid input
      inFirstGuessLoop = False #breaks loop
      print("\nFirst reveal:")
      if(guess == "1"):
        if(door2 == False):
          print("1:🚪 2:🐐 3:🚪")
        elif(door3 == False):
          print("1:🚪 2:🚪 3:🐐")
      elif(guess == "2"):
        if(door1 == False):
          print("1:🐐 2:🚪 3:🚪")
        elif(door3 == False):
          print("1:🚪 2:🚪 3:🐐")
      elif(guess == "3"):
        if(door1 == False):
          print("1:🐐 2:🚪 3:🚪")
        elif(door2 == False):
          print("1:🚪 2:🐐 3:🚪")

  inFirstGuessLoop = True

  
  while(inNewGuessLoop == True):
    #take in new guess  
    newGuess = str(input("Please enter your new guess (it could be the same):\n"))
  
    #reveals correct answers and checks if valid input
    if(newGuess != "1" and newGuess != "2" and newGuess != "3"): #invalid inputs
      print("invalid input")
    else: #valid input
      inNewGuessLoop = False #breaks loop
      print() #new line
      if(answer == 1): #reveals answer
        print("1:🚗 2:🐐 3:🐐")
      elif(answer == 2):
        print("1:🐐 2:🚗 3:🐐")
      elif(answer == 3):
        print("1:🐐 2:🐐 3:🚗")
        
  inNewGuessLoop = True

    
  #determines if guess was correct or not, and updates counters based on whether or not a switch occurred
  if(newGuess == str(answer)):
    print("Congratulations! You won!\nDoor " + newGuess, "was correct!")
    totalWinCount += 1
    if(guess != newGuess): #switch stats
      switchWin += 1
      switchCount += 1
    elif(guess == newGuess): #stay stats
      stayWin += 1
      stayCount += 1
  else:
    print("Unfortunately door", newGuess, "was incorrect.\nThe correct answer was door", str(answer) + ".")
    if(guess != newGuess): #switch stats
      switchLoss += 1
      switchCount += 1
    elif(guess == newGuess): #stay stats
      stayLoss += 1
      stayCount += 1

  #updates other counters
  playCount += 1


  #does user want to play again/view stats? Also checks if valid input
  while(inPlayAgainLoop == True):
    print("\nYou have played", str(playCount), "games.")
    playAgain = str(input("Would you like to play again?\nPress y to play again\nPress s to view stats\nPress e to exit and view stats\nPress r to review game rules\nPress ? for explanation of stats\n"))
    playAgain = playAgain.lower()
    if(playAgain == "y"): #play again
      print()
      inPlayAgainLoop = False
    elif(playAgain == "s"): #view stats
      stats()
    elif(playAgain == "e"): #exit
      print("Thanks for playing")
      playingGame = False
      inPlayAgainLoop = False
    elif(playAgain == "r"): #review game rules
      print()
      instructions()
    elif(playAgain == "?"): #explain stats
      explainStats()
    else: #invalid input + receive input again by not breaking loop
      print("invalid input")
      
  inPlayAgainLoop = True

#statistics when done
stats()
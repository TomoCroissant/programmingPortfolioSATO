# Tomo Sato | Mar 24 2023 | Dice Roller
# Makes a histogram of dice rolls
import matplotlib.pyplot as plt
import random


#rollDice rolls x dice and sums up all the dice
def rollDice(x):
  total = 0
  for i in range(x):
    result = random.randint(1, 6)
    total += result
  
  return total

#takes in inputs
diceNum = input("How many dice should be rolled each round? ")
roundNum = input("How many rounds should there be? ")

recordNum = [None] * int(roundNum) #one list item for every round

#rolls dice and puts results in recordNum list
i = 0
while(i < int(roundNum)):
  recordNum[i] = rollDice(int(diceNum))
  i += 1


#creates histogram
plt.hist(recordNum, bins=range(int(diceNum)*6 + 2))
plt.title("Distribution of dice sums")
plt.ylabel("Frequency (sample size: " + roundNum + ")")
plt.xlabel("Sum of " + str(diceNum) + " dice")
plt.show()

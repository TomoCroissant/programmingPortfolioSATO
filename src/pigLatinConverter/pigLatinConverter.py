#Tomo Sato | Feb 22 2023 | Pig Latin Converter
playing = True

#function which translates word into Pig Latin
def translateToPig(word):
  word = word.lower()
  firstLetter = word[0]
  otherLetters = word[1:]
  pigLatin = otherLetters + firstLetter
  if(word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u"):
    pigLatin += "way"
  else:
    pigLatin += "ay"
  return pigLatin

#loop to continue taking inputs
while playing == True:
  x = str(input("Enter a word to be translated into Pig Latin or ! to quit: "))
  if(x == "!"): #if !, break loop
    playing = False
  else: #otherwise use translateToPig function
    print(translateToPig(x))
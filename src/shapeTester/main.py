from Box import Box
from Sphere import Sphere
from Pyramid import Pyramid


b1 = Box()
s1 = Sphere()
p1 = Pyramid()
isFinished = False

while isFinished == False:
  shapeChoice = input("Pick a shape (1 for Box, 2 for Sphere, 3 for Pyramid, and 4 to finish): ")
  if (shapeChoice == "1"): #box
    b1.l = input("enter value for box length ")
    print(b1.l)
    b1.w = input("enter value for box width ")
    print(b1.w)
    b1.h = input("enter value for box height ")
    print(b1.h)
    
    print("Box Volume:", b1.calcVol())
    print("Box Surface Area:", b1.calcSA())
    
  elif (shapeChoice == "2"): #sphere
    s1.r = input("enter a value for sphere radius: ")
    print(s1.r)
    
    print("Sphere Volume:", s1.calcVol())
    print("Sphere Surface Area:", s1.calcSA())
    
  elif(shapeChoice == "3"): #pyramid
    p1.l = input("enter a value for pyramid base length ")
    print(p1.l)
    p1.w = input("enter a value for pyramid base width ")
    print(p1.w)
    p1.h = input("enter a value for pyramid height ")
    print(p1.h)

    print("Pyramid height:", p1.calcVol())
    print("Pyramid Surface Area:", p1.calcSA())
    
  elif(shapeChoice == "4"):
    isFinished = True
    
  print()
  
print("Have a good day")
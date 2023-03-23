#Convolution algorithm | Mar 6 2023 | Tomo Sato

#original data. Each line of input.txt affects each array item so you can change the input data before convolution for different results (max of 25)
inputDataFile = open("input.txt", "r")
inData = inputDataFile.readlines()
oData = [
  float(inData[0]),
  float(inData[1]),
  float(inData[2]),
  float(inData[3]),
  float(inData[4]),
  float(inData[5]),
  float(inData[6]),
  float(inData[7]),
  float(inData[8]),
  float(inData[9]),
  float(inData[10]),
  float(inData[11]),
  float(inData[12]),
  float(inData[13]),
  float(inData[14]),
  float(inData[15]),
  float(inData[16]),
  float(inData[17]),
  float(inData[18]),
  float(inData[19]),
  float(inData[20]),
  float(inData[21]),
  float(inData[22]),
  float(inData[23]),
  float(inData[24])]
inputDataFile.close()

#sliding window, the value the data points are multiplied by as the slider moves across (the sum of all values in the slider must be below or equal to one).
#Example value sets: [0.1, 0.2, 0.4, 0.2, 0.1], [0.2, 0.2, 0.2, 0.2, 0.2], [0.1, 0.1, 0.2, 0.2, 0.4]
slider = [0.1, 0.2, 0.4, 0.2, 0.1]

#array for new data after convolution
nData = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

#arrays for storing graph values as strings
oDataGraph = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
nDataGraph = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
sliderShape = [None, None, None, None, None]


#convolution algorithm
i = 0
runCon = True
while (runCon == True):
  if (i == 0): #first data point
    nData[0] = oData[0] * slider[4]
  elif (i == 1): #second data point
    nData[1] = (oData[0] * slider[3]) + (oData[1] * slider[4])
  elif (i == 2): #third data point
    nData[2] = (oData[0] * slider[2]) + (oData[1] * slider[3]) + (oData[2] * slider[4])
  elif (i == 3): #fourth data point
    nData[3] = (oData[0] * slider[1]) + (oData[1] * slider[2]) + (oData[2] * slider[3])  + (oData[3] * slider[4])
  elif (i == len(oData)-2): #second to last data point
    nData[i] = (oData[i-2] * slider[0]) + (oData[i-1] * slider[1]) + (oData[i] * slider[2]) + (oData[i+1] * slider[3])
  elif (i == len(oData)-1): #last data point
    nData[i] = (oData[i-2] * slider[0]) + (oData[i-1] * slider[1]) + (oData[i] * slider[2])
  else: #all other data points
    nData[i] = (oData[i-2] * slider[0]) + (oData[i-1] * slider[1]) + (oData[i] * slider[2]) + (oData[i+1] * slider[3]) + (oData[i+2] * slider[4])

  nData[i] = round(nData[i], 2) #data rounded to hundredth
  print(oData[i], "->",nData[i]) #prints what each value turned into
  
  i += 1 #increase array item that is accessed
  if (i >= len(oData)): #stop when end of array reached
    runCon = False


#converts numbers to strings function
def numToString(x):
  if(x == None):
    graphing == False
  elif(round(x, 1) == 0.0):
    return "0          "
  elif(round(x, 1) == 0.1):
    return "00         "
  elif(round(x, 1) == 0.2):
    return "000        "
  elif(round(x, 1) == 0.3):
    return "0000       "
  elif(round(x, 1) == 0.4):
    return "00000      "
  elif(round(x, 1) == 0.5):
    return "000000     "
  elif(round(x, 1) == 0.6):
    return "0000000    "
  elif(round(x, 1) == 0.7):
    return "00000000   "
  elif(round(x, 1) == 0.8):
    return "000000000  "
  elif(round(x, 1) == 0.9):
    return "0000000000 "
  elif(round(x, 1) == 1.0):
    return "00000000000"

#uses numToString function
graphing = True
g=0
while (graphing == True):
  #assigns graph values for original data
  oDataGraph[g] = numToString(oData[g])
  #assigns graph values for new data
  nDataGraph[g] = numToString(nData[g])
  #assigns graph values for slider shape
  if(g <= len(slider) - 1):
    sliderShape[g] = numToString(slider[g])

  g += 1  
  if(g >= len(oData) or g >= len(nData)):
    graphing = False


#draws slider shape to console and results.txt
d = 0
drawing = True
result = open("results.txt", "a")
result.write("Slider:")
print("\nSlider:")
while (drawing == True):
  print(sliderShape[d])
  result.write("\n" + sliderShape[d])
  d += 1
  if(d >= len(sliderShape)):
    drawing = False

#resets for second graph
drawing = True
d = 0

#draws graphs of original data -> Data after convolution to console and results.txt
result.write("\n\nOriginal Data:       Data after convolution:")
print("\nOriginal Data:       Data after convolution:")
while (drawing == True):
  print(oDataGraph[d], "   ->   ", nDataGraph[d])
  result.write("\n" + oDataGraph[d])
  result.write("    ->    " + nDataGraph[d])
  
  d += 1
  if(d >= len(oDataGraph) or d >= len(nDataGraph)):
    drawing = False


result.write("\n\n\n")
result.close()

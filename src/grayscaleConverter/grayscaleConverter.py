#Grayscale Converter | May 3 2023 | Tomo Sato
import matplotlib.pyplot as plt
import matplotlib.image as img

inputImg = img.imread(str(input("Name of image file: ")))

def toGray(img):
  #seperate color channels
  r = img[:, :, 0] #red
  g = img[:, :, 1] #green
  b = img[:, :, 2] #blue

  #weighted method to convert three color channels into one gray scale channel
  gray = 0.299*r + 0.587*g + 0.114*b

  return gray


#uses to Gray to convert image to grayscale
grayImg = toGray(inputImg)


#creates figure
fig = plt.figure(figsize = (6, 3)) #dimensions of figure

#1 row, 2 columns, spot 1  original
fig.add_subplot(1, 2, 1)
plt.title("original")
plt.imshow(inputImg)

#1 row, 2 columns, spot 2  grayscale
fig.add_subplot(1, 2, 2)
plt.title("grayscale")
plt.imshow(grayImg, cmap = "gray")

plt.show()

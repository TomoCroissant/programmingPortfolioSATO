import math
class Pyramid:
  l = 0.0
  w = 0.0
  h = 0.0

  def __init__(self):
    self.l = 0.0
    self.w = 0.0
    self.h = 0.0

  def calcVol(self):
    volume = (float(self.l) * float(self.w) * float(self.h)) / 3
    return volume

  def calcSA(self):
    surfaceArea = (float(self.l) * float(self.w)) + (float(self.l) * math.sqrt((float(self.w) / 2)**2 + (float(self.h)**2))) + (float(self.w) * math.sqrt((float(self.l) / 2)**2 + (float(self.h)**2)))
    return surfaceArea
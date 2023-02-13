class Box:
  l = 0.0
  w = 0.0
  h = 0.0

  def __init__(self):
    self.l = 0.0
    self.w = 0.0
    self.h = 0.0

  def calcVol(self):
    volume = float(self.l) * float(self.w) * float(self.h)
    return volume

  def calcSA(self): #surface area
    surfaceArea = (2 * float(self.l) * float(self.w)) + (2 * float(self.w) * float(self.h)) + (2 * float(self.l) * float(self.h))
    return surfaceArea
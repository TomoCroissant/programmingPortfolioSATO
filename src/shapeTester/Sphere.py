import math
class Sphere:
  r = 0.0

  def __init__(self):
    self.r = 0.0

  def calcVol(self):
    volume = (float(self.r)**3) * (math.pi * (4/3))
    return volume

  def calcSA(self):
    surfaceArea = 4 * math.pi * (float(self.r)**2)
    return surfaceArea
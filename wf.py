class Vehicle:
    def __init__(self,max_speed,mileage):
      self.max_speed=max_speed
      self.mileage = mileage
ob = Vehicle(180,18)
print("model Max speed :", ob.max_speed)
print("model Mileage :", ob.mileage)
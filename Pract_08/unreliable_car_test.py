from Pract_08.unreliable_car import UnreliableCar

"""Tests Unreliable_Car"""
new_car = UnreliableCar("Mirage", 100, 40)
miles_to_drive = 70
new_car.drive(miles_to_drive)
print(f"{new_car.name} tried to drive {miles_to_drive} miles, but drove {new_car.odometer} miles. The car has "
      f"{new_car.fuel} gallons of fuel left")





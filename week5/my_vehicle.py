# Polymorphism Example

class Vehicle:
    def move(self):
        print("This vehicle moves...")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# List of different vehicles
vehicles = [Car(), Plane(), Boat()]

# Each vehicle "moves" in its own way
for v in vehicles:
    v.move()

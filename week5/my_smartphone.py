# Smartphone class with attributes and methods

class Smartphone:
    def __init__(self, brand, model, battery_life):
        # Constructor initializes unique values for each object
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")
    
    def battery_status(self):
        print(f"{self.brand} {self.model} has {self.battery_life} hours of battery left.")


# Inheritance: GamingPhone is a child class of Smartphone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        # Call the parent constructor
        super().__init__(brand, model, battery_life)
        self.cooling_system = cooling_system
    
    # Extra method specific to GamingPhone
    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.brand} {self.model} with {self.cooling_system} cooling system!")


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S24", 20)
phone2 = GamingPhone("Asus", "ROG Phone 7", 15, "liquid cooling")

# Use methods
phone1.call("0501234567")
phone1.battery_status()

phone2.call("0249876543")
phone2.play_game("PUBG Mobile")
phone2.battery_status()

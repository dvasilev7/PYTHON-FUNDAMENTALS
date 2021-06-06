class Vehicle:
    owner = None

    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price

    def buy(self, money, owner):
        if money < self.price:
            return "Sorry, not enough money"
        elif Vehicle.owner:
            return "Car already sold"
        else:
            Vehicle.owner = owner
            return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"

    def sell(self):
        if Vehicle.owner:
            Vehicle.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if Vehicle.owner is None:
            return f"{self.model} {self.type} is on sale: {self.price}"
        else:
            return f"{self.model} {self.type} is owned by: {Vehicle.owner}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
vehicle.buy(29000, "Maikati")
vehicle.buy(40000, "Putani")
print(vehicle)

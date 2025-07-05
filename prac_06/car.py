class Car:
    def __init__(self, fuel=0, name="Car"):
        self.fuel = fuel
        self.odometer = 0
        self.name = name

    def add(self, amount):
        self.fuel += amount

    def drive(self, distance):
        if distance <= self.fuel:
            self.fuel -= distance
            self.odometer += distance
        else:
            self.odometer += self.fuel
            self.fuel = 0

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"
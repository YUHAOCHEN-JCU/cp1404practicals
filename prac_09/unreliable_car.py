from car import Car
import random

class UnreliableCar(Car):
    """A subclass of Car that simulates an unreliable car, which may not always drive
    even when requested, based on a reliability percentage."""
    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if it passes the reliability check."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0

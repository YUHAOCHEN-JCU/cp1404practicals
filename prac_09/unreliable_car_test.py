"""
car = UnreliableCar(name: "Unreliable Car", fuel: 100, reliability: 30)
total_distance = 0
repeat i from 0 to 99
    distance_driven = car drive 10km
    total_distance = total_distance + distance_driven
display i + 1, total_distance
"""
from unreliable_car import UnreliableCar

car = UnreliableCar(name="Unreliable Car", fuel=100, reliability=30)
total_distance = 0
for i in range(100):
    distance_driven = car.drive(10)
    total_distance += distance_driven
    print(f"Total distance traveled number {i + 1} attempts: {total_distance}km")
print(f"Total distance traveled after 100 attempts: {total_distance}km")


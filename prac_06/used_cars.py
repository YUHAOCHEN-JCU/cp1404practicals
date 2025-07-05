from car import Car

# 1. Create a new Car object called "limo" with 100 units of fuel
limo = Car(100, "limo")

# 2. Add 20 more units of fuel using the add method
limo.add(20)

# 3. Print the amount of fuel in the car
print(limo.fuel)

# 4. Attempt to drive the car 115 km using the drive method
limo.drive(115)

# 7. Print the car object to test the __str__ method
print(limo)
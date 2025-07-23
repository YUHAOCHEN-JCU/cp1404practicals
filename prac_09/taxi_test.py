"""
my_taxi = Taxi(name: "Prius 1", fuel: 100)
my_taxi drive 40 kilometers
display my_taxi and current fare
restart the meter
my_taxi drive 100 kilometers
display my_taxi and current fare
"""
from taxi import Taxi

# Create a Taxi object
my_taxi = Taxi("Prius 1", 100)

# Drive 40 kilometers
my_taxi.drive(40)

# Print taxi details and current fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")

# Restart the meter and drive 100 kilometers.
my_taxi.start_fare()
my_taxi.drive(100)

# Reprint the details and current costs
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")
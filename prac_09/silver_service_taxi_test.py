"""
display "SilverServiceTaxi Test"
taxi = SilverServiceTaxi(name: "Hummer", fuel=200, fanciness=2)
taxi.start_fare()
taxi.drive(18)
fare = taxi.get_fare()
display taxi
display "Expected fare: $48.78"
display fare
"""
from silver_service_taxi import SilverServiceTaxi

print("SilverServiceTaxi Test")
taxi = SilverServiceTaxi("Hummer", fuel=200, fanciness=2)
taxi.start_fare()
taxi.drive(18)
fare = taxi.get_fare()
print(taxi)
print("Expected fare: $48.78")
print(f"Calculated fare: ${fare}")





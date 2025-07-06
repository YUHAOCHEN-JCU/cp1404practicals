from guitar import Guitar

# Create Guitar instances for testing
gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 1000.00)

# Test get_age method
print(f"Gibson L-5 CES get_age() - Expected 100. Got {gibson.get_age()}")
print(f"Another Guitar get_age() - Expected 9. Got {another_guitar.get_age()}")

# Test is_vintage method
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"Another Guitar is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

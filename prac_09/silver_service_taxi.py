from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50  

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with name, fuel, and fanciness level."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Calculate the total fare including flagfall, without rounding."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation with flagfall included."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

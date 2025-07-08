class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise init instance.
                name: name of guitar
                year: year of guitar
                cost: cost of guitar
                """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string information"""
        return f"{self.name} ({self.year}): ${self.cost:.2f}"

    def get_age(self):
        """Get guitar's age"""
        return 2022 - self.year

    def is_vintage(self):
        """Add function to judge is vintage"""
        return self.get_age() >= 50

    def __lt__(self, other):
        return self.year < other.year
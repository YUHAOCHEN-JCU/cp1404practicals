"""
Estimated time: 25 minutes
Actual time: [To be filled after completion]
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance.
                name, typing, reflection, year
                """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Add is_dynamic function to judge is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """return string information"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
class ProgrammingLanguage

    function __init__(self, name, typing, reflection, year, pointer_arithmetic)
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    function __str__(self)
        return name, typing, reflection, year, pointer arithmetic

    function --repr__(self)
        return name, typing, reflection, year, pointer arithmetic

    function is_dynamic(self)
        return typing == 'Dynamic'

function run_tests()
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, pointer_arithmetic="No")
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, pointer_arithmetic="No")
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, pointer_arithmetic="No")
    languages contain ruby, python, visual_basic
    display python
    display "The dynamically typed languages are:"
    repeat language in languages
        if language is dynamic
            display language.name
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}, Pointer Arithmetic={self.pointer_arithmetic}"

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}, Pointer Arithmetic={self.pointer_arithmetic}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, pointer_arithmetic="No")
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, pointer_arithmetic="No")
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, pointer_arithmetic="No")

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()

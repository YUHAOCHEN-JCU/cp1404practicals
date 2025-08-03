"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase_as_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a full stop.

    >>> format_phrase_as_sentence("hello")
    'Hello.'
    >>> format_phrase_as_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_phrase_as_sentence("already ended!")
    'Already ended!'
    """
    phrase = phrase.strip()
    if not phrase:
        return ''
    phrase = phrase[0].upper() + phrase[1:]
    if phrase[-1] not in '.!?':
        phrase += '.'
    return phrase


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car.odometer == 0, "Car does not set odometer correctly"

    # Test Car sets fuel correctly
    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Car does not set fuel correctly with argument"

    default_car = Car()
    assert default_car.fuel == 0, "Car does not set default fuel to 0"


run_tests()
doctest.testmod()

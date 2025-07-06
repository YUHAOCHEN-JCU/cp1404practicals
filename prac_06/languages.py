"""
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
display python

languages contains python, ruby, visual_basic

display "The dynamically typed languages are:"
repeat lang in languages
    if lang is dynamic
        print lang of name

repeat lang in languages
    display lang
"""
from programming_language import ProgrammingLanguage

# Create ProgrammingLanguage objects
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

# List of languages
languages = [python, ruby, visual_basic]

# Print dynamically typed languages
print("The dynamically typed languages are:")
for lang in languages:
    if lang.is_dynamic():
        print(lang.name)

# Test __str__ method
for lang in languages:
    print(lang)

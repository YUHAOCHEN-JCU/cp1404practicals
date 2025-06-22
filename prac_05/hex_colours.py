"""
COLOR_HEX_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}
get user_color
while user_color not equal to ""
    if user_color in COLOR_HEX_CODES
        display user_color with value
    else
        display error message
    get user_color
display "Thank you!"
"""
COLOR_HEX_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}
user_color = input("Hex Code Lookup (Enter blank to quit): ").lower()
while user_color != "":
    if user_color in COLOR_HEX_CODES:
        print(f"{user_color} is {COLOR_HEX_CODES[user_color]}")
    else:
        print("Sorry, that color is not in the dictionary.")
    user_color = input("Hex Code Lookup (Enter blank to quit): ").lower()
print("Thank you!")

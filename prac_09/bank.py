"""
band contain Musician("Kevin Figueiredo"), Musician("Nuno Bettencourt"), Musician("Gary Cherone"), Musician("Pat Badger")
display "Original Band (Generic Musicians):"
repeat member in band
    display member.play()


kevin = Drummer("Kevin Figueiredo")
nuno = Guitarist("Nuno Bettencourt")
gary = Singer("Gary Cherone")
pat = Musician("Pat Badger")
band contain kevin, nuno, gary, pat
display "Extreme Band (With Roles):"
repeat member in band
    display member.play()
"""
class Musician:
    """
    A base class representing a generic musician.
    Attributes:
        name (str): The name of the musician.
    """
    def __init__(self, name):
        """
        Initialize the Musician with a name.
        Args:
            name (str): The name of the musician.
        """
        self.name = name

    def play(self):
        """
        Simulate the musician playing music.
        Returns:
            str: A string describing the musician's action.
        """
        return f"{self.name} is playing music."


class Guitarist(Musician):
    """A class representing a guitarist, derived from Musician."""
    def play(self):
        """Simulate the guitarist shredding on the guitar."""
        return f"{self.name} is shredding on the guitar!"


class Drummer(Musician):
    """A class representing a drummer, derived from Musician."""
    def play(self):
        """Simulate the drummer pounding the drums."""
        return f"{self.name} is pounding the drums!"


class Singer(Musician):
    """A class representing a singer, derived from Musician."""
    def play(self):
        """Simulate the singer singing passionately."""
        return f"{self.name} is singing passionately!"


band = [
    Musician("Kevin Figueiredo"),
    Musician("Nuno Bettencourt"),
    Musician("Gary Cherone"),
    Musician("Pat Badger")
]
print("Original Band (Generic Musicians):")
for member in band:
    print(member.play())


kevin = Drummer("Kevin Figueiredo")
nuno = Guitarist("Nuno Bettencourt")
gary = Singer("Gary Cherone")
pat = Musician("Pat Badger")
band = [kevin, nuno, gary, pat]
print("Extreme Band (With Roles):")
for member in band:
    print(member.play())

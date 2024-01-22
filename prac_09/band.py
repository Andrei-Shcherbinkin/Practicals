class Band:
    """Band class for storing details of a band."""

    def __init__(self, name=""):
        """Initialize a Band."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Simulate the band playing."""
        for musician in self.musicians:
            print(musician.play())

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.musicians})"
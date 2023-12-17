class Guitar:
    """Represent a guitar with name, year, and cost."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize the Guitar object with default values."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self, current_year):
        """Return the age of the guitar."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Return True if the guitar is more than 50 years old, otherwise return False"""
        age = self.get_age(current_year)
        return age >= 50
    def __lt__(self, other):
        """Define less than comparison based on the guitar's year."""
        return self.year < other.year


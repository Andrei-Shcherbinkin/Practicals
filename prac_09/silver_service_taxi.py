from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialized version of a Taxi with fanciness and flagfall."""

    flagfall = 4.50  # Class variable for the extra charge on each new fare

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance, based on the parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness

    def get_fare(self):
        """Return the total fare including extra charges."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Taxi but with fanciness and flagfall information."""
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"

    def drive(self, distance):
        """Drive like the parent Taxi but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance *= self.fanciness
        return distance_driven
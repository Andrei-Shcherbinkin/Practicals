import random
from car import Car  # Assuming your Car class is defined in a 'car.py' file

class UnreliableCar(Car):
    """Specialized version of a Car with reliability factor."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance, based on the parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like the parent Car, but with a reliability factor."""
        random_number = random.randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            print(f"{self.name} failed to start due to low reliability.")
            return 0  # Car did not drive
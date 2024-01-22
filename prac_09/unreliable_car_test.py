from unreliable_car import UnreliableCar

my_unreliable_car = UnreliableCar(name="UnreliableCar 1", fuel=50, reliability=70)

# Attempt to drive the unreliable car
distance_driven = my_unreliable_car.drive(30)

# Print the details and the distance driven
print(my_unreliable_car)
print(f"Distance driven: {distance_driven} km")

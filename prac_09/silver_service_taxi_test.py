from silver_service_taxi import SilverServiceTaxi

# Create a new silver service taxi object

# Test code in silver_service_taxi_test.py
my_silver_service_taxi = SilverServiceTaxi(name="Hummer", fuel=200, fanciness=2)

# Drive the silver service taxi
my_silver_service_taxi.drive(18)

# Print the details and the total fare
print(my_silver_service_taxi)
print(f"Total Fare: ${my_silver_service_taxi.get_fare():.2f}")

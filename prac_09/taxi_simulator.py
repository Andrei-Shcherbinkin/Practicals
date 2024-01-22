from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    """Display the available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def main():
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")

    while True:
        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            break
        elif choice == 'c':
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            if 0 <= taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]
                print(f"Bill to date: ${total_bill:.2f}")
            else:
                print("Invalid taxi choice")

        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                cost = current_taxi.drive(distance)
                total_bill += cost
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

if __name__ == "__main__":
    main()
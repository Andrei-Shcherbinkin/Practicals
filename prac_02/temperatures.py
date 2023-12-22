def main():
    MENU = """
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(f"Result: {celsius_to_fahrenheit(celsius):.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(f"Result: {fahrenheit_to_celsius(fahrenheit):.2f} C")
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def celsius_to_fahrenheit(celsius):
    fahrenheit_temp = celsius * 9.0 / 5 + 32
    return fahrenheit_temp

def fahrenheit_to_celsius(fahrenheit):
    celsius_temp = 5 / 9 * (fahrenheit - 32)
    return celsius_temp

main()
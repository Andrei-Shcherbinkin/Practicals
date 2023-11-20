def main():
    score = get_valid_score("Enter the valid score: ", 0, 100)
    print(score)
    MENU = """
       (G)et a valid score
       (P)rint result
       (S)how stars
       (Q)uit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Enter the valid score: ", 0, 100)
            print(score)
        elif choice == "P":
            print(f"Your result is: {describe_score(score)}")
        elif choice == "S":
            print(int(score) * "*")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")

def get_valid_score(prompt, low, high):
    number = float(input(prompt))
    while high >= number < low:
        print("Invalid input")
        number = float(input(prompt))
    return number

def describe_score(score):
    while 0 <= score <= 100:
        if score >= 90:
           return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"
    return "Invalid input!"
main()
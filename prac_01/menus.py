name = input("Enter name: ")
print(f"(H)ello \n(G)oodbye \n(Q)uit")
choice = input("Make a choice: ")
while choice != "Q":
    if choice == "H":
        print(f"Hello, {name}!")
    elif choice == "G":
        print(f"Goodbye, {name}!")
    else:
        print("Invalid choice!")
    print(f"(H)ello \n(G)oodbye \n(Q)uit")
    choice = input("Make a choice: ")
print("finished.")
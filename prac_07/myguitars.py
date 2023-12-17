from guitar import Guitar

def read_guitars_from_file(file_path):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name, year, cost = parts
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def write_guitars_to_file(file_path, guitars):
    """Write guitars to a CSV file."""
    with open(file_path, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}\n")

def get_guitar():
    """Ask the user to enter information for a new guitar."""
    name = input("Enter the name of the guitar: ")
    year = int(input("Enter the year of manufacture: "))
    cost = float(input("Enter the cost of the guitar: "))
    return Guitar(name, year, cost)

if __name__ == "__main__":
    # Read guitars from the file
    guitars_list = read_guitars_from_file('guitars.csv')

    # Display guitars in default order
    print("Guitars in default order:")
    for guitar in guitars_list:
        print(guitar)

    # Sort guitars by year (oldest to newest) using the __lt__ method
    guitars_list.sort()

    # Display guitars in sorted order
    print("\nGuitars sorted by year:")
    for guitar in guitars_list:
        print(guitar)

    # Ask the user to enter new guitars
    num_new_guitars = int(input("Enter the number of new guitars you want to add: "))
    for _ in range(num_new_guitars):
        new_guitar = get_guitar()
        guitars_list.append(new_guitar)

    # Write all guitars to the data file
    write_guitars_to_file('guitars.csv', guitars_list)

    print("\nAll guitars have been updated and written to the data file.")
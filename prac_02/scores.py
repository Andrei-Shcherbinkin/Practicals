import random
def main():
    score = float(input("Enter score: "))
    print(describe_score(score))
    random_number = random.randint(0, 100)
    print(f"{random_number} - {describe_score(random_number)}")

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
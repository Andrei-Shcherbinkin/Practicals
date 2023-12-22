def main():
    MIN_LENGTH = 8
    user_password = get_password(MIN_LENGTH)
    make_stars(user_password)


def make_stars(user_password):
    stars = len(user_password) * "*"
    print(stars)


def get_password(MIN_LENGTH):
    user_password = input("Enter your password: ")
    while len(user_password) < MIN_LENGTH:
        print("Your password must contain at least 8 characters!")
        user_password = input("Enter your password: ")
    return user_password


main()
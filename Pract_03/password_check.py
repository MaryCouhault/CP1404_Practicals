"""CP1404
Name: Mary Couhault
Date: July 30th 2021
Description: Asks user for a password and prints the equivalent length of *
"""


def main():
    password = input("What is your password?")
    pass_length = len(password)  # takes the password and gets its length
    print_asterisks(pass_length)


def print_asterisks(pass_length):
    for i in range(1, pass_length):
        print("*", end="")


main()

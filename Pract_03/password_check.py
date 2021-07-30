"""CP1404
Name: Mary Couhault
Date: July 30th 2021
Description: Asks user for a password and prints the equivalent length of *
"""


def main():
    password = input("What is your password?")
    pass_length = len(password)  # takes the password and gets its length
    length(pass_length)


def length(pass_length):
    for i in range(pass_length):
        print("*", end="")


main()

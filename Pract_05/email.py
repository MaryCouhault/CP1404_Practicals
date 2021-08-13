"""
CP1404/CP5632 Practical
User Enters email
Program Prints their name
"""


def main():
    email_capture = []
    email = input("What is your email? ")
    while email != " ":
        name = email.split()
        email_capture.append(name)
        print(name)
        return name


main()

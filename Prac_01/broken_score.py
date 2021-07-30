"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Enter a valid score!")
    elif score >= 90:
        print('Excellent')
    elif score >= 50:
        print("You passed the class!")
    else:
        print("Please try better next time!")


main()

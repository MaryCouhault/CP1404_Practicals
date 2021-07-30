"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    get_score_response(score)
    print(get_score_response(score))
    print(random.randint(get_score_response(score)))


def get_score_response(score):
    if score < 0 or score > 100:
        return "Enter a valid score!"
    elif score >= 90:
        return 'Excellent'
    elif score >= 50:
        return "You passed the class!"
    else:
        return "Please try better next time!"


main()

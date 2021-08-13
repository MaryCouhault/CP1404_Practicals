"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
from typing import Dict

CODE_TO_NAME: dict[str, str] = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                                "WA": "Western Australia",
                                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").title()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").title()

for x, y in CODE_TO_NAME.items():
    print(f"{x} is {y}")

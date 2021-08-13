"""
CP1404/CP5632 Practical
User enters color name
prints out hexcolor code
"""


def main():
    colors_to_hex: dict[str, str] = {"Violet": "#ee82ee", "Turquoise": "#40e0d0", "Thistle": "#d8bfd8",
                                     "Plum": "#dda0dd",
                                     "Pink": "#ffc0cb", "PaleVioletRed": "#db7093", "MintCream": "#f5fffa",
                                     "MediumOrchid": "#ba55d3", "LimeGreen": "#32cd32", "LightCoral": "#f08080"}

    color = input("What color would you like to pick?").title()
    while color != "":
        if color in colors_to_hex:
            print(color, "is", colors_to_hex[color])
        else:
            print("Invalid input")
        color = input("What color would you like to pick: ").title()

    for x, y in colors_to_hex.items():
        print(f"{x} is {y}")


main()

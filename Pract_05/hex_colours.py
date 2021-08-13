"""
CP1404/CP5632 Practical
User enters color name
prints out hexcolor code
"""


def main():
    colors_to_hex = {"violet": "#ee82ee", "turquoise": "#40e0d0", "thistle": "#d8bfd8",
                     "plum": "#dda0dd",
                     "pink": "#ffc0cb", "palevioletred": "#db7093", "mintcream": "#f5fffa",
                     "mediumorchid": "#ba55d3", "limegreen": "#32cd32", "lightcoral": "#f08080"}

    for m in colors_to_hex:
        print(m)
    color = input("What color would you like to pick?").lower()
    while color != " ":
        if color in colors_to_hex:
            print(color, "is", colors_to_hex[color])
        else:
            print("Invalid input")
        color = input("What color would you like to pick: ").lower()
    for x, y in colors_to_hex.items():
        print(f"{x} is {y}")


main()

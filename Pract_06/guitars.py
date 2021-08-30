from Pract_06.guitar import Guitar


def main():
    print("My Guitar Collection!!")
    guitars_list = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        add_guitar = Guitar(name, year, cost)
        guitars_list.append(add_guitar)
        print(f"{add_guitar} added.")
        name = input("Name: ")0

    print("These are my guitars in my collection:")
    for i, guitar in enumerate(guitars_list, 1):  # for loop to print list of guitars and vintage status
        vintage = ""
        if guitar.is_vintage():
            vintage = "(Vintage)"
        print(f"Guitar {i}: {guitar.name}, {guitar.year},worth: ${guitar.cost:.2f} {vintage}")


main()
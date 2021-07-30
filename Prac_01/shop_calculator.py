def shopCal():
    total = 0
    items = int(input("Number of items: "))
    while items <= 0:
        print("Invalid Input!")
        items = int(input("Number of items: "))

    for n in range (items):
        itemprice = float(input("Price of Item: "))
        total = itemprice + total

    if total >= 100:
        total = total - ( total * .10)

    print("Total Price of all your {} items is:  ${:.2f}".format(items, total))


shopCal()

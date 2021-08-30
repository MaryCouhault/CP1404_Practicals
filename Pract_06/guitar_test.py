from Pract_06.guitar import Guitar

first_guitar = Guitar("Gibson L-5 CES", 1945, 34588)
second_guitar = Guitar("Yamaha 3-f CST", 1944, 24500)

print("{} get_age() - Expected {}. Got {}".format(first_guitar.name, 66, first_guitar.get_age()))
print("{} get_age() - Expected {}. Got {}".format(second_guitar.name, 67, second_guitar.get_age()))
print('{} is_vintage() - Expected True. Got {}'.format(first_guitar.name, first_guitar.is_vintage()))
print('{} is_vintage() - Expected False. Got {}'.format(second_guitar.name, second_guitar.is_vintage()))
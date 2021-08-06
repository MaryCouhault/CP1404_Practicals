import random

LARGEST = 45
SMALLEST = 1
NUMBER_COUNT = 6


def main():
    number_gen = int(input("How many quick picks would you like to generate? "))
    for i in range(0, number_gen):
        number_list = []
        for n in range(NUMBER_COUNT):
            num_gen = random.randint(SMALLEST, LARGEST)
            while num_gen in number_list:
                num_gen = random.randint(SMALLEST, LARGEST)
            number_list.append(num_gen)
        number_list.sort()
        print(*number_list, sep='  ')


main()

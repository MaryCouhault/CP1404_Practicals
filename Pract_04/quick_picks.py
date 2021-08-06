import random

number_gen = int(input("How many quick picks would you like to generate? "))
for i in range(0, number_gen):

    for n in range(6):
        print(random.randint(1, 45), end=" ")

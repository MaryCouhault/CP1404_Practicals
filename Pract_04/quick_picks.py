import random

number_gen = int(input("How many quick picks would you like to generate? "))
for i in range (1, number_gen):
    for n in range (1,6):
        print(random.randint(1, 45))
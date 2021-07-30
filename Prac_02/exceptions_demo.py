"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0 or numerator == 0:
        print("This value is incorrect, you can not divide by 0")
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. ValueError occurs when the numerator or denominator goes into decimal places
# 2. ZeroDivisionError occurs when 0 is divided by itself
# 3. add a While loop that indicates that both numbers have to be larger than 0

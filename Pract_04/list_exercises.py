def main():
    numbers = []
    for i in range(1, 6):
        new_numbers = int(input(f"Write Number {i}: "))
        numbers.append(new_numbers)  # puts the new number into the list

    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))


main()

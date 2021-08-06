usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


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

    username = input("What is your username: ")
    if username in usernames:
        print("access granted")
    else:
        print("DENIED")

main()

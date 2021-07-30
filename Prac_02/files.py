def main():
    name_file = "names.txt"
    out_file = open("names.txt", 'w')
    user_input = input("What is your name? ")
    print("Your name is {}".format(user_input), file=out_file)
    out_file.close()

    logs = open("names.txt", 'r')
    logs_read = logs.read()
    logs.close()
    print(logs_read)

    read_file = open("numbers.txt", 'r')
    num1 = int(read_file.readline())
    num2 = int(read_file.readline())
    read_file.close()
    num3 = num1 + num2
    print(num3)


if __name__ == '__main__':
    main()

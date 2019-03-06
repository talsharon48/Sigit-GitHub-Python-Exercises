# function that gets a list of integers and sum them
def sum_list_numbers():
    sum_of_numbers = 0
    list_of_numbers = input("Please Enter Numbers Separated By Commas: ").split(',')
    for number in list_of_numbers:
        sum_of_numbers += int(number)
    print("The Sum Of The Numbers Is: ", sum_of_numbers)
    # Also Can Be Done Like: print("The Sum Of The Numbers Is: " + sum(array_of_nums))


# function that ask the user to enter numbers until "Stop"
def sum_numbers():
    sum_of_numbers = 0
    num = input("Please Enter Numbers, To Stop Enter 'Stop': ")
    while num != "Stop":
        # checking that the number is valid
        while not num.isdigit():
            num = input("Not All Chars Are Digits, Please Enter New Number: ")
        sum_of_numbers += int(num)
        num = input("Please Enter Number: ")
    print("The Sum Of The Numbers Is: ", sum_of_numbers)


# main function that call the functions above
def main():
    sum_numbers()
    sum_list_numbers()

if __name__ == '__main__':
    main()

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

if __name__ == '__main__':
    main()

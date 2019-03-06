# the function gets ID and check if it's check digit is correct
def check_digit(identity):
    sum_nums = 0
    # calculating the sum of the digits
    for i in range(len(identity) - 1):
        num = int(identity[i]) * (i % 2 + 1)
        if num > 9:
            num = num % 10 + num // 10 % 10
        sum_nums += num
    real_check_dig = 10 - sum_nums % 10
    if (10 - sum_nums % 10) == int(identity[i+1]):
        print("The ID Is Valid!!, The Check Digit Is: " + str(real_check_dig))
    else:
        print("The ID Is Invalid!!, The Real Check Digit Is: " + str(real_check_dig))


# the function ask the user to enter an ID that contains only digits
def get_id():
    identity = input("Please Enter ID: ")
    # check if the ID contains only digits
    while not identity.isdigit():
        print("One Or More Chars Aren't Digits")
        identity = input("Please Enter New ID: ")
    return identity


# main function that call the functions above
def main():
    identity = get_id()
    check_digit(identity)

if __name__ == '__main__':
    main()

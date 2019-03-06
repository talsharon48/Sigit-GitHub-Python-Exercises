DICT_OF_SECRET_MONEY = {"1234": 2000, "2345": 3000, "3456": 4000, "4567": 5000, "5678": 6000, "6789": 7000}


# Exiting the ATM
def exit_atm(secret_code):
    exit("Exited With Secret Code: " + secret_code)


# function that gets secret code and changing it
def change_secret_code(secret_code):
    new_code = input("Please Enter A 4 Digits New Code: ")
    # checking if the code is valid
    while not new_code.isdigit() or len(new_code) != 4 or new_code in DICT_OF_SECRET_MONEY.keys():
        new_code = input(
            "Not All Chars Are Digits Or The Length Isn't 4 Or Code Already Exist, Please Enter A 4 Digits New Code: ")
    # creating the new code
    DICT_OF_SECRET_MONEY[new_code] = DICT_OF_SECRET_MONEY[secret_code]
    DICT_OF_SECRET_MONEY.pop(secret_code)
    return new_code


# function the gets secret code and making withdrawal
def withdrawal(secret_code):
    dict_of_amounts = {"A": 50, "B": 20}
    op = input("To Withdrawal 50 Enter A\nTo Withdrawal 20 Enter B\nTo Withdrawal Another Amount C\n")
    # checking the validate of the option
    while not 'A' <= op <= 'C':
        print("Invalid Input")
        op = input("To Withdrawal 50 Enter A\nTo Withdrawal 20 Enter B\nTo Withdrawal Another Amount C\n")
    # making the withdrawal
    if op != "C":
        DICT_OF_SECRET_MONEY[secret_code] -= dict_of_amounts[op]
    else:
        amount = input("Please Enter The Amount: ")
        while not amount.isdigit() or int(amount) < 0 or DICT_OF_SECRET_MONEY[secret_code] < int(amount):
            amount = input(
                "Not All Chars Are Digits Or Number Isn't Positive Or Not Enough Money, Please Enter New Amount: ")

        DICT_OF_SECRET_MONEY[secret_code] -= int(amount)


# printing the current balance
def print_balance(secret_code):
    print(DICT_OF_SECRET_MONEY[secret_code])


# function that simulates ATM
def options(secret_code):
    dict_of_operations = {"A": print_balance,
                          "B": withdrawal,
                          "C": change_secret_code,
                          "D": exit_atm}
    # checking the validate of the option
    while True:
        op = input(
            "Please Enter One Of These Options:\nA: Print Balance\nB: Withdrawal\nC: Change Secret Code\nD: Exit\n")
        while not 'A' <= op <= 'D':
            print("Invalid Input")
            op = input(
                "Please Enter One Of These Options:\nA: Print Balance\nB: Withdrawal\nC: Change Secret Code\nD: Exit\n")
        # calling the specific function that matches the option
        if op == 'C':
            secret_code = dict_of_operations[op](secret_code)
        else:
            dict_of_operations[op](secret_code)


# function that checks if the secret num is exists
def check_secret_num():
    code = input("Please Enter Secret Code: ")
    # checking if the code exists
    if code in DICT_OF_SECRET_MONEY.keys():
        return True, code
    try_again = input("Wrong Code, Do You Want To Try Again?\nEnter Yes/No\n")
    # letting the customer to try again
    while try_again == "Yes":
        code = input("Please Enter Secret Code: ")
        if code in DICT_OF_SECRET_MONEY.keys():
            return True, code
        try_again = input("Wrong Code, Do You Want To Try Again?\nEnter Yes/No\n")
    return False, code


# main function that call the functions above
def main():
    correct_secret, code = check_secret_num()
    if correct_secret:
        print("Connected Successfully")
        options(code)
    else:
        print("Bye Bye")


if __name__ == '__main__':
    main()

DICT_OF_SECRET_MONEY = {"1234": 2000, "2345": 3000, "3456": 4000, "4567": 5000, "5678": 6000, "6789": 7000}


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
    else:
        print("Bye Bye")


if __name__ == '__main__':
    main()

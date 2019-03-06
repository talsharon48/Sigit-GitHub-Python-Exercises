# printing the winner
def print_the_winner(winner):
    print("Congratulations!!! Player " + str(winner) + " Won The Game!")


# checking if given list simulates winner, if does it prints the winner
def check_list_win(row):
    winner = 0
    for i in range(len(row) - 1):
        if (row[i] != 1 and row[i] != 2) or row[i] != row[i+1]:
            return 0
        else:
            winner = row[i]
    if winner:
        print_the_winner(winner)
        return True
    return False


# the function gets game board and checking for cross win
def check_winner_crosses(game):
    list_of_main_cross = []
    list_of_secondary_cross = []
    # checking main and secondary crosses
    for index in range(len(game)):
        # main cross
        list_of_main_cross.append(game[index][index])
        # secondary cross
        list_of_secondary_cross.append((game[len(game) - index - 1][index]))
    return check_list_win(list_of_main_cross) or check_list_win(list_of_secondary_cross)


# the function gets game board and checking for column win
def check_winner_col(game):
    # checking columns
    for index in range(len(game)):
        list_to_check = []
        for row in game:
            list_to_check.append(row[index])
        if check_list_win(list_to_check):
            return True


# the function gets game board and checking for row win
def check_winner_row(game):
    # checking rows
    for row in game:
        if check_list_win(row):
            return True


# function that gets the game board and sending it to each win option functions
def check_winner(game):
    # checking rows
    if not check_winner_row(game):
        # checking columns
        if not check_winner_col(game):
            # checking crosses
            if not check_winner_crosses(game):
                print("Its A Tie!!!")


# main function that call the functions above
def main():
    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]
    check_winner(game)


if __name__ == '__main__':
    main()

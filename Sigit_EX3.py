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


# main function that call the functions above
def main():
    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]

if __name__ == '__main__':
    main()

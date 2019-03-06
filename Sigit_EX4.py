# function that gets a sting and compress it, For Example: Input: “abcaadddcc” Output: “a1b1c1a2d3c2”
def compress_string(string):
    compressed_string = ''
    counter = 1
    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            compressed_string += string[i] + str(counter)
            counter = 1
        else:
            counter += 1
    compressed_string += string[i+1] + str(counter)
    return compressed_string


# function that ask the user to enter string that contain only alpha chars and return it
def get_string():
    string = input("Please Enter String That Contains Only Alpha Chars: ")
    # check if all chars ar alphas
    while not string.isalpha():
        print("The String Must Contain Only Alpha Chars")
        string = input("Please Enter String That Contains Only Alpha Chars: ")
    return string


# main function that call the functions above
def main():
    string = get_string()
    compressed_string = compress_string(string)
    print("The Old String Was: " + string + " The New String Is: " + compressed_string)

if __name__ == '__main__':
    main()

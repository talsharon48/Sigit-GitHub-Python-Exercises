# example for function
def my_multiply(x):
    return x * 2


# function that does the same thing as map: the function gets function as parameter and apply it on each element
# of given list, and update the elements
def my_map(func_name, list_of_parameters):
    for i in range(len(list_of_parameters)):
        list_of_parameters[i] = func_name(list_of_parameters[i])
    return list_of_parameters


# main function that call the functions above
def main():
    list_of_parameters = [1, 2, 3]
    print("Before: ", list_of_parameters)
    list_of_parameters = my_map(my_multiply, list_of_parameters)
    print("After: ", list_of_parameters)

if __name__ == '__main__':
    main()

from functools import reduce

def func_lambda():

    palindrome = lambda string: string == string[::-1]

    print("Is palindrome ", palindrome('ana'))
    funct_filter()

def funct_filter():
    # Using list comprehension for odd numbers
    my_list = [1,4,5,6,9,13,19,21]
    odd = [i for i in my_list if i % 2 != 0]
    print("Normal: ", odd)
    # Using filter function
    odd = list(filter(lambda x: x%2 != 0, my_list))
    print("List function", odd)

    funct_map()

def funct_map():
    # Using list comprehensions for squares of each number of list by 2
    my_list = [1,2,3,4,5]
    squares = [i**2 for i in my_list]

    print("Normal: ",squares)

    # Using map function
    squares = list(map(lambda x: x**2, my_list))
    print("Using map: ",squares)

    funct_reduce()

def funct_reduce():
    # Using normal path
    my_list = [2,2,2,2,2]

    all_multiplied = 1

    for i in my_list:
        all_multiplied = all_multiplied * i

    print("Normal: ",all_multiplied)
    # Using reduce function
    all_multiplied = reduce(lambda a, b: a * b, my_list)
    print("Using Reduce funct", all_multiplied)


if __name__ == '__main__':
    func_lambda()
    
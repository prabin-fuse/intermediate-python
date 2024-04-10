def square_numbers(int_list):
    '''
    Sqaures each item of the list using map()

    Parameters:
    int_list : list of integers to be squaresd

    Results:
    squared : list of integers after squaring each of them
    '''
    sqaured = list(map(lambda item: item ** 2, int_list))
    return sqaured


def convert_to_uppercase(str_list):
    """
    converts to uppercase for each strings using map()

    Parameters: 
    str_list = list of strings

    Results: 
    upper_list = list of string converted into upper case
    """
    uppered = list(map(lambda item: item.upper(), str_list))
    return uppered


def is_prime(num):
    '''
    tells if the given number is prime or not

    parameters:
    num = the number to be check 

    Returns:
    True = if the give number is prime
    False = not pricme
    '''
    if(num <= 1):
        return True
    for i in range(2, int(num ** 0.5) +1):
        if(num %i) ==0:
            return False
    return True


def filter_prime_numbers(int_list):

    prime_numbers = list(filter(lambda item: is_prime(item), int_list ))
    return prime_numbers


def filter_long_strings(str_list):
    long_string = list(filter(lambda x: len(x)> 5, str_list))
    return long_string


### Reduce section:
from functools import reduce

def calculate_factorial(num):
    factorial = reduce(lambda x, y: x*y , range(1, num + 1))
    return factorial

def concatenate_strings(str_list):
    full_string = reduce(lambda x , y : x + y, str_list)
    return full_string


### testing the functions:
int_list = [4,8,14,53,56,7]
str_list = ["word", "Prabin", "embeddINGs", "ate"]
num = 4

print(f"The squaares of list {int_list}  is : ", square_numbers(int_list))
print(f"The uppercase of {str_list} is : {convert_to_uppercase(str_list)}")
print(f"The prime numbers from list {int_list} are: {filter_prime_numbers(int_list)}")
print(f"The long strings from list {str_list} are: {filter_long_strings(str_list)}")
print(f"The factorial of number {num} is : {calculate_factorial(num)}")
print(f"The concatenated form of strings {str_list} is : {concatenate_strings(str_list)}")
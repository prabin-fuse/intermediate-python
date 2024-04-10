def sum_args(*numbers):
    """
    Sums all the number given in the positional argument the is arbitary.

    Parameters:
    *numbers = variable length arguments (int or float)

    Returns:
    sum = the result after summing all of the numberss.
    """

    sum = 0
    for num in numbers:
        sum += num
    return sum


def concat_strings(*strings):
    """
    Concats all the strings given.

    Parameters: 
    *strings = any number of string arguments

    Returns:
    the concatenated single string
    """
    concat_string= ""
    for str in strings:
        concat_string += str
    
    return concat_string


def calculate_total_cost(**kwargs_purchased):
    """
    Totals the price of all items in given kwargs.

    Parameter:
    **kwargs_purchased: (key-value): key = name of item and value= price of item.

    Results:
    total_cost = the final cost of all the items
    """
    total_cost = 0
    for price in kwargs_purchased.values():
        total_cost += price

    return total_cost


def create_student_report(s_name, s_age, **kwargs_sub_marks):
    pass

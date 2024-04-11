### Exception Handling Assignment day2:
def division(num1, num2):

    try:
        ans = num1/num2
        print(f"The answer of dividing {num1} by {num2} is : {ans} ")
    except ZeroDivisionError as e:
        print("Error! Divisor is zero. Please change it or handle it.")
    

def user_file():
    try:    
        file_name = input("\n\nPlease give the file name you want to access : ")
        print(f"\nReading from {file_name} :" )
        file = open(file_name)
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("The required file is not found")


def convert_to_int(str):
    print(f"Original Input : {str}")
    try:
        print(f"Converted to integer : {int(str)}")
    except ValueError:
        print("The given input cannot be converted into integer. Please give integer compatible string.")
    

def division_both_error(num1, num2):
    try:
        ans = num1/num2
        print(f"The answer of dividing {num1} by {num2} is : {ans} ")
    except ZeroDivisionError as e:
        print("Error! Divisor is zero. Please change it or handle it.")
    except ValueError:
        print("The given value is not interger or float")



### testing functions:
def testing_functions():
    print("1) Division => ZeroDivisionError")
    print("2) Filename and read content")
    print("3) Integer conversion")
    print("4) Division => ZeroDivisionError and Value Error")

    option = int(input("\nChoose the options : "))
    #print(option)

    if option == 1:
        num1 = int(input("Enter the dividend : "))
        num2 = int(input("Enter the divisor : "))
        division(num1, num2)
    elif option == 2:
        user_file()
    elif option == 3:
        string = input("Enter the string to type cast in integer : ")
        convert_to_int(string)
    elif option == 4:
        num1 = int(input("Enter the dividend : "))
        num2 = int(input("Enter the divisor : "))
        division_both_error(num1, num2)


### main

testing_functions()




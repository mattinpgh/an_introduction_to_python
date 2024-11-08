# an_introduction_to_python/2_introduction_to_programming/functions_and_methods.py


# * What happens when you run the following program? Why do we get that result?
'''You get a nameerror because the function doesn't return anything.'''

# * Take a look at this code snippet:
'''It prints 'bar' because the function doesn't affect the outer scope'''

# * Write a program that uses a multiply function to multiply two numbers and 
# * returns the result. Ask the user to enter the two numbers, then output the 
# * numbers and result as a simple equation.

def multiply():
    num_one = int(input('Enter the first of two numbers: '))
    num_two = int(input('Enter the second of two numbers: '))
    return num_one, num_two, (num_one * num_two)

# * Consider this code:
'''
def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

product = multiply_numbers(2, 3, 4)'''
# Identiy the following:
'''
function name:      multiply_numbers()
function arguments  2, 3, 4
function definition     def multiply_numbers(num1, num2, num3):; result = num1 * num2 * num3; return result
function body           result = num1 * num2 * num3; return result
function parameters num1, num2, num3
function invocation product = multiply_numbers(2, 3, 4)
function return value    return result
all identifiers
'''

# * What does the following code print?
'''Nothing. It returns 'Yippee!!!!' but doesn't print it.'''

# * What does the following code print?
'''!!!It prints Yippee!!!!

I was wrong here - I missed the return before the calling of print'''

# * Without running the following code, what do you think it will do?
'''It's going to raise an error because qux has no default value'''

# * Without running the following code, what do you think it will do?
'''It's going to raise an error because 3 arguments were passed instead of 2'''

# * Without running the following code, what do you think it will do?
'''print 42, 3.141592, 2.718 on new lines'''

# * Without running the following code, what do you think it will do?
'''42, 3.141592), and the default,m 2'''

# * Without running the following code, what do you think it will do?
'''It will print 42, 3, 2'''

# * Without running the following code, what do you think it will do?
'''It will return an error because the first parameter has no default argument'''

# * Without running the following code, what do you think it will do?
'''It will return an error because the third parameter has no defualt argument'''

# * Identify all of the identifiers on each line of the following code.
'''multiply, left, right, get_num, prompt, first_number, second_number, product'''
# I missed input and print

# * Using the code below, classify the identifiers as global, local, or 
# * built-in. For our purposes, you may assume this code is the entire program.
'''
multiply=global
left,right=local
get_num=global
prompt= local as a parameter, possibly global as a return value
first_number, second_number=GLOBAL
product=global

'''

# * In the code shown below, identify all of the function names and parameters 
# * present in the code. Include the line numbers for each item identified.
'''
multiply: ln 1, ln 9 function name
left, right: ln 1, ln 2, parameters
get_num, ln 4, ln 7, ln 8, function name
prompt: ln 4, ln 5parameter
--I keep ignoring the built in functions
'''

# * Use this function to determine which of the following lists contains at 
# * least one number that is not evenly divisible by 3 (that is, the remainder 
# * is not 0):

'''
def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []
'''

def remainders_3(numbers):
    return [number % 3 for number in numbers]
numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(any(remainders_3(numbers_1)))     
print(any(remainders_3(numbers_2)))     
print(any(remainders_3(numbers_3)))     
print(any(remainders_3(numbers_4)))

# * The following function returns a list of the remainders of dividing the 
# * numbers in numbers by 5: Use this function to determine which of the 
# * following lists do not contain any numbers that are divisible by 5:

def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainders_5(numbers_1)))     
print(all(remainders_5(numbers_2)))     
print(all(remainders_5(numbers_3)))     
print(all(remainders_5(numbers_4)))
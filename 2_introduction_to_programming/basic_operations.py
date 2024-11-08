# an_introduction_to_python/introduction_to_programming/basic_operations.py


# * Concatenate two strings, one with your first name and one with your  
# * last, to create a new string with your full name as its value. For  
# * example, if your name is John Doe, you should combine 'John' and 'Doe' 
# * to get 'John Doe'.

first_name = 'Matt'
last_name = 'Smith'
full_name = first_name + ' ' + last_name

# * This question may be a little challenging if your math skills are rusty. 
# * Don't be afraid to take advantage of the hints. Try your best to solve the 
# * problem, but don't feel compelled to complete it if you become frustrated.

# * Use the REPL and the arithmetic operators to extract the 
# * individual digits of 4936:

'''One place is 6.
Tens place is 3.
Hundreds place is 9.
Thousands place is 4.'''

ones, tens, hundreds, thousands = 0, 0, 0, 0
full_num = 4936
ones = full_num % 10
full_num = full_num // 10
tens = full_num % 10
full_num = full_num // 10
hundreds = full_num % 10
full_num = full_num // 10
thousands = full_num % 10
full_num = full_num // 10

print(f'1. Ones place is {ones}, \n2. Tens place is {tens}, \n3. Hundreds \
    place is {hundreds}, \n4. Thousands place is {thousands}.')

# * What does the following code do? Why?
# print('5' + '10')

'''It concatenates the two strings together to form '510'.'''

# * Refactor the code from the previous exercise to use coercion to print 15

print(int('5') + int('10'))

# * Will an error occur if you try to access a list element with an index 
# * greater than or equal to the list's length? For example: letters , for
# * examples: foo = ['a', 'b', 'c'] print(foo[3])      

'''Yes, this will produce an IndexError.'''

# * To what value does the following expression evaluate? 'foo' == 'Foo'

'''False. Strings are case-sensitive.'''

# * What will the following code do? Why? int('3.1415')

'''It will produce an error because only whole numbers can be converted to
integers. You could instead convert it to a float and // by 1, then convert'''

print(type(int(float('3.1415') // 1))) # returns <class 'int'>

# * To what value does the following expression evaluate? '12' < '9'

'''True. The first character of '12' < the first character of '9'.'''
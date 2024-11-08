# an_introduction_to_python/2_introduction_to_programming/variables.py


# * Classify the following potential non-constant variable names as idiomatic, 
# * non-idiomatic, or illegal. For the non-idiomatic and illegal names, 
# * explain your choice.

'''
Name        Classification  Reason
index       idiomatic       it's not reserved, it's clear, it's in snake case
CatName     non-idiomatic   not in snake case
lazy_dog    idiomatic       it's clear, it's in snake case
quick_Fox   non-idiomatic   not in snake case
1stCharacter    illegal     starts with a number
operand2    idiomatic       it's clear, it's in snake case
BIG_NUMBER  non-idiomatic   all caps - idiomatic if it's a constant
π           non-idiomatic   the variable name is not in English/non-ascii'''

# * Classify the following potential function names as idiomatic, 
# * non-idiomatic, or illegal. For the non-idiomatic and illegal names, 
# * explain your choice.

'''
Name        Classification  Reason
index       idiomatic       it's not reserved, it's clear, it's in snake case
CatName     non-idiomatic   not in snake case
lazy_dog   idiomatic       it's clear, it's in snake case
quick_Fox   non-idiomatic   not in snake case
1stCharacter    illegal     starts with a number
operand2    idiomatic       it's clear, it's in snake case
BIG_NUMBER  non-idiomatic   all caps
π           non-idiomatic   the variable name is not in English/non-ascii'''

# * Classify the following potential class names as idiomatic, non-idiomatic, 
# * or illegal. For the non-idiomatic and illegal names, explain your choice.

'''
Name        Classification  Reason
index       non-idiomatic   not in camel case
CatName     idiomatic       it's clear, it's in camel case
Lazy_Dog    non-idiomatic   shouldn't use underscores in class names
1ST         illegal         starts with a number
operand2    non-idiomatic   not in camel case
BigNumber3 idiomatic       it's clear, it's in camel case
Πi      non-idiomatic   the first character is not in English/non-ascii
'''

# * Write a program named greeter.py that greets 'Victor' three times. Your 
# * program should use a variable and not hard code the string value 'Victor' 
# * in each greeting. Here's an example run of the program:

name = 'Victor'
time_of_day = ['Morning', 'Afternoon', 'Evening']
for time in time_of_day:
    print(f'Good {time}, {name}.')

# * Write a program named age.py that includes someone's age and then 
# * calculates and reports the future age 10, 20, 30, and 40 years from now. 

age = input('Enter your age: ')
print(f'You are {age} years old.')
age_range = [10, 20, 30, 40]
for years in age_range:
    future_age = int(age) + years
    print(f'In {years} years, you will be {future_age} years old.')

# * What happens when you run the following code? Why?

'''The program greets victorx3, then  ninax3. The value of the variable is 
changed to 'Nina' and the program is run again. '''

# * This program uses a bit of math. Don't let that scare you away -- try it anyway.

'''Assume you have $1,000.00 in the bank, and you've somehow managed to find a 
bank that pays you 5% (this is a wish-fulfillment fantasy) compounded interest 
every year. After one year, you will have $1,050 ($1,000 times 1.05). After two 
years, you will have $1,050 times 1.05, or $1102.50. Create a variable named 
balance that contains the amount of money you will have after 5 years, then 
print the result. Use a single expression if you can to set balance to the 
correct value.'''

balance = 1000.00 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05
print(balance)

# * Repeat the previous question but, this time, use augmented assignment to 
# * compute the final result, one year at a time.

balance = 1000.00  
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
print(balance)

# * Assume that obj already has a value of 42 when the code below starts 
# * running. Which of the subsequent statements reassign the variable? Which 
# * statements mutate the value of the object that obj references? Which 
# * statements do neither? If necessary, you can read the documentation.

'''
Reassign:           Mutate:             Neither:
obj = 'ABcd'        !obj = list(obj)!   obj.upper()
obj = obj.lower()   object.pop()        print(len(obj))
obj = tuple(obj)    obj[2] = 'X'        set(obj)            
                    obj.sort()      
'''
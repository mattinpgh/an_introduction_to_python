# an_introduction_to_python/2_introduction_to_programming/age.py


# * Write a program named age.py that asks the user to enter their age, then 
# calculates and reports the future age 10, 20, 30, and 40 years from now. 
age = input('Enter your age: ')
age_range = [10, 20, 30, 40]
for years in age_range:
    future_age = int(age) + years
    print(f'In {years} years, you will be {future_age} years old.')
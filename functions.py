#greet function
def greet(name, age, location):
    greeting = f'Hello, my name is {name}, '
    greeting += f'I am {age} years old, '
    greeting += f'and I live in {location}'
    return greeting

print(greet('Jane', 30, 'Ireland'))
print(greet('John', 20, 'Spain'))

#addition function
def addition(number_one, number_two):
    total = number_one + number_two
    return total

first_addition = addition(3,5)
second_addition = addition(6,10)
final_addition = first_addition + second_addition
print(final_addition)

# is positive function
def is_positive(num):
    # if the num parameter is greater than 0 return true
    # if it is less than 0 return false
    if num >= 0:
        return True
    elif num < 0:
        return False

# print(is_positive(5))
# print(is_positive(-10))

# even or odd function
def even_or_odd(num):
    #if the num parameter is even return 'Even'
    #if the num parameter is odd, return 'Odd
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


print(even_or_odd(2))
print(even_or_odd(7))

# get grade function

def get_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    return grade

mark_grade = get_grade(52)

# print number function
def print_numbers(num):
    # Return a list of numbers starting at 1, and going up to the number provided
    # [1, 2, 3, 4, 5]
    values = []
    for i in range(1, num+1):
        values.append(i)
    return values

print(print_numbers(5))

# find the largest number
def find_largest(numbers):
    # numbers parameter takes a list of number [12, 50, 38, 44, 150, 5]
    # find and return the largest number in the list
    # if a number is larger than another number
    # we will need to loop over the list

    largest = numbers[0] 
    print(largest)
    for number in numbers: 
        if number > largest:  
            largest = number
            

    return largest

print(find_largest([12, 50, 38, 44, 150, 5]))
print(find_largest([55, 3, 500, 12, 25]))


def check_user(name): #check_user('mark')
    if name == 'Bob':
        return 'Nice to see you again'
    else:
        return 'Hello'


def welcome_user(name, language):  # name = mark, language = Python
    # Hello Mark, welcome to Python
    # Bob, nice to see you again Bob

    initial_greeting = check_user(name) # check_user('mark')

    greeting = f"{initial_greeting} {name}, welcome to {language}"

    return greeting


def take_order(name):

    initial_greeting = check_user(name)
    
    return f"{initial_greeting} {name}, can I take your order?"

print(take_order('Bob', 'Python'))


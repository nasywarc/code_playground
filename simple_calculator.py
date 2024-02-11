import math, os

def plus (num_one, num_two):
    return num_one + num_two

def sub (num_one, num_two):
    return num_one - num_two

def multi(num_one, num_two):
    return num_one * num_two

def div(num_one, num_two):
    return num_one / num_two

def sq(num_one):
    return math.sqrt(num_one)

def power(num_one):
    return math.pow(num_one, 2)

while True:

    os.system('cls')
    operation = input(
'''1. Add
2. Sub
3. Multiply
4. Division
5. Square
6. Power
Type your choice : ''')
    
    try:
        operation = int(operation)
    except:
        print('\nYour input is invalid.')
    if operation in [1, 2, 3, 4, 5, 6]:    
        input_num_one = int(input('Type the first number : '))
        if operation not in [5, 6]:
            input_num_two = int(input('Type the second number : '))
        if operation == 1:
            print(plus(input_num_one, input_num_two))
        elif operation == 2:
            print(sub(input_num_one, input_num_two))
        elif operation == 3:
            print(multi(input_num_one, input_num_two))
        elif operation == 4:
            print(div(input_num_one, input_num_two))
        elif operation == 5:
            print(sq(input_num_one))
        elif operation == 6:
            print(power(input_num_one))
        else:
            print('Your input is invalid.')
        continue_or_no = input('\nDo you want to continue? ')
        if continue_or_no != 'yes':
            break

print('Bye!')
import math, os

def plus (num_one, num_two):
    print(f'{num_one} + {num_two} = {num_one + num_two}')

def sub (num_one, num_two):
    print(f'{num_one} - {num_two} = {num_one - num_two}')

def multi(num_one, num_two):
    print(f'{num_one} * {num_two} = {num_one * num_two}')

def div(num_one, num_two):
    print(f'{num_one} / {num_two} = {num_one / num_two}')

def sq(num_one):
    print(f'The square of {num_one} is {math.sqrt(num_one)}')

def power(num_one):
    print(f'The power of {num_one} is {math.pow(num_one, 2)}')

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
        pass
        
    if operation in [1, 2, 3, 4, 5, 6]:    
        input_num_one = int(input('\nType the first number : '))
        if operation not in [5, 6]:
            input_num_two = int(input('Type the second number : '))
        if operation == 1:
            plus(input_num_one, input_num_two)
        elif operation == 2:
            sub(input_num_one, input_num_two)
        elif operation == 3:
            multi(input_num_one, input_num_two)
        elif operation == 4:
            div(input_num_one, input_num_two)
        elif operation == 5:
            sq(input_num_one)
        else:
            power(input_num_one)
    else:
        print('\nYour input is invalid.')
    continue_or_no = input('Do you want to continue?\n')
    if continue_or_no != 'yes':
        break

print('Bye!\n')
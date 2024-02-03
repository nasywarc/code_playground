import math

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

def pow(num_one):
    return math.pow(num_one, 2)

operation = (input('Type "Add" or "Sub" or "Multi" or "Div" or "Sq" or "Pow" : ')).upper()

input_num_one = int(input('Type the first number : '))
if operation not in ['SQ', 'POW']:
    input_num_two = int(input('Type the second number : '))

if operation == 'ADD':
    print(plus(input_num_one, input_num_two))
elif operation == 'SUB':
    print(sub(input_num_one, input_num_two))
elif operation == 'DIV':
    print(div(input_num_one, input_num_two))
elif operation == 'POW':
    print(pow(input_num_one))
elif operation == 'SQ':
    print(sq(input_num_one))
else:
    print(multi(input_num_one, input_num_two))
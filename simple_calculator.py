def plus (num_one, num_two):
    return num_one + num_two

def sub (num_one, num_two):
    return num_one - num_two

operation = (input('Type "Add" or "Sub" : ')).upper()

input_num_one = int(input('Type the first number : '))
input_num_two = int(input('Type the second number : '))

if operation == 'ADD':
    print(plus(input_num_one, input_num_one))
else:
    print(sub(input_num_one, input_num_two))
letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

user_input = (input('Type a Letter : ')).upper()

if user_input in letter:
    letter_index = letter.index(user_input)
    
print(letter_index + 1)
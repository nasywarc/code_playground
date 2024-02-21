import tkinter

window = tkinter.Tk()
window.title('Calculator App')
# window.minsize(width=300, height=400)
# window.maxsize(width=300, height=400)
# window.geometry('300x400')

result = tkinter.Label(text='Hello World', height=4)
result.grid(row=0, column=0, columnspan=3)

one = tkinter.Button(text='1', width=7, height=4)
one.grid(row=1, column=0)

two = tkinter.Button(text='2', width=7, height=4)
two.grid(row=1, column=1)

three = tkinter.Button(text='3', width=7, height=4)
three.grid(row=1, column=2)

four = tkinter.Button(text='4', width=7, height=4)
four.grid(row=2, column=0)

five = tkinter.Button(text='5', width=7, height=4)
five.grid(row=2, column=1)

six = tkinter.Button(text='6', width=7, height=4)
six.grid(row=2, column=2)

seven = tkinter.Button(text='7', width=7, height=4)
seven.grid(row=3, column=0)

eight = tkinter.Button(text='8', width=7, height=4)
eight.grid(row=3, column=1)

nine = tkinter.Button(text='9', width=7, height=4)
nine.grid(row=3, column=2)

zero = tkinter.Button(text='0', width=7, height=4)
zero.grid(row=4, column=1)

window.mainloop()
from tkinter import Label, Button, Tk, Entry

window = Tk()
window.title('Calculator App')
window.config(background='#000')

result = Label(text='Calculation', height=4, background='#000', foreground='#FFF')
result.grid(row=0, column=0, columnspan=4)

one = Button(text='7', width=7, height=4, background='#000', foreground='#FFF')
one.grid(row=1, column=0)

two = Button(text='8', width=7, height=4, background='#000', foreground='#FFF')
two.grid(row=1, column=1)

three = Button(text='9', width=7, height=4, background='#000', foreground='#FFF')
three.grid(row=1, column=2)

four = Button(text='4', width=7, height=4, background='#000', foreground='#FFF')
four.grid(row=2, column=0)

five = Button(text='5', width=7, height=4, background='#000', foreground='#FFF')
five.grid(row=2, column=1)

six = Button(text='6', width=7, height=4, background='#000', foreground='#FFF')
six.grid(row=2, column=2)

seven = Button(text='1', width=7, height=4, background='#000', foreground='#FFF')
seven.grid(row=3, column=0)

eight = Button(text='2', width=7, height=4, background='#000', foreground='#FFF')
eight.grid(row=3, column=1)

nine = Button(text='3', width=7, height=4, background='#000', foreground='#FFF')
nine.grid(row=3, column=2)

zero = Button(text='0', width=7, height=4, background='#000', foreground='#FFF')
zero.grid(row=4, column=1)

plus = Button(text='+', width=7, height=4, background='#000', foreground='#FFF')
plus.grid(row=3, column=3)

minus = Button(text='-', width=7, height=4, background='#000', foreground='#FFF')
minus.grid(row=2, column=3)

multiply = Button(text='x', width=7, height=4, background='#000', foreground='#FFF')
multiply.grid(row=1, column=3)

equal = Button(text='=', width=7, height=4, background='#000', foreground='#FFF')
equal.grid(row=4, column=3)

window.mainloop()
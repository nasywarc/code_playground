import tkinter as tk

window = tk.Tk()
window.title('Calculator App')
window.config(background='#000')

result = tk.Label(text='Result', height=4, background='#000', foreground='#FFF')
result.grid(row=0, column=0, columnspan=3)

one = tk.Button(text='7', width=7, height=4, background='#000', foreground='#FFF')
one.grid(row=1, column=0)

two = tk.Button(text='8', width=7, height=4, background='#000', foreground='#FFF')
two.grid(row=1, column=1)

three = tk.Button(text='9', width=7, height=4, background='#000', foreground='#FFF')
three.grid(row=1, column=2)

four = tk.Button(text='4', width=7, height=4, background='#000', foreground='#FFF')
four.grid(row=2, column=0)

five = tk.Button(text='5', width=7, height=4, background='#000', foreground='#FFF')
five.grid(row=2, column=1)

six = tk.Button(text='6', width=7, height=4, background='#000', foreground='#FFF')
six.grid(row=2, column=2)

seven = tk.Button(text='1', width=7, height=4, background='#000', foreground='#FFF')
seven.grid(row=3, column=0)

eight = tk.Button(text='2', width=7, height=4, background='#000', foreground='#FFF')
eight.grid(row=3, column=1)

nine = tk.Button(text='3', width=7, height=4, background='#000', foreground='#FFF')
nine.grid(row=3, column=2)

zero = tk.Button(text='0', width=7, height=4, background='#000', foreground='#FFF')
zero.grid(row=4, column=1)

plus = tk.Button(text='+', width=7, height=4, background='#000', foreground='#FFF')
plus.grid(row=4, column=0)

minus = tk.Button(text='-', width=7, height=4, background='#000', foreground='#FFF')
minus.grid(row=4, column=2)

window.mainloop()
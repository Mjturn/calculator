from tkinter import *
from tkinter import messagebox

root = Tk()
text = ''
text_input = StringVar()


def press(num):
    global text
    text += str(num)
    text_input.set(text)


def equals():
    try:
        total = str(eval(text))
        text_input.set(total)
    except SyntaxError:
        messagebox.showerror('Try again', "Sorry, what you've entered was invalid. Please try again.")
        text_input.set('0')


def clr():
    global text
    text = ''
    text_input.set(text)


def delete():
    global text
    text = text[:-1]
    text_input.set(text)


def create_window():
    root.title('Calculator')
    root.iconbitmap('images\calc_icon.ico')
    text_input.set('0')
    calc_box = Entry(root, font=('comic sans', 20), textvariable=text_input, bg='#282828', fg='white', borderwidth=0,
                     justify='right')
    calc_box.grid(row=0, column=0, rowspan=2, columnspan=6, sticky='nsew')
    button7 = Button(root, font=('comic sans', 20), text='7', width=4, height=2, bg='black', fg='white', borderwidth=0,
                     command=lambda: press('7'))
    button7.grid(row=2, column=0)
    button8 = Button(root, font=('comic sans', 20), text='8', width=4, height=2, bg='black', fg='white', borderwidth=0,
                     command=lambda: press('8'))
    button8.grid(row=2, column=1)
    button9 = Button(root, font=('comic sans', 20), text='9', width=4, height=2, bg='black', fg='white', borderwidth=0,
                     command=lambda: press('9'))
    button9.grid(row=2, column=2)
    button4 = Button(root, font=('comic sans', 20), text='4', width=4, height=2, bg='black', fg='white', borderwidth=0,
                     command=lambda: press('4'))
    button4.grid(row=3, column=0)
    button5 = Button(root, font=('comic sans', 20), text='5', width=4, height=2, bg='black', fg='white', borderwidth=0,
                     command=lambda: press('5'))
    button5.grid(row=3, column=1)
    button6 = Button(root, font=('comic sans', 20), text='6', width=4, height=2, bg='black', fg='white', borderwidth=0,
                     command=lambda: press('6'))
    button6.grid(row=3, column=2)
    button1 = Button(root, font=('comic sans', 20), text='1', width=4, height=2, bg='black', fg='white', borderwidth=0,
                     command=lambda: press('1'))
    button1.grid(row=4, column=0)
    button2 = Button(root, font=('comic sans', 20), text='2', width=4, height=2, bg='black', fg='white', borderwidth=0,
                     command=lambda: press('2'))
    button2.grid(row=4, column=1)
    button3 = Button(root, font=('comic sans', 20), text='3', width=4, height=2, bg='black', fg='white', borderwidth=0,
                     command=lambda: press('3'))
    button3.grid(row=4, column=2)
    button0 = Button(root, font=('comic sans', 20), text='0', width=4, height=2, bg='black', fg='white', borderwidth=0,
                     command=lambda: press('0'))
    button0.grid(row=5, column=0, columnspan=3, sticky='nsew')
    decimal = Button(root, font=('comic sans', 20), text='.', width=4, height=2, bg='black', fg='white', borderwidth=0,
                     command=lambda: press('.'))
    decimal.grid(row=5, column=2)
    plus_button = Button(root, font=('comic sans', 20), text='+', width=4, height=2, bg='#282828', fg='white',
                         borderwidth=0,
                         command=lambda: press('+'))
    plus_button.grid(row=5, column=3)
    minus_button = Button(root, font=('comic sans', 20), text='-', width=4, height=2, bg='#282828', fg='white',
                          borderwidth=0,
                          command=lambda: press('-'))
    minus_button.grid(row=4, column=3)
    multiply_button = Button(root, font=('comic sans', 20), text='*', width=4, height=2, bg='#282828', fg='white',
                             borderwidth=0,
                             command=lambda: press('*'))
    multiply_button.grid(row=3, column=3)
    divide_button = Button(root, font=('comic sans', 20), text='/', width=4, height=2, bg='#282828', fg='white',
                           borderwidth=0,
                           command=lambda: press('/'))
    divide_button.grid(row=2, column=3)
    equals_button = Button(root, font=('comic sans', 20), text='=', width=4, height=2, bg='red', fg='white',
                           borderwidth=0,
                           command=equals)
    equals_button.grid(row=5, column=4)
    clear = Button(root, font=('comic sans', 20), text='CLR', width=4, height=2, bg='#282828', fg='white',
                   borderwidth=0,
                   command=clr)
    clear.grid(row=3, column=4, rowspan=2, sticky='nsew')
    delete_button = Button(root, font=('comic sans', 20), text='DEL', width=4, height=2, bg='#282828', fg='white',
                           borderwidth=0,
                           command=delete)
    delete_button.grid(row=2, column=4)
    root.mainloop()


create_window()

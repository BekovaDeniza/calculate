from tkinter import *
from decimal import *

window = Tk()
window.title("Calculate")
window["bg"] = '#000000'
window.resizable(width=False, height=False)

buttons = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ["0", ".", "=", '/']
]

global stack
stack = ['', '', '']
global result
result = '0'
global output
output = Label(window, text='', font=f'Courier 35', fg='#FFFF00', bg='#000000')
output.grid(row=1, column=0, columnspan=5)


def draw_buttons():
    counter_x = 1
    counter_y = 3
    size_btn_x = 30
    size_btn_y = 30
    for btn_y in buttons:
        for btn_x_y in btn_y:
            com = lambda x = btn_x_y: logical(x)
            btn = Button(text=btn_x_y,
                         background='#000000',
                         foreground='#FFFF00',
                         padx=str(size_btn_x),
                         pady=str(size_btn_y),
                         font='Courier 20',
                         command=com)
            btn.grid(row=counter_y, column=counter_x)
            counter_x += 1
        counter_x = 1
        counter_y += 1


def output_update():
    global output
    global result
    Label(window, text='', font='Courier 12', fg='#FFFF00', bg='#000000').grid(row=0, column=0, columnspan=5)
    Label(window, text='', font='Courier 12', fg='#FFFF00', bg='#000000').grid(row=2, column=0, columnspan=5)
    result = str(result)
    if len(result) <= 13:
        font_size = 35
    elif len(result) <= 16:
        font_size = 30
    else:
        font_size = 25
    output.config(text=result, font=f'Courier {font_size}')


def logical(operation):
    global stack
    global result
    if operation.isdigit() or operation == '.':
        if stack[1] == '' and len(stack[0]) < 9:
            if operation.isdigit():
                stack[0] += operation
            elif operation == '.':
                if stack[0] != '':
                    stack[0] += '.'
                elif stack[0] == '':
                    stack += '0.'
        if stack[1] != '' and len(stack[2]) < 9:
            if operation.isdigit():
                stack[2] += operation
            elif operation == '.':
                if stack[2] != '':
                    stack[2] += '.'
                elif stack[2] == '':
                    stack += '0.'
    elif operation in ['+', '-', '*', '/']:
        if operation == '-' and stack[0] == '':
            stack[0] += '-'
        else:
            stack[1] = operation
    result = stack[0] + stack[1] + stack[2]
    if operation == '=' and (stack[0] != '' and stack[1] != '' and stack[2] != ''):
        calculate()
    output_update()


def calculate():
    global stack
    global result
    operand_2 = Decimal(stack.pop())
    operation = stack.pop()
    operand_1 = Decimal(stack.pop())
    stack = ['', '', '']
    if operation == '+':
        result = operand_1 + operand_2
    elif operation == '-':
        result = operand_1 - operand_2
    elif operation == '*':
        result = operand_1 * operand_2
    elif operation == '/':
        result = operand_1 / operand_2


output_update()
draw_buttons()
window.mainloop()

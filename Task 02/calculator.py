# --- Import Libraries ---
from tkinter import *

expression = ''
first_number = second_number = operator = None

def update_expression_label():
    expression_label.config(text=expression)

def update_result_label(result_text=''):
    result_label.config(text=result_text)

def get_digit(digit):
    global expression
    expression += str(digit)
    update_expression_label()

def clear():
    global expression, first_number, second_number, operator
    expression = ''
    first_number = second_number = operator = None
    update_expression_label()
    update_result_label()

def get_operator(op):
    global first_number, operator, expression
    if expression and expression[-1] not in '+-*/%':
        try:
            first_number = float(expression)
            operator = op
            expression += ' ' + op + ' '
            update_expression_label()
        except:
            update_result_label("= Error")

def get_result():
    global expression, first_number, second_number, operator
    if operator and operator in expression:
        try:
            parts = expression.split(operator)
            second_part = parts[1].strip()
            if second_part:
                second_number = float(second_part)
                result = None
                if operator == '+':
                    result = first_number + second_number
                elif operator == '-':
                    result = first_number - second_number
                elif operator == '*':
                    result = first_number * second_number
                elif operator == '/':
                    if second_number == 0:
                        update_result_label("= Error (div by 0)")
                        return
                    result = round(first_number / second_number, 2)
                elif operator == '%':
                    result = first_number % second_number
                update_result_label(f"= {result}")
        except:
            update_result_label("= Error")

def get_dot():
    global expression
    if not expression or expression[-1] in '+-*/% ':
        expression += '0.'
    elif '.' not in expression.split()[-1]:
        expression += '.'
    update_expression_label()

def off():
    root.destroy()

def reciprocal():
    global expression
    try:
        value = float(expression)
        if value == 0:
            update_result_label("= Error (div by 0)")
        else:
            result = round(1 / value, 6)
            expression = str(result)
            update_expression_label()
            update_result_label(f"= {result}")
    except:
        update_result_label("= Error")

# --- Setup ---
root = Tk()
root.title('Calculator')
root.geometry('360x450')  # Adjusted for 5 columns
root.resizable(0, 0)
root.configure(background='#ffffff')

# --- Labels ---
# --- Expression Labels ---
expression_label = Label(root, text='', bg='#ffffff', fg='#1f1f1f', anchor='e')
expression_label.grid(row=0, column=0, columnspan=5, padx=10, pady=(30, 5), sticky='we')
expression_label.config(font=('Segoe UI', 20))

# --- Result Labels ---
result_label = Label(root, text='', bg='#ffffff', fg='#26a69a', anchor='e')
result_label.grid(row=1, column=0, columnspan=5, padx=10, pady=(0, 20), sticky='we')
result_label.config(font=('Segoe UI', 20))

btn_config = {'width': 5, 'height': 2, 'font': ('Segoe UI', 14)}

def make_button(text, row, col, bg, command, fg='#ffffff'):
    btn = Button(root, text=text, bg=bg, fg=fg, command=command,
                 **btn_config, bd=0, relief='flat', activebackground='#dcdcdc')
    btn.grid(row=row, column=col, padx=5, pady=5)
    return btn

# --- Colors ---
digit_bg = '#26a69a'
operator_bg = '#FF7433'
action_bg = '#607D8B'

# --- Row 2 ---
make_button('OFF', 2, 0, action_bg, off)
make_button('C', 2, 1, action_bg, clear)
make_button('1/x', 2, 2, action_bg, reciprocal)
make_button('=', 2, 3, action_bg, get_result)
make_button('/', 2, 4, operator_bg, lambda: get_operator('/'))

# --- Row 3 ---
make_button('9', 3, 0, digit_bg, lambda: get_digit(9))
make_button('8', 3, 1, digit_bg, lambda: get_digit(8))
make_button('7', 3, 2, digit_bg, lambda: get_digit(7))
make_button('6', 3, 3, digit_bg, lambda: get_digit(6))
make_button('-', 3, 4, operator_bg, lambda: get_operator('-'))

# --- Row 4 ---
make_button('5', 4, 0, digit_bg, lambda: get_digit(5))
make_button('4', 4, 1, digit_bg, lambda: get_digit(4))
make_button('3', 4, 2, digit_bg, lambda: get_digit(3))
make_button('2', 4, 3, digit_bg, lambda: get_digit(2))
make_button('%', 4, 4, operator_bg, lambda: get_operator('%'))

# --- Row 5 ---
make_button('1', 5, 0, digit_bg, lambda: get_digit(1))
make_button('0', 5, 1, digit_bg, lambda: get_digit(0))
make_button('.', 5, 2, digit_bg, get_dot)
make_button('+', 5, 3, operator_bg, lambda: get_operator('+'))
make_button('*', 5, 4, operator_bg, lambda: get_operator('*'))

root.mainloop()
import tkinter as tk
import re

window = tk.Tk()
window.title("Calculator")

count = 0

#Functions to handle buttons
def create_button(master, text, func, *args): #Create a button
    if args:
        return tk.Button(master = master, text = text, width = 5, height = 3, command = lambda: func(args))
    else:
        return tk.Button(master = master, text = text, width = 5, height = 3, command = lambda: func())

def insert(button_value): #Insert the text value of the button clicked into the second field from the top
    ent_op.insert(tk.END, button_value)

def clear(): #Clear the second field from the top
    ent_op.delete(0, tk.END)

def clear_all(): #Clear the both entry fields
    clear()
    ent_result.delete(0, tk.END)

def eq(): #Use a regex to determine the operation and return a result inserted in both entry fields
    value = ent_op.get()

    if value.isdigit():
        ent_result.insert(0, value)

    regex = re.compile('(\d*)([-+/*])(\d*)')

    m = regex.match(value)
    num1 = int(m.group(1))
    num2 = int(m.group(3))

    if m.group(2) == '+':
        result = num1 + num2
    elif m.group(2) == '-':
        result = num1 - num2
    elif m.group(2) == '*':
        result = num1 * num2
    else:
        result = num1 / num2

    clear_all()
    ent_result.insert(0, result)
    ent_op.insert(tk.END, result)

#Create three frames for the window
#frm_display to display numbers entered and result of operation
#frm_pad to display a pad with digits and operators
#frm_eq to display an equal Button

frm_display = tk.Frame()
frm_pad = tk.Frame()
frm_eq = tk.Frame()

frm_display.pack()
frm_pad.pack()
frm_eq.pack()

#Create two entry fields for the first frame
ent_result = tk.Entry(master = frm_display, width = 25)
ent_op = tk.Entry(master = frm_display, width = 25)
ent_result.pack()
ent_op.pack()

#Create the main pad

btn_1 = create_button(frm_pad, '1', insert, '1')
btn_2 = create_button(frm_pad, '2', insert, '2')
btn_3 = create_button(frm_pad, '3', insert, '3')
btn_4 = create_button(frm_pad, '4', insert, '4')
btn_5 = create_button(frm_pad, '5', insert, '5')
btn_6 = create_button(frm_pad, '6', insert, '6')
btn_7 = create_button(frm_pad, '7', insert, '7')
btn_8 = create_button(frm_pad, '8', insert, '8')
btn_9 = create_button(frm_pad, '9', insert, '9')

btn_0 = create_button(frm_pad, '0', insert, '0')
btn_AC = create_button(frm_pad, 'AC', clear_all)
btn_C = create_button(frm_pad, 'C', clear)

btn_divide = create_button(frm_pad, '/', insert, '/')
btn_multiply = create_button(frm_pad, '*', insert, '*')
btn_minus = create_button(frm_pad, '-', insert, '-')
btn_plus = create_button(frm_pad, '+', insert, '+')

first_part_pad = [
    btn_1,
    btn_2,
    btn_3,
    btn_4,
    btn_5,
    btn_6,
    btn_7,
    btn_8,
    btn_9
]

second_part_pad = [
    btn_0,
    btn_AC,
    btn_C
]

third_part_pad = [
    btn_divide,
    btn_multiply,
    btn_minus,
    btn_plus
]

for i in range(3, 0, -1):
    for j in range(3):
        first_part_pad[count].grid(row = i, column = j, padx = 5, pady = 5)
        count += 1

for i in range(3):
    second_part_pad[i].grid(row = 4, column = i, padx = 5, pady = 5)

for i in range(1, 5):
    third_part_pad[i - 1].grid(row = i, column = 3, padx = 5, pady = 5)

#Create the last equal button at the bottom of the pad
btn_eq = tk.Button(master = frm_eq, text='=', width = 25, command = eq)
btn_eq.pack(fill=tk.X)

window.mainloop()

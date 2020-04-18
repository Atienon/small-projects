import tkinter as tk
import re

window = tk.Tk()
window.title("Calculator")

count = 0

#Functions to handle buttons

def insert(button_value):
    ent_op.insert(tk.END, button_value)

def clear():
    ent_op.delete(0, tk.END)

def clear_all():
    clear()
    ent_result.delete(0, tk.END)

def eq():
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
#First frame to display numbers entered and result of operation
#Second frame to display a pad with digits and operators
#Third frame to display an equal Button

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
#Issue found: we can create all this buttons with three for loops
#When it comes to get the text value from one button, since it has been created with the
#variable, we end up getting the same last value that was created
#Hence why I'm creating them manually and then looping through them

btn_1 = tk.Button(master = frm_pad, text = '1', width = 5, height = 3, command = lambda: insert('1'))
btn_2 = tk.Button(master = frm_pad, text = '2', width = 5, height = 3, command = lambda: insert('2'))
btn_3 = tk.Button(master = frm_pad, text = '3', width = 5, height = 3, command = lambda: insert('3'))
btn_4 = tk.Button(master = frm_pad, text = '4', width = 5, height = 3, command = lambda: insert('4'))
btn_5 = tk.Button(master = frm_pad, text = '5', width = 5, height = 3, command = lambda: insert('5'))
btn_6 = tk.Button(master = frm_pad, text = '6', width = 5, height = 3, command = lambda: insert('6'))
btn_7 = tk.Button(master = frm_pad, text = '7', width = 5, height = 3, command = lambda: insert('7'))
btn_8 = tk.Button(master = frm_pad, text = '8', width = 5, height = 3, command = lambda: insert('8'))
btn_9 = tk.Button(master = frm_pad, text = '9', width = 5, height = 3, command = lambda: insert('9'))

first_part_pad = [btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9]

btn_0 = tk.Button(master = frm_pad, text = '0', width = 5, height = 3, command = lambda: insert('0'))
btn_AC = tk.Button(master = frm_pad, text = 'AC', width = 5, height = 3, command = clear_all)
btn_C = tk.Button(master = frm_pad, text = 'C', width = 5, height = 3, command = clear)

second_part_pad = [btn_0, btn_AC, btn_C]

btn_divide = tk.Button(master = frm_pad, text = '/', width = 5, height = 3, command = lambda: insert('/'))
btn_multiply = tk.Button(master = frm_pad, text = '*', width = 5, height = 3, command = lambda: insert('*'))
btn_minus = tk.Button(master = frm_pad, text = '-', width = 5, height = 3, command = lambda: insert('-'))
btn_plus = tk.Button(master = frm_pad, text = '+', width = 5, height = 3, command = lambda: insert('+'))

third_part_pad = [btn_divide, btn_multiply, btn_minus, btn_plus]

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

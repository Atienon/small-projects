import tkinter as tk

window = tk.Tk()

count = 1
symbols = ['/', '*', '-', '+']
other_symbols = ['0', '.', 'C']


for i in range(3, 0, -1): # Display buttons for digits 1-9
    for j in range(3):
        frame = tk.Frame(master = window, relief = tk.RAISED, borderwidth = 1)
        frame.grid(row = i, column = j, padx = 5, pady = 5)
        button = tk.Button(master = frame, text = f"{count}", width = 5, height = 3)
        button.pack()
        count += 1

for i in range(1, 5): #Display button on the far-right side for operators
    frame = tk.Frame(master = window, relief = tk.RAISED, borderwidth = 1)
    frame.grid(row = i, column = 3, padx = 5, pady = 5)
    button = tk.Button(master = frame, text = symbols[i - 1], width = 5, height = 3)
    button.pack()

for i in range(3): #Display additional buttons at the bottom of the main digit-pad
    frame = tk.Frame(master = window, relief = tk.RAISED, borderwidth = 1)
    frame.grid(row = 4, column = i, padx = 5, pady = 5)
    button = tk.Button(master = frame, text = other_symbols[i], width = 5, height = 3)
    button.pack()

window.mainloop()

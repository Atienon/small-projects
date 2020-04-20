import tkinter as tk
import json


def check_keys(list): #Check if all the keys are the same to print the proper headers
    keys = list[0].keys()
    for dict in list:
        if dict.keys() == keys:
            pass
        else:
            return False
        return True

def convert_to_csv():

    csv_text_box.delete('1.0', tk.END)

    json_entry = json_text_box.get('1.0', tk.END)

    try: #Check if the file has the correct format
        json_loaded = json.loads(json_entry)

        if check_keys(json_loaded):
                #Print headers from dict keys
                csv_text_box.insert('1.0', ','.join(json_loaded[0].keys()))
                csv_text_box.insert(tk.END, '\n')

                #Print lines
                for i in range(len(json_loaded)):
                    line_list = [json_loaded[i][key] for key in json_loaded[0].keys()]
                    line_list = [str(line_list[i]) for i in range(len(line_list))]
                    csv_text_box.insert(f'{i+2}.0', ','.join(line_list))
                    csv_text_box.insert(tk.END, '\n')
        else:
            csv_text_box.insert('1.0', 'An issue occured. The keys are not the same.')

    except ValueError:
        json_text_box.insert('1.0', 'JSON format incorrect or nothing to convert\n\n')

def clear():
    json_text_box.delete('1.0', tk.END)
    csv_text_box.delete('1.0', tk.END)

window = tk.Tk()
window.title('JSON to CSV')

# Structure of the window
# Two textboxes, one for JSON code, one for CSV code
# Two buttons, submit and clear

frm_text_boxes = tk.Frame()
frm_text_boxes.pack()
frm_buttons = tk.Frame()
frm_buttons.pack()

json_label = tk.Label(master = frm_text_boxes, text = 'JSON', width = 50)
json_label.grid(row = 0, column = 0)

json_scrollbar = tk.Scrollbar(master = frm_text_boxes)
json_text_box = tk.Text(master = frm_text_boxes, height = 25, width = 50)
json_text_box.grid(row = 1, column = 0)
json_scrollbar.grid(row = 1 , column = 1)

json_scrollbar.config(command = json_text_box.yview)
json_text_box.config(yscrollcommand = json_scrollbar.set)

csv_label = tk.Label(master = frm_text_boxes, text = 'CSV', width = 50)
csv_label.grid(row = 0, column = 2)

csv_scrollbar = tk.Scrollbar(master = frm_text_boxes)
csv_text_box = tk.Text(master = frm_text_boxes, height = 25, width = 50)
csv_text_box.grid(row = 1, column = 2)
csv_scrollbar.grid(row = 1, column = 3)

csv_scrollbar.config(command = csv_text_box.yview)
csv_text_box.config(yscrollcommand = csv_scrollbar.set)

convert_button = tk.Button(master = frm_buttons, text = 'Convert', command = convert)
convert_button.pack(side = tk.RIGHT)

clear_button = tk.Button(master = frm_buttons, text = 'Clear', command = clear)
clear_button.pack(side = tk.RIGHT)


window.mainloop()

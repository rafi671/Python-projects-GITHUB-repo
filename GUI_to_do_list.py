import tkinter as tk
root = tk.Tk()
root.title("To Do List") #Main title

#widgets
listbox = tk.Listbox(root)
scrollbar = tk.Scrollbar(root)
entry = tk.Entry(root)
add_button = tk.Button(root, text = "Add")
delete_button = tk.Button(root, text = "Delete")
save_button = tk.Button(root, text = "Save")
load_button = tk.Button(root, text = "Load")

#Widgets Arrangment using grid manager
listbox.grid(row = 0, column = 0, rowspan = 4, sticky= "nsew")
scrollbar.grid(row = 0, column = 1, rowspan = 4, sticky= "ns")
entry.grid(row = 4, column = 0, sticky= "ew")
add_button.grid(row = 5, column = 0, sticky= "ew")
delete_button.grid(row = 6, column = 0, sticky= "ew")
save_button.grid(row = 7, column = 0, sticky= "ew")
load_button.grid(row = 8, column = 0, sticky= "ew")

#Widgets binding with function
def add_item():
    text = entry.get()
    if len(text) > 0:
        listbox.insert(tk.END, text)
    entry.delete(0, tk.END)

def delete_item():
    index = listbox.curselection()
    if len(index) > 0:
        listbox.delete(index)
        
def save_list():
    with open("todo.txt", "w") as file:
        items = listbox.get(0, tk.END)
        for item in items:
            file.write(item + "\n")
            
def load_list():
    with open("todo.txt", "r") as file:
        listbox.delete(0, tk.END)
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            listbox.insert(tk.END, line)
            
add_button.config(command=add_item)
delete_button.config(command=delete_item)
save_button.config(command=save_list)
load_button.config(command=load_list)
entry.bind("<Return>", add_item)

#logic of the functions using the FileI/O module
def save_list():
    file = open("todo.txt", "w")
    items = listbox.get(0, tk.END)
    for item in items:
        file.write(item + "\n")
        file.close()
def load_list():
    file = open("todo.txt", "r")
    listbox.delete(0, tk.END)
    for line in file:
        line = line.strip()
        listbox.insert(tk.END, line)
        file.close()
        
root.mainloop()
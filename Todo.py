import tkinter as tk
import os

TODO_FILE = "aufgabentodo.txt"

def save_tasks():
    with open(TODO_FILE, "w") as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            file.write(tasks + "\n")


def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())




def add():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        print("Add")
        save_tasks()

def delet():
    task = entry.get()
    if task:
        for index in range(listbox.size()):
            if listbox.get(index) == task:
                listbox.delete(index)
                entry.delete(0, tk.END)
                break
            print("delet")




root = tk.Tk()
root.title("ToDo Liste")
root.geometry("300x300")
root.config(bg="blue")



label = tk.Label(root, text="Todo Liste by DevSalz", bg="lightblue", fg="black", font=("Arial", 12))
label.pack()

entry = tk.Entry(root, width=25, bg="lightblue")
entry.pack(pady=10)

add_button = tk.Button(root, text="Aufgabe hinzufügen", command=add, bg="lightblue", fg="black", font=("Arial", 10))
add_button.pack()

delete_button = tk.Button(root, text="Aufgabe erledigt", command=delet, bg="lightblue", fg="black", font=("Arial", 10))
delete_button.pack()

listbox = tk.Listbox(root, width=40, height=10, bg="lightblue")
listbox.pack(pady=10)

root.mainloop()

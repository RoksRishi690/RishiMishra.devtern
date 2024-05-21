import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")
root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack()

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)


listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10, yscrollcommand=scrollbar_tasks.set)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar_tasks.config(command=listbox_tasks.yview)
listbox_tasks.config(bg="lightpink")

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, bg='blue', command=add_task)
button_add_task.pack()

button_remove_task = tk.Button(root, text="Remove Task", width=48, bg='grey', command=remove_task)
button_remove_task.pack()
 
root.mainloop()
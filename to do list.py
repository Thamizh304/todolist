import tkinter as tk
from tkinter import messagebox
import os
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                task_listbox.insert(tk.END, line.strip())
def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")
def add_task():
    task = entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")
def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to delete")
def mark_done():
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        task_listbox.delete(index)
        task_listbox.insert(tk.END, task + " ✅")
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to mark as done")
root = tk.Tk()
root.title("To-Do List App")
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)
task_listbox = tk.Listbox(root, width=45)
task_listbox.pack(pady=10)
del_btn = tk.Button(root, text="Delete Task", command=delete_task)
del_btn.pack(pady=5)
done_btn = tk.Button(root, text="Mark as Done", command=mark_done)
done_btn.pack(pady=5)
load_tasks()
root.mainloop()

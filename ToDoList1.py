
import tkinter as tk
from tkinter import scrolledtext
import pickle

def add_task1():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        notes_list.append("")  
        task_entry.delete(0, tk.END)

def mark_completed():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.itemconfig(selected_task, {'bg': 'light green'})
        task_listbox.selection_clear(0, tk.END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        task_listbox.delete(index)
        notes_list.pop(index)
        task_listbox.selection_clear(0, tk.END)

def add_notes():
    selected_task = task_listbox.curselection()
    if selected_task:
        notes_window = tk.Toplevel(root)
        notes_window.title("Add Notes")
        
        notes_label = tk.Label(notes_window, text="Add notes for the selected task:")
        notes_label.pack(pady=5)
        
        notes_entry = scrolledtext.ScrolledText(notes_window, width=40, height=5, wrap=tk.WORD)
        notes_entry.pack(pady=5)
        
        save_notes_button = tk.Button(notes_window, text="Save", command=lambda: save_notes(selected_task[0], notes_entry, notes_window))
        save_notes_button.pack(pady=5)

def save_notes(index, notes_entry, notes_window):
    notes = notes_entry.get("1.0", tk.END).strip()
    notes_list[index] = notes
    notes_window.destroy()

def show_details():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        details_text.delete("1.0", tk.END)
        details_text.insert(tk.END, notes_list[index])

def update_notes():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        notes = notes_list[index]
        
        update_window = tk.Toplevel(root)
        update_window.title("Update Notes")
        
        update_label = tk.Label(update_window, text="Update notes for the selected task:")
        update_label.pack(pady=5)
        
        update_entry = scrolledtext.ScrolledText(update_window, width=40, height=5, wrap=tk.WORD)
        update_entry.insert(tk.END, notes)
        update_entry.pack(pady=5)
        
        save_update_button = tk.Button(update_window, text="Update", command=lambda: save_updated_notes(index, update_entry, update_window))
        save_update_button.pack(pady=5)

def save_updated_notes(index, update_entry, update_window):
    notes = update_entry.get("1.0", tk.END).strip()
    notes_list[index] = notes
    update_window.destroy()

def save_to_file():
    with open('tasks_data.pkl', 'wb') as file:
        data = {'tasks': task_listbox.get(0, tk.END), 'notes': notes_list}
        pickle.dump(data, file)

def load_from_file():
    try:
        with open('tasks_data.pkl', 'rb') as file:
            data = pickle.load(file)
            task_listbox.delete(0, tk.END)
            task_listbox.insert(tk.END, *data['tasks'])
            notes_list.clear()
            notes_list.extend(data['notes'])
    except FileNotFoundError:
        pass

root = tk.Tk()
root.configure(bg='pink')
root.geometry("2000x2000")
root.title("To-Do List")

task_entry = tk.Entry(root, width=40, bg='skyblue')
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=60, height=15, bg='skyblue')
add_button = tk.Button(root, text="Add Task", command=add_task1, bg='violet')
delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg='orange')

task_entry.pack(pady=10)
add_button.pack(pady=10)
task_listbox.pack()
delete_button.pack()

task_listbox.bind("<<ListboxSelect>>", lambda event: details_text.delete("1.0", tk.END))

mark_completed_button = tk.Button(root, text="Mark Completed", command=mark_completed, bg='lightgreen')
mark_completed_button.pack(pady=10)

show_details_button = tk.Button(root, text="Show Details", command=show_details, bg='lightblue')
show_details_button.pack(pady=10)

add_notes_button = tk.Button(root, text="Add Notes", command=add_notes, bg='yellow')
add_notes_button.pack(pady=10)

update_notes_button = tk.Button(root, text="Update Notes", command=update_notes, bg='lightblue')
update_notes_button.pack(pady=10)

save_button = tk.Button(root, text="Save Tasks", command=save_to_file, bg='lightyellow')
save_button.pack(pady=10)

load_button = tk.Button(root, text="Load Tasks", command=load_from_file, bg='lightgreen')
load_button.pack(pady=10)

details_label = tk.Label(root, text="Task Details:")
details_text = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD)

details_label.pack(pady=5)
details_text.pack(pady=10)

add_button.configure(command=add_task1)
mark_completed_button.configure(command=mark_completed)
delete_button.configure(command=delete_task)

notes_list = []

root.mainloop()

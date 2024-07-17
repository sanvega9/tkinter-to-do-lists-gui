import tkinter as tk
from tkinter import messagebox
#File save history list
History_File = "taskshistory.txt"

#set up main app tk
app = tk.Tk()
app.title("To-DO List APP")
app.geometry("405x665")
app.config(bg="#102C57")

# funtion to add a task toward the list sections
def to_add_task():
    tasks = tasks_entry.get()
    if tasks !="":
        tasks_list.insert(tk.END,tasks)
        tasks_entry.delete(0,tk.END)
    else: 
        messagebox.showwarning("Warning", "You must enter a tasks!")

# function to delete the task completion from the list 
def task_to_delete():
    try:
        tasks_index_select = tasks_list.curselection()[0]
        task = tasks_list.get(tasks_index_select)
        tasks_list.delete(tasks_index_select)
        add_history_file(task + "- DELETED")
    except:
        messagebox.showwarning("Warning", "You must enter a tasks!")
# Function to mark the selected task as completed 
def marking_task_Completed():
    try:
        tasks_index_select = tasks_list.curselection()[0]
        tasks = tasks_list.get(tasks_index_select)
        tasks_list.delete(tasks_index_select)
        tasks_list.insert(tk.END, tasks + " * Completed Great Job")
        add_history_file (tasks+ " * Completed Great Job")
    except:
        messagebox.showwarning("Warning", "You must enter a tasks!")

# function to add an entry to the history and save it to the file
def add_history_file(entry):
    history_lists.insert(tk.END,entry)
    try:
        with open(History_File,"a") as file:
            #space for the write the file
            file.write(entry + "\n")
    except Exception as e:
        messagebox.showerror("Error", f"Could not write to file: {e}")


def loading_history():
    try:
        with open(History_File, "r") as file:
            for line in file:
                history_lists.insert(tk.END, line.strip())
    except FileNotFoundError:
        #These would do is if the file doesn't exist, do nothing
        pass
    except Exception as e:
        messagebox.showerror("Error", f"Could not read to file: {e}")

def delete_history_list():
    history_lists.delete(0,tk.END)
    try:
        with open(History_File,"w") as file:
            file.write("")
    except Exception as e:
        messagebox.showerror("Error", f"Could not clear history: {e}")

def delete_history_entry():
    try: 
        history_index_select = history_lists.curselection()[0]
        history_lists.delete(history_index_select)
        with open(History_File,"w") as file:
           for i in range(history_lists.size()):
               file.write(history_lists.get(i)+ "\n")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a history entry")
    except Exception as e:
        messagebox.showerror("Error", f"Could not update file: {e}")

# task entry field
tasks_entry = tk.Entry(app, width=35)
tasks_entry.pack(pady=10)
tasks_entry.config(bg='#F19ED2', fg='#402E7A')
# add, delete, and mark tasks button & marks any task completed 
add_button_list = tk.Button(app, text="ADD TASK", command=to_add_task, bg="#D8EFD3")
add_button_list.pack(pady=5)

delete_button_list = tk.Button(app,text="DELETE TASK",command=task_to_delete, bg="#FF6969")
delete_button_list.pack(pady=5)

complete_button = tk.Button(app,text="COMPLETED TASK",command=marking_task_Completed, bg="#E9FF97")
complete_button.pack(pady=5)

tasks_label = tk.Label(app, text = " Tasks List ", bg='#102C57',fg='#ffffff')
tasks_label.pack()

# display the text listbox 

tasks_list = tk.Listbox(app, width=35, height=15)
tasks_list.pack(pady=10)

history_label = tk.Label(app, text = "History Tasks File", bg='#102C57',fg='#ffffff')
history_label.pack()

delete_history = tk.Button(app, text="DELETE ALL HISTORY", command=delete_history_list, bg='#FFB1B1')
delete_history.pack(pady=5)

delete_history_entry_Btn = tk.Button(app, text="DELETE SELECTED TASK IN HISTORY", command=delete_history_entry, bg='#FFE4C9')
delete_history_entry_Btn.pack(pady=5)

# Label for history archive
history_lists = tk.Listbox(app, width= 70, height=15)
history_lists.pack(pady=10)

loading_history()
app.mainloop()

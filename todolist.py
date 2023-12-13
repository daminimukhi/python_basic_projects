import tkinter as tk
import winsound  # For Windows sound notifications

class ToDoListApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("400x300")

        # List to hold tasks
        self.tasks = []

        # Entry field to input new tasks
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack()

        # Button to add tasks
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        # Frame to contain tasks
        self.tasks_frame = tk.Frame(root)
        self.tasks_frame.pack()

        # List to hold Checkbuttons
        self.complete_buttons = []

        # Display initial tasks
        self.populate_tasks()

        # Button to exit the application
        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack()

    def add_task(self):
        # Function to add a task
        task = self.task_entry.get()
        if task:
            # Append the task to the tasks list
            self.tasks.append({"task": task, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.play_notification()
            self.populate_tasks()

    def remove_task(self, index):
        # Function to remove a task
        del self.tasks[index]
        self.populate_tasks()

    def mark_task_complete(self, index):
        # Function to toggle task completion status
        self.tasks[index]["completed"] = not self.tasks[index]["completed"]
        self.populate_tasks()

    def populate_tasks(self):
        # Function to populate tasks in the GUI
        for widget in self.tasks_frame.winfo_children():
            # Clear the existing tasks
            widget.destroy()

        for i, task in enumerate(self.tasks):
            task_text = task["task"]
            completed = task["completed"]

            task_frame = tk.Frame(self.tasks_frame)
            task_frame.pack(anchor="w")

            check_button_var = tk.BooleanVar(value=completed)
            check_button = tk.Checkbutton(task_frame, command=lambda idx=i: self.mark_task_complete(idx), var=check_button_var)
            check_button.pack(side="left")

            if completed:
                label = tk.Label(task_frame, text=task_text, fg="grey")
                label.pack(side="left")
            else:
                label = tk.Label(task_frame, text=task_text)
                label.pack(side="left")

            remove_button = tk.Button(task_frame, text="Remove", command=lambda idx=i: self.remove_task(idx))
            remove_button.pack(side="left")

            self.complete_buttons.append(check_button)

    def play_notification(self):
        # Function to play a notification sound
        winsound.Beep(500, 200)

def main():
    # Create and run the application
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

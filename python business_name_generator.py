import tkinter as tk
import random

# Predefined list of keywords for business names
keywords = ["Tech", "Solutions", "Innovations", "Digital", "Services", "Creative", "Group", "Global", "Network", "Smart"]

def generate_business_names(keyword, num_names=5):
    return [f"{keyword} {random.choice(keywords)}" for _ in range(num_names)]

def generate_names():
    keyword = keyword_entry.get()
    if keyword:
        name_suggestions = generate_business_names(keyword)
        suggestion_label.config(text='\n'.join(name_suggestions))
    else:
        suggestion_label.config(text="Please enter a keyword to generate business name suggestions.")

# Create the main window
root = tk.Tk()
root.title("Business Name Generator")

# Styling
root.geometry("400x300")
root.configure(bg="#f2f2f2")

# Create GUI components with custom styling
label = tk.Label(root, text="Enter a keyword:", bg="#f2f2f2", font=("Helvetica", 14))
keyword_entry = tk.Entry(root, font=("Helvetica", 12))
generate_button = tk.Button(root, text="Generate Names", command=generate_names, font=("Helvetica", 12), bg="#007acc", fg="white")
suggestion_label = tk.Label(root, text="", bg="#f2f2f2", font=("Helvetica", 12))

# Pack GUI components
label.pack(pady=10)
keyword_entry.pack(pady=10, padx=10, ipadx=5, ipady=5, fill=tk.X)
generate_button.pack(pady=10)
suggestion_label.pack(pady=10)

# Start the main event loop
root.mainloop()

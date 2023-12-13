import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate_text():
    # Retrieve the input text and destination language code
    input_text = input_entry.get()
    dest_language = lang_entry.get()

    # Translate the input text to the destination language
    translator = Translator()
    translated_text = translator.translate(input_text, dest=dest_language).text

    # Clear previous output, insert translated text into output entry
    output_entry.delete(0, tk.END)  # Clear any previous text
    output_entry.insert(tk.END, translated_text)

# Creating the main window
root = tk.Tk()
root.title("Language Translator")

# Creating a style for the labels and buttons
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

# Frame to hold the input elements
input_frame = ttk.Frame(root)
input_frame.pack(padx=20, pady=10)

# Label and entry for input text
input_label = ttk.Label(input_frame, text="Enter Text to Translate:")
input_label.grid(row=0, column=0, padx=5, pady=5)

input_entry = ttk.Entry(input_frame, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)

# Label and entry for destination language code
lang_label = ttk.Label(input_frame, text="Enter Destination Language Code (e.g., 'fr' for French):")
lang_label.grid(row=1, column=0, padx=5, pady=5)

lang_entry = ttk.Entry(input_frame, width=50)
lang_entry.grid(row=1, column=1, padx=5, pady=5)

# Button to trigger translation
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.pack(padx=20, pady=10)

# Frame to hold the output elements
output_frame = ttk.Frame(root)
output_frame.pack(padx=20, pady=10)

# Label for displaying translated text
output_label = ttk.Label(output_frame, text="Translated Text:")
output_label.grid(row=0, column=0, padx=5, pady=5)

# Entry field to display translated text
output_entry = ttk.Entry(output_frame, width=50)
output_entry.grid(row=0, column=1, padx=5, pady=5)

# Start the main loop
root.mainloop()

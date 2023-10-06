import tkinter as tk
import requests

# Define a dictionary of hardcoded conversion rates (for demonstration purposes)
conversion_rates = {
    "USD": 0.0063,  # 1 PKR to USD
    "EUR": 0.0053,  # 1 PKR to EUR
    "GBP": 0.0045,  # 1 PKR to GBP
    # Add more currencies here
}

# Function to perform currency conversion
def convert_currency():
    amount = float(entry_amount.get())
    from_currency = "PKR"  # Convert from Pakistani Rupees
    to_currency = combo_to_currency.get()

    result = amount * (conversion_rates[to_currency])
    label_result.config(text=f"Result: {result:.2f} {to_currency}")

# Create the main window
root = tk.Tk()
root.title("PKR to All Currencies Converter")

# Create GUI elements
label_amount = tk.Label(root, text="Amount (PKR):")
entry_amount = tk.Entry(root)
label_to_currency = tk.Label(root, text="To Currency:")
combo_to_currency = tk.StringVar()
combo_to_currency.set("USD")
menu_to_currency = tk.OptionMenu(root, combo_to_currency, *conversion_rates.keys())
button_convert = tk.Button(root, text="Convert", command=convert_currency)
label_result = tk.Label(root, text="Result:")

# Arrange GUI elements using the grid layout
label_amount.grid(row=0, column=0)
entry_amount.grid(row=0, column=1)
label_to_currency.grid(row=1, column=0)
menu_to_currency.grid(row=1, column=1)
button_convert.grid(row=2, columnspan=2)
label_result.grid(row=3, columnspan=2)

# Start the Tkinter main loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine")
        self.root.geometry("400x300")
        
        self.balance = 1000
        
        self.label = tk.Label(root, text="Welcome to the ATM Machine", font=("Helvetica", 14))
        self.label.pack(pady=20)
        
        self.balance_label = tk.Label(root, text=f"Balance: ${self.balance}", font=("Helvetica", 12))
        self.balance_label.pack()
        
        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw, font=("Helvetica", 12))
        self.withdraw_button.pack(pady=10)
        
        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit, font=("Helvetica", 12))
        self.deposit_button.pack(pady=10)
        
        self.quit_button = tk.Button(root, text="Quit", command=root.destroy, font=("Helvetica", 12), bg="red", fg="white")
        self.quit_button.pack(pady=10)

    def withdraw(self):
        amount = float(askstring("Withdraw", "Enter the amount to withdraw:"))
        if amount <= self.balance:
            self.balance -= amount
            self.balance_label.config(text=f"Balance: ${self.balance}")
            messagebox.showinfo("Success", f"Withdrew ${amount}")
        else:
            messagebox.showerror("Error", "Insufficient balance!")

    def deposit(self):
        amount = float(askstring("Deposit", "Enter the amount to deposit:"))
        if amount > 0:
            self.balance += amount
            self.balance_label.config(text=f"Balance: ${self.balance}")
            messagebox.showinfo("Success", f"Deposited ${amount}")
        else:
            messagebox.showerror("Error", "Invalid amount!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ATM(root)
    root.mainloop()

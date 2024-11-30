import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Global list to store transactions
transactions = []

# Function to add a transaction
def add_transaction():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        date = date_entry.get()

        # Validate input
        if not category or not date:
            raise ValueError("Category and Date cannot be empty!")
        
        # Append transaction to the global list
        transactions.append({"amount": amount, "category": category, "date": date})
        update_balance()
        update_transaction_list()
        update_pie_chart()
        clear_entries()
        messagebox.showinfo("Success", "Transaction added successfully!")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid Input: {e}")

# Function to clear input fields
def clear_entries():
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

# Function to update balance display
def update_balance():
    balance = sum(tx["amount"] for tx in transactions)
    balance_label.config(text=f"Account Balance: ${balance:.2f}")

# Function to update the transaction list display
def update_transaction_list():
    for row in transaction_tree.get_children():
        transaction_tree.delete(row)
    
    for i, tx in enumerate(transactions):
        transaction_tree.insert("", "end", iid=i, values=(tx["amount"], tx["category"], tx["date"]))

# Function to delete a transaction
def delete_transaction():
    selected_item = transaction_tree.selection()
    if selected_item:
        index = int(selected_item[0])
        transactions.pop(index)
        update_balance()
        update_transaction_list()
        update_pie_chart()
        messagebox.showinfo("Success", "Transaction deleted successfully!")
    else:
        messagebox.showerror("Error", "Please select a transaction to delete!")

# Function to update the pie chart
def update_pie_chart():
    # Clear existing chart
    pie_axes.clear()

    if transactions:
        # Group transactions by category
        category_totals = {}
        for tx in transactions:
            category_totals[tx["category"]] = category_totals.get(tx["category"], 0) + tx["amount"]
        
        # Prepare data for the pie chart
        labels = list(category_totals.keys())
        sizes = list(category_totals.values())
        colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c44e52", "#4c72b0", "#55a868"]

        # Plot the pie chart
        pie_axes.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        pie_axes.set_title("Spending by Category", fontsize=14, color="#333333")
    
    # Refresh the canvas
    pie_canvas.draw()

# Main Tkinter Window
root = tk.Tk()
root.title("Personal Finance Manager")
root.geometry("1000x700")
root.configure(bg="white")  # Set white background

# Header Section
header_label = tk.Label(root, text="Personal Financial Analysis", font=("Helvetica", 20, "bold"), bg="white", fg="#333333")
header_label.pack(fill="x", pady=10)

# Left Section: Account Balance and Pie Chart
left_frame = tk.Frame(root, bg="white", padx=10, pady=10)
left_frame.pack(side="left", fill="both", expand=True)

# Account Balance
balance_label = tk.Label(left_frame, text="Account Balance: $0.00", font=("Helvetica", 16), fg="#4c72b0", bg="white")
balance_label.pack(pady=10)

# Pie Chart
fig = Figure(figsize=(4, 4), dpi=100)
pie_axes = fig.add_subplot(111)
pie_canvas = FigureCanvasTkAgg(fig, left_frame)
pie_canvas.get_tk_widget().pack()

# Right Section: Inputs and Transaction History
right_frame = tk.Frame(root, bg="white", padx=10, pady=10)
right_frame.pack(side="right", fill="both", expand=True)

# Inputs Section
input_frame = tk.Frame(right_frame, bg="white")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Amount ($):", bg="white", fg="#333333").grid(row=0, column=0, padx=5, pady=5)
amount_entry = tk.Entry(input_frame)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Category:", bg="white", fg="#333333").grid(row=1, column=0, padx=5, pady=5)
category_entry = tk.Entry(input_frame)
category_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Date (YYYY-MM-DD):", bg="white", fg="#333333").grid(row=2, column=0, padx=5, pady=5)
date_entry = tk.Entry(input_frame)
date_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add", command=add_transaction, bg="#4caf50", fg="white")
add_button.grid(row=3, column=0, columnspan=2, pady=10)

delete_button = tk.Button(input_frame, text="Delete", command=delete_transaction, bg="#f44336", fg="white")
delete_button.grid(row=4, column=0, columnspan=2, pady=10)

# Transaction History
transaction_tree = ttk.Treeview(right_frame, columns=("Amount", "Category", "Date"), show="headings")
transaction_tree.heading("Amount", text="Amount ($)")
transaction_tree.heading("Category", text="Category")
transaction_tree.heading("Date", text="Date")
transaction_tree.pack(fill="both", expand=True)

# Run the Tkinter application
root.mainloop()

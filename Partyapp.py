import tkinter as tk
from tkinter import messagebox

#Creating the main window
root = tk.Tk()
root.title("Party Management App")
root.geometry("1000x1000")
root.configure(bg="grey")

#centering of it
frame = tk.Frame(root, bg="grey")
frame.pack()
frame.place(rely = 0.5, relx = 0.5, anchor = "center")

#Quantity
MAX_QUANTITY = 500
MIN_QUANTITY = 1
LOG_FILE = "returns.txt"

#Rentable Items
items = {
    "Chairs": 7,
    "Tables": 15,
    "Gazebo": 250,
    "Tableware": 20,
    "Sound System": 75
}

selected_items = tk.StringVar(value=list(items.keys())[0])

#Layout
main_frame = tk.Frame(root, bg="grey", padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

form_frame = tk.LabelFrame(main_frame, text="New Hires", bg="grey", padx=15, pady=15)
form_frame.pack(fill="x", pady=(0, 15))

list_frame = tk.LabelFrame(main_frame, text="Currently Hired Items", bg="grey", padx=15, pady=15)
list_frame.pack(fill="both", expand=True)

#Gridding the form frame
form_frame.columnconfigure(1, weight=1)


tk.Label(form_frame, text="Name: ", bg="grey").grid(row=0, column=0, sticky="e", pady=5)
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, sticky="ew", padx=5,pady=5)

tk.Label(form_frame, text="Receipt Number: ", bg="grey").grid(row=1, column=0, sticky="e",padx=5, pady=5)
receipt_entry = tk.Entry(form_frame)
receipt_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

tk.Label(form_frame, text="Select Item: ", bg="grey").grid(row=2, column=0, sticky="e", pady=5)
item_menu = tk.OptionMenu(form_frame, selected_items, *items.keys())
item_menu.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

tk.Label(form_frame, text="Quantity (1-500): ", bg="grey").grid(row=3, column=0, sticky="e", pady=5)
quantity_entry = tk.Entry(form_frame)
quantity_entry.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

#Listbox
hire_listbox = tk.Listbox(list_frame, width=120)
hire_listbox.pack()

#List holding data
names = []
receipts = []
items_hired = []
quantities = []
items_price = []
hires = []

#Functions
def validate_quantity(quantity):
    try:
        quantity = int(quantity)
        return MIN_QUANTITY <= quantity <= MAX_QUANTITY
    except ValueError:
        return False
    
def validate_receipt(receipt):
    return receipt.isdigit() and len(receipt) == 6

def refresh_list():
    hire_listbox.delete(0, tk.END)
    for hire in hires:
        line = f"name: {hire['name']} | receipt: {hire['receipt']} | item: {hire['item']} |quantity: {hire['quantity']} |price: ${hire['price']}"
        hire_listbox.insert(tk.END, line)

def clear_entries():
    name_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

def add_hire():
    name = name_entry.get()
    receipt = receipt_entry.get()
    item = selected_items.get()
    quantity = quantity_entry.get()

    if not name or not receipt or not quantity:
        tk.messagebox.showerror("Error", "All fields must be filled.")
        return

    if not validate_receipt(receipt):
        tk.messagebox.showerror("Error", "Receipt number must be a 6-digit number.")
        return

    if not validate_quantity(quantity):
        tk.messagebox.showerror("Error", f"Quantity must be between {MIN_QUANTITY} and {MAX_QUANTITY}.")
        return

    quantity = int(quantity)
    price = items[item] * quantity

    hires.append({
        "name": name,
        "receipt": receipt,
        "item": item,
        "quantity": quantity,
        "price": price
    })

    refresh_list()
    clear_entries()
add_button = tk.Button(form_frame, text="Add Hire", command=add_hire)
add_button.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

#Returning Items
def return_item():
    selected = hire_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select an item to return.")
        return
    
    index = selected[0]
    with open(LOG_FILE, "a") as f:
        f.write(f"name: {hires[index]['name']} | receipt: {hires[index]['receipt']} | item: {hires[index]['item']} |quantity: {hires[index]['quantity']} |price: ${hires[index]['price']}\n")

    hires.pop(index)
    refresh_list()
    messagebox.showinfo("Item successfully returned.")

tk.Button(list_frame, text="Return Item", command=return_item).pack(pady=5)

#Make code run
root.mainloop()
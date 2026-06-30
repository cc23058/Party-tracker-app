import tkinter as tk

#Creating the main window
root = tk.Tk()
root.title("Party Management App")
root.geometry("1000x500")

#centering of it
frame = tk.Frame(root)
frame.pack()
frame.place(rely = 0.5, relx = 0.5, anchor = "center")
#The Quantity of items
quantity_max = 500
quantity_min = 1
tk.Entry(frame, text="quantity").grid(row=2, column=3, padx=10, pady=5, sticky="e")

#Selection of Item & pricing
tk.Label(frame, text="Items:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
items = ["Balloons", "Party Hats", "Confetti", "Music", "Food", "Drinks", "DJ", "Photographer"]
items_price = [1.00, 2.50, 0.50, 100.00, 200.00, 150.00, 300.00, 250.00]
selected_item = tk.StringVar(value=items[0])
item_menu = tk.OptionMenu(frame, selected_item, *items)
item_menu.grid(row=1, column=1, padx=10, pady=5)


#make the code run
root.mainloop()
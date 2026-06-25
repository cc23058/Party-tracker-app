import tkinter as tk

#Creating the main window
root = tk.Tk()
root.title("Party Management App")
root.geometry("1000x500")

#centering of it
frame = tk.Frame(root)
frame.pack()
frame.place(rely = 0.5, relx = 0.5, anchor = "center")

#Creating menu of party items
#Selection of Item & pricing
tk.Label(frame, text="Item").grid(row=1, column=0, padx=10, pady=5, sticky="e")
items = ["Balloons", 25, "Party Hats", 12, "Confetti", 15,"Music", 5, "Food", 20,"Drinks", 15]
selected_item = tk.StringVar(value=items[0])
item_menu = tk.OptionMenu(frame, selected_item, *items)
item_menu.grid(row=3, column=1, padx=10, pady=5)


#make the code run
root.mainloop()
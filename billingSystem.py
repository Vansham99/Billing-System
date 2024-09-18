# Import tkinter module for GUI
from tkinter import *

# Create a window object
window = Tk()

# Set the window title and size
window.title("Billing System")
window.geometry("500x400")

# Create a label for the title
title_label = Label(window, text="Billing System", font="Arial 20 bold")
title_label.pack()

# Create a frame for the input fields
input_frame = Frame(window)
input_frame.pack()

# Create labels and entry boxes for the product name and price
product_label = Label(input_frame, text="Product Name:", font="Arial 15")
product_label.grid(row=0, column=0, padx=10, pady=10)
product_entry = Entry(input_frame, font="Arial 15")
product_entry.grid(row=0, column=1, padx=10, pady=10)

price_label = Label(input_frame, text="Price:", font="Arial 15")
price_label.grid(row=1, column=0, padx=10, pady=10)
price_entry = Entry(input_frame, font="Arial 15")
price_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a button to add the product to the bill
add_button = Button(input_frame, text="Add", font="Arial 15", command=lambda: add_product())
add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create a listbox to display the bill items
bill_list = Listbox(window, font="Arial 15", width=40, height=10)
bill_list.pack()

# Create a label to display the total amount
total_label = Label(window, text="Total: 0", font="Arial 20 bold")
total_label.pack()


# Define a function to add a product to the bill
def add_product():
    # Get the product name and price from the entry boxes
    product = product_entry.get()
    price = price_entry.get()

    # Check if the product name and price are not empty
    if product and price:
        # Try to convert the price to a float value
        try:
            price = float(price)
        except ValueError:
            # If the price is not a valid number, show an error message
            bill_list.insert(END, "Invalid price")
            return

        # Format the product and price as a string
        item = f"{product}: {price}"

        # Add the item to the bill list
        bill_list.insert(END, item)

        # Clear the entry boxes
        product_entry.delete(0, END)
        price_entry.delete(0, END)

        # Update the total amount
        update_total()

    else:
        # If the product name or price is empty, show an error message
        bill_list.insert(END, "Please enter product name and price")


# Define a function to update the total amount
def update_total():
    # Initialize the total amount to zero
    total = 0

    # Loop through the bill items
    for i in range(bill_list.size()):
        # Get the item from the bill list
        item = bill_list.get(i)

        # Split the item by colon
        parts = item.split(":")

        # Check if the item has two parts
        if len(parts) == 2:
            # Try to convert the second part to a float value
            try:
                price = float(parts[1])
            except ValueError:
                # If the price is not a valid number, skip this item
                continue

            # Add the price to the total amount
            total += price

    # Format the total amount as a string
    total = f"Total: {total}"

    # Update the total label
    total_label.config(text=total)


# Start the main loop of the window
window.mainloop()



import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to restock a product
def restock_product():
    try:
        # Get inputs from the user
        product_id = entry_product_id.get()
        quantity = entry_quantity.get()

        # Validate inputs
        if not product_id.isdigit() or not quantity.isdigit():
            messagebox.showerror("Invalid Input", "Please enter valid numbers for Product ID and Quantity.")
            return

        # Connect to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="asdfghjkl",  # Replace with your MySQL password
            database="MeltasticStore"  # Replace with your database name
        )
        cursor = connection.cursor()

        # Update the stock in the Product table
        query = "UPDATE Product SET Stock = Stock + %s WHERE idProduct = %s"
        cursor.execute(query, (int(quantity), int(product_id)))

        # Commit the changes and provide feedback
        connection.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", f"Restocked Product ID {product_id} with {quantity} units.")
        else:
            messagebox.showwarning("Warning", f"No product found with ID {product_id}.")

    except mysql.connector.Error as error:
        messagebox.showerror("Database Error", f"Error: {error}")

    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Create the Tkinter GUI
root = tk.Tk()
root.title("Restock Products")

# Labels and Entry Widgets
label_product_id = tk.Label(root, text="Product ID:")
label_product_id.grid(row=0, column=0, padx=10, pady=10)

entry_product_id = tk.Entry(root)
entry_product_id.grid(row=0, column=1, padx=10, pady=10)

label_quantity = tk.Label(root, text="Quantity:")
label_quantity.grid(row=1, column=0, padx=10, pady=10)

entry_quantity = tk.Entry(root)
entry_quantity.grid(row=1, column=1, padx=10, pady=10)

# Restock Button
restock_button = tk.Button(root, text="Restock", command=restock_product)
restock_button.grid(row=2, column=0, columnspan=2, pady=20)

# Start the Tkinter main loop
root.mainloop()

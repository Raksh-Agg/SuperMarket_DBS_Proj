import tkinter as tk
from tkinter import ttk
import Processes
from tkinter import messagebox
import SalesPage


class AddSalesPage(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Sales Page")
        self.master.geometry("1920x1080")
        self.tempCursorInit = tempCursorInit

        # Create the frames
        self.top_frame = tk.Frame(self.master)
        self.middle_frame = tk.Frame(self.master)
        self.bottom_frame = tk.Frame(self.master)

        # Place the frames in the window
        self.top_frame.pack(side="top")
        self.middle_frame.pack(side="top", fill="both", expand=True)
        self.bottom_frame.pack(side="bottom", fill="x")

        # Create the widgets for the top frame
        self.back_button = tk.Button(
            self.top_frame, text="Back", command=self.master.destroy)
        self.back_button.pack(side=tk.LEFT)

        self.emp_id_label = tk.Label(self.top_frame, text="Employee ID:")
        self.emp_id_label.pack(side="left")
        self.emp_id_entry = tk.Entry(self.top_frame, validate="key")
        self.emp_id_entry.config(validatecommand=(
            self.emp_id_entry.register(self.is_numeric_input), '%P'))
        self.emp_id_entry.pack(side="left", padx=10)

        self.Cust_id_label = tk.Label(self.top_frame, text="Customer ID:")
        self.Cust_id_label.pack(side="left")
        self.Cust_id_entry = tk.Entry(self.top_frame, validate="key")
        self.Cust_id_entry.config(validatecommand=(
            self.Cust_id_entry.register(self.is_numeric_input), '%P'))
        self.Cust_id_entry.pack(side="left", padx=10)

        self.product_id_label = tk.Label(self.top_frame, text="Product ID:")
        self.product_id_label.pack(side="left")
        self.product_id_entry = tk.Entry(self.top_frame, validate="key")
        self.product_id_entry.config(validatecommand=(
            self.product_id_entry.register(self.is_numeric_input), '%P'))
        self.product_id_entry.pack(side="left", padx=10)

        self.quantity_label = tk.Label(self.top_frame, text="Quantity:")
        self.quantity_label.pack(side="left")
        self.quantity_entry = tk.Entry(self.top_frame, validate="key")
        self.quantity_entry.config(validatecommand=(
            self.quantity_entry.register(self.is_numeric_input), '%P'))
        self.quantity_entry.pack(side="left", padx=10)

        # Create the widgets for the middle frame
        self.tree = ttk.Treeview(
            self.middle_frame, columns=("Product ID", "Quantity"))
        self.tree.heading("#0", text="")
        self.tree.heading("Product ID", text="Product ID")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.pack(side="left", fill="both", expand=True)
        self.scrollbar = ttk.Scrollbar(
            self.middle_frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Create the widgets for the bottom frame
        self.add_button = tk.Button(
            self.bottom_frame, text="Add to Current Sale", command=self.add_to_Sale)
        self.add_button.pack(side="left", padx=10, pady=10)
        self.end_button = tk.Button(
            self.bottom_frame, text="End Sale", command=self.end_Sale)
        self.end_button.pack(side="right", padx=10, pady=10)

    def add_to_Sale(self):
        # Get the product ID and quantity from the entries
        product_id = self.product_id_entry.get()
        quantity = self.quantity_entry.get()

        # Add the product ID and quantity to the treeview
        self.tree.insert("", "end", text="", values=(product_id, quantity))

        # Clear the entries
        self.product_id_entry.delete(0, "end")
        self.quantity_entry.delete(0, "end")

    def end_Sale(self):
        # Get the data from the treeview
        data = []
        for child in self.tree.get_children():
            data.append((self.tree.item(child)["values"]))

        Emp_ID = self.emp_id_entry.get()
        Cust_ID = self.Cust_id_entry.get()
        Processes.Cursor_Init.addSale(
            self.tempCursorInit, Emp_ID, Cust_ID, data)
        messagebox.showinfo("Success", "Sale Added Successfully")
        self.quantity_entry.delete(0, tk.END)
        self.product_id_entry.delete(0, tk.END)
        self.master.destroy()


    def is_numeric_input(self, value):
        if value:
            try:
                int(value)
            except ValueError:
                return False
        return True


if __name__ == "__main__":
    root = tk.Tk()
    app = AddSalesPage(master=root)
    app.mainloop()

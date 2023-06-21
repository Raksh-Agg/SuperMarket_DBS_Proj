import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
import Processes


class AddProductPage(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Add Product")
        self.tempCursorInit = tempCursorInit

        self.back_button = tk.Button(
            self, text="Back", command=self.master.withdraw)
        self.back_button.grid(row=0, column=0, padx=5, pady=5)

        self.product_name_label = tk.Label(
            self, text="Product Name", padx=10, pady=10)
        self.product_name_label.grid(row=1, column=0)
        self.product_name_entry = tk.Entry(self)
        self.product_name_entry.grid(row=1, column=1)

        self.price_label = tk.Label(self, text="Price", padx=10, pady=10)
        self.price_label.grid(row=2, column=0)
        vcmd = self.master.register(self.validate_price)
        self.price_entry = tk.Entry(
            self, validate="key", validatecommand=(vcmd, '%P'))
        self.price_entry.grid(row=2, column=1)

        self.submit_button = tk.Button(
            self, text="Submit", command=self.submit)
        self.submit_button.grid(row=3, column=1)

        self.pack()

    def validate_price(self, new_value):
        if not new_value:
            return True
        try:
            float(new_value)
            return True
        except ValueError:
            return False

    def submit(self):
        Prod_Name = self.product_name_entry.get()
        Prod_Price = (self.price_entry.get())
        Processes.Cursor_Init.insertProduct(
            self.tempCursorInit, Prod_Name, Prod_Price)
        messagebox.showinfo("Success", "Product Added Successfully")
        self.price_entry.delete(0, tk.END)
        self.product_name_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AddProductPage(master=root)
    app.mainloop()

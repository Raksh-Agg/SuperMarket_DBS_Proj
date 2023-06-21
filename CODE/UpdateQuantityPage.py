import tkinter as tk
from tkinter import ttk
import Processes
from tkinter import messagebox


class UpdateQuantityPage(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Update Quantity")
        self.tempCursorInit = tempCursorInit

        self.back_button = tk.Button(
            self.master, text="Back", command=self.master.destroy, anchor='w')
        self.back_button.grid(row=0, column=0, padx=5, pady=5)

        self.product_id_label = tk.Label(self.master, text="Product ID")
        self.product_id_label.grid(row=1, column=0, padx=10, pady=10)

        self.product_id_entry = tk.Entry(self.master)
        self.product_id_entry.grid(row=1, column=1, padx=10, pady=10)
        self.product_id_entry.config(validatecommand=(
            self.product_id_entry.register(self.is_numeric_input), '%P'))

        self.quantity_label = tk.Label(self.master, text="Quantity in stock")
        self.quantity_label.grid(row=2, column=0, padx=10, pady=10)

        self.quantity_entry = tk.Entry(self.master)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=10)
        self.quantity_entry.config(validatecommand=(
            self.quantity_entry.register(self.is_numeric_input), '%P'))

        self.update_button = tk.Button(
            self.master, text="Update", command=self.update)
        self.update_button.grid(
            row=5, column=0, columnspan=2, padx=10, pady=10)

    def is_numeric_input(self, value):
        # Returns True if the value is numeric, False otherwise
        return str(value).isdigit()

    def update(self):
        prodid = self.product_id_entry.get()
        qty = self.quantity_entry.get()
        if self.is_numeric_input(prodid) and self.is_numeric_input(qty):
            Processes.Cursor_Init.updateQuantity(
                self.tempCursorInit, qty, prodid)
            messagebox.showinfo("Success", "Quantity has been updated")
            self.product_id_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Values Entered should be Numeric")


if __name__ == "__main__":
    root = tk.Tk()
    app = UpdateQuantityPage(master=root)
    app.mainloop()

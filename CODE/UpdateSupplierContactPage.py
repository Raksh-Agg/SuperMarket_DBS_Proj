import tkinter as tk
from tkinter import ttk
import AddProductPage
from tkinter import messagebox
import Processes


class UpdateSupplierContactPage(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Update Supplier Contact Information")
        # self.master.geometry("1920x1080")
        self.tempCursorInit = tempCursorInit

        self.back_button = tk.Button(
            self.master, text="Back", command=self.master.destroy, anchor='w')
        self.back_button.grid(row=0, column=0, padx=5, pady=5)

        self.supplier_id_label = tk.Label(self.master, text="Supplier ID")
        self.supplier_id_label.grid(row=1, column=0, padx=10, pady=10)

        self.supplier_id_entry = tk.Entry(self.master)
        self.supplier_id_entry.grid(row=1, column=1, padx=10, pady=10)
        self.supplier_id_entry.config(validatecommand=(
            self.supplier_id_entry.register(self.is_numeric_input), '%P'))

        self.phone_number_label = tk.Label(self.master, text="Phone Number")
        self.phone_number_label.grid(row=2, column=0, padx=10, pady=10)

        self.phone_number_entry = tk.Entry(self.master)
        self.phone_number_entry.grid(row=2, column=1, padx=10, pady=10)

        self.update_button = tk.Button(
            self.master, text="Update", command=self.update)
        self.update_button.grid(
            row=5, column=0, columnspan=2, padx=10, pady=10)

    def update(self):
        supp_id = self.supplier_id_entry.get()
        phone = self.phone_number_entry.get()
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror(
                "Error", "Invalid Phone Number. Please enter a valid 10 digit phone number")
        elif not supp_id.isdigit():
            messagebox.showerror("Error", "Please Enter Valid Supplier ID")
        else:
            Processes.Cursor_Init.updateSupplierContact(
                self.tempCursorInit, phone, supp_id)
            self.master.withdraw()

    def is_numeric_input(self, value):
        # Returns True if the value is numeric, False otherwise
        return str(value).isdigit()


if __name__ == "__main__":
    root = tk.Tk()
    app = UpdateSupplierContactPage(master=root)
    app.mainloop()

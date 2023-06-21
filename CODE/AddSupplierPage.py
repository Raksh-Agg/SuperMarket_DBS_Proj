import tkinter as tk
from tkinter import messagebox
import mysql.connector
import Processes


class AddSupplier(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Add Supplier")
        self.master.geometry("1920x1080")
        self.tempCursorInit = tempCursorInit

        self.back_button = tk.Button(
            self.master, text="Back", command=self.master.destroy, anchor='w')
        self.back_button.grid(row=0, column=0, padx=5, pady=5)

        self.first_name_label = tk.Label(self.master, text="First Name")
        self.first_name_label.grid(row=1, column=0, padx=10, pady=10)

        self.first_name_entry = tk.Entry(self.master)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.second_name_label = tk.Label(self.master, text="Second Name")
        self.second_name_label.grid(row=2, column=0, padx=10, pady=10)

        self.second_name_entry = tk.Entry(self.master)
        self.second_name_entry.grid(row=2, column=1, padx=10, pady=10)

        self.phone_label = tk.Label(self.master, text="Phone Number")
        self.phone_label.grid(row=3, column=0, padx=10, pady=10)

        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=3, column=1, padx=10, pady=10)

        self.address_line_one_label = tk.Label(
            self.master, text="Address (Line 1)")
        self.address_line_one_label.grid(row=4, column=0, padx=10, pady=10)

        self.address_line_one_entry = tk.Entry(self.master)
        self.address_line_one_entry.grid(row=4, column=1, padx=10, pady=10)

        self.address_line_two_label = tk.Label(
            self.master, text="Address (Line 2)")
        self.address_line_two_label.grid(row=5, column=0, padx=10, pady=10)

        self.address_line_two_entry = tk.Entry(self.master)
        self.address_line_two_entry.grid(row=5, column=1, padx=10, pady=10)

        self.pincode_label = tk.Label(self.master, text="Pincode")
        self.pincode_label.grid(row=6, column=0, padx=10, pady=10)

        self.pincode_entry = tk.Entry(self.master)
        self.pincode_entry.grid(row=6, column=1, padx=10, pady=10)

        self.submit_button = tk.Button(
            self.master, text="Submit", command=self.submit_supplier)
        self.submit_button.grid(
            row=7, column=0, columnspan=2, padx=10, pady=10)

    def submit_supplier(self):
        first_name = self.first_name_entry.get()
        second_name = self.second_name_entry.get()
        phone = self.phone_entry.get()
        address_one = self.address_line_one_entry.get()
        address_two = self.address_line_two_entry.get()
        pincode = self.pincode_entry.get()

        if not first_name or not second_name or not phone or not address_one or not address_two or not pincode:
            messagebox.showerror("Error", "All fields are required")
        elif not phone.isdigit() or len(phone) != 10:
            messagebox.showerror(
                "Error", "Invalid Phone Number. Please enter a valid 10 digit phone number")
        elif not pincode.isdigit() or len(pincode) != 6:
            messagebox.showerror(
                "Error", "Invalid Pincode. Please enter a valid 6 digit pincode")
        else:
            Processes.Cursor_Init.insertHuman(
                self.tempCursorInit, "Supplier", first_name, second_name, phone, address_one, address_two, pincode)
            messagebox.showinfo("Success", "Supplier Added Successfully")
            # clear all entry fields
            self.first_name_entry.delete(0, tk.END)
            self.second_name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.address_line_one_entry.delete(0, tk.END)
            self.address_line_two_entry.delete(0, tk.END)
            self.pincode_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AddSupplier(master=root)
    app.mainloop()

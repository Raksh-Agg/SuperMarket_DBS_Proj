import tkinter as tk
from tkinter import ttk
import AddProductPage
from tkinter import messagebox
import Processes


class DeleteSalePage(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Delete Sale")
        self.tempCursorInit = tempCursorInit

        self.back_button = tk.Button(
            self.master, text="Back", command=self.master.withdraw, anchor='w')
        self.back_button.grid(row=0, column=0, padx=5, pady=5)

        self.sale_id_label = tk.Label(self.master, text="Sale ID")
        self.sale_id_label.grid(row=1, column=0, padx=10, pady=10)

        self.sale_id_entry = tk.Entry(self.master)
        self.sale_id_entry.grid(row=1, column=1, padx=10, pady=10)
        self.sale_id_entry.config(validatecommand=(
            self.sale_id_entry.register(self.is_numeric_input), '%P'))

        self.delete_button = tk.Button(
            self.master, text="Delete", command=self.delete)
        self.delete_button.grid(
            row=5, column=0, columnspan=2, padx=10, pady=10)

    def delete(self):
        sale_id = self.sale_id_entry.get()
        Processes.Cursor_Init.deleteSale(self.tempCursorInit, sale_id)
        messagebox.showinfo("Success", "Sale has been Deleted")

    def is_numeric_input(self, value):
        # Returns True if the value is numeric, False otherwise
        return str(value).isdigit()


if __name__ == "__main__":
    root = tk.Tk()
    app = DeleteSalePage(master=root)
    app.mainloop()

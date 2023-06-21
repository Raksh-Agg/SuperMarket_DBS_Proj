import tkinter as tk
from tkinter import ttk
import AddSupplierPage
import mysql.connector
import Processes
import UpdateSupplierContactPage
import DashboardPage


class SupplierInfoPage(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Supplier Info")
        self.master.geometry("1920x1080")
        self.tempCursorInit = tempCursorInit

        # Top Frame
        self.top_frame = tk.Frame(self.master, padx=10, pady=10)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.back_button = tk.Button(
            self.top_frame, text="Back", command=self.go_back)
        self.back_button.grid(row=0, column=0, pady=5)

        self.search_id_label = tk.Label(
            self.top_frame, text="Search By Supplier ID:")
        self.search_id_label.grid(
            row=1, column=0, padx=5, pady=5)

        self.search_id_entry = tk.Entry(self.top_frame)
        self.search_id_entry.grid(
            row=1, column=1, padx=5, pady=5)

        self.search_id_button = tk.Button(
            self.top_frame, text="Submit", command=self.search_by_id)
        self.search_id_button.grid(
            row=1, column=3, padx=5, pady=5)

        self.search_name_label = tk.Label(
            self.top_frame, text="Search By Name:")
        self.search_name_label.grid(
            row=2, column=0, padx=5, pady=5)

        self.search_name_entry = tk.Entry(self.top_frame)
        self.search_name_entry.grid(
            row=2, column=1, padx=5, pady=5)

        self.search_name_button = tk.Button(
            self.top_frame, text="Submit", command=self.search_by_name)
        self.search_name_button.grid(
            row=2, column=3, padx=5, pady=5)

        self.sort_button = tk.Button(
            self.top_frame, text="Sort By Amount Earnt", command=self.sort_by_expenditure)
        self.sort_button.grid(row=3, column=0, padx=5, pady=5)

        self.add_button = tk.Button(
            self.top_frame, text="Update Contact Info", command=self.update_Supplier_Contact)
        self.add_button.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(
            self.top_frame, text="New Supplier", command=self.add_supplier)
        self.add_button.grid(row=4, column=0, padx=5, pady=5)

        # Bottom Frame
        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.treeview = ttk.Treeview(self.bottom_frame, columns=(
            "ID", "First_Name", "Second_Name", "Phone", "Amount_Earnt", "Address1", "Address2", "Pincode"), selectmode='browse')
        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.treeview.heading("#0", text="")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("First_Name", text="First Name")
        self.treeview.heading("Second_Name", text="SecondName")
        self.treeview.heading("Phone", text="Phone")
        self.treeview.heading("Amount_Earnt", text="Amount Earnt")
        self.treeview.heading("Address1", text="Address Line 1")
        self.treeview.heading("Address2", text="Address Line 2")
        self.treeview.heading("Pincode", text="PinCode")

        self.treeview.column("#0", stretch=tk.YES, width=0)
        self.treeview.column("ID", stretch=tk.YES, width=100)
        self.treeview.column("First_Name", stretch=tk.YES, width=200)
        self.treeview.column("Second_Name", stretch=tk.YES, width=200)
        self.treeview.column("Phone", stretch=tk.YES, width=150)
        self.treeview.column("Amount_Earnt", stretch=tk.YES, width=150)
        self.treeview.column("Address1", stretch=tk.YES, width=200)
        self.treeview.column("Address2", stretch=tk.YES, width=200)
        self.treeview.column("Pincode", stretch=tk.YES, width=200)

        self.treeview_scroll = ttk.Scrollbar(
            self.bottom_frame, orient=tk.VERTICAL, command=self.treeview.yview)
        self.treeview_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.treeview.configure(yscrollcommand=self.treeview_scroll.set)

        self.treeview.configure(yscrollcommand=self.treeview_scroll.set)
        allSupplierData = Processes.Cursor_Init.showAll(
            self.tempCursorInit, "Supplier")
        self.populate_listbox(allSupplierData)

    def go_back(self):
        DashBoard = tk.Toplevel(self.master)
        DashboardPage.Dashboard(DashBoard, self.tempCursorInit)
        self.master.withdraw()

    def populate_listbox(self, data):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        num = 0
        for item in data:
            self.treeview.insert(parent='', index=num, iid=num, values=(
                item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))
            num = num + 1

    def search_by_id(self):
        Supplier_id = (self.search_id_entry.get())
        if Supplier_id == '':
            self.populate_listbox(Processes.Cursor_Init.showAll(
                self.tempCursorInit, "Supplier"))
        else:
            Supplier_ID = (int)(Supplier_id)
            myResult = Processes.Cursor_Init.showBySearch(
                self.tempCursorInit, "Supplier", "Supplier_ID", Supplier_ID)
            self.populate_listbox(myResult)

    def search_by_name(self):
        Supplier_Name = self.search_name_entry.get()
        myResult = Processes.Cursor_Init.searchByName(
            self.tempCursorInit, "Supplier", Supplier_Name)
        self.populate_listbox(myResult)

    def sort_by_expenditure(self):
        data = []
        for child in self.treeview.get_children():
            row_data = []
            for column in self.treeview["columns"]:
                row_data.append(self.treeview.item(child)[
                                "values"][self.treeview["columns"].index(column)])
            data.append(row_data)
        sorted_list = sorted(data, key=lambda x: x[4], reverse=True)
        self.populate_listbox(sorted_list)

    def add_supplier(self):
        add_supplier_window = tk.Toplevel(self.master)
        AddSupplierPage.AddSupplier(add_supplier_window, self.tempCursorInit)

    def update_Supplier_Contact(self):
        Update = tk.Toplevel(self.master)
        UpdateSupplierContactPage.UpdateSupplierContactPage(
            Update, self.tempCursorInit)


if __name__ == "__main__":
    root = tk.Tk()
    app = SupplierInfoPage(master=root)
    app.mainloop()

import tkinter as tk
from tkinter import ttk
import AddCustomerPage
import mysql.connector
import Processes
import DashboardPage


class CustomerInfoPage(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Customer Info")
        self.master.geometry("1920x1080")
        self.tempCursorInit = tempCursorInit

        # Top Frame
        self.top_frame = tk.Frame(self.master, padx=10, pady=10)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.back_button = tk.Button(
            self.top_frame, text="Back", command=self.go_back)
        self.back_button.pack(side=tk.LEFT)

        self.search_id_label = tk.Label(
            self.top_frame, text="Search By Customer ID:")
        self.search_id_label.pack(side=tk.LEFT, padx=(50, 5))

        self.search_id_entry = tk.Entry(self.top_frame)
        self.search_id_entry.pack(side=tk.LEFT)

        self.search_id_button = tk.Button(
            self.top_frame, text="Submit", command=self.search_by_id)
        self.search_id_button.pack(side=tk.LEFT, padx=(5, 50))

        self.search_name_label = tk.Label(
            self.top_frame, text="Search By Name:")
        self.search_name_label.pack(side=tk.LEFT, padx=(50, 5))

        self.search_name_entry = tk.Entry(self.top_frame)
        self.search_name_entry.pack(side=tk.LEFT)

        self.search_name_button = tk.Button(
            self.top_frame, text="Submit", command=self.search_by_name)
        self.search_name_button.pack(side=tk.LEFT, padx=(5, 50))

        self.sort_button = tk.Button(
            self.top_frame, text="Sort By Total Expenditure", command=self.sort_by_expenditure)
        self.sort_button.pack(side=tk.LEFT)

        self.add_button = tk.Button(
            self.top_frame, text="Add New Customer", command=self.add_customer)
        self.add_button.pack(side=tk.LEFT)

        # Bottom Frame
        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.treeview = ttk.Treeview(self.bottom_frame, columns=(
            "ID", "First_Name", "Second_Name", "Phone", "Total Expenditure", "Address_Line_one", "Address_Line_two", "Pincode"), selectmode='browse')
        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.treeview.heading("#0", text="")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("First_Name", text="First_Name")
        self.treeview.heading("Second_Name", text="Second Name")
        self.treeview.heading("Phone", text="Phone")
        self.treeview.heading("Total Expenditure", text="Total Expenditure")
        self.treeview.heading("Address_Line_one", text="Address Line 1")
        self.treeview.heading("Address_Line_two", text="Address Line 2")
        self.treeview.heading("Pincode", text="PinCode")

        self.treeview.column("#0", stretch=tk.YES, width=0)
        self.treeview.column("ID", stretch=tk.YES, width=100)
        self.treeview.column("First_Name", stretch=tk.YES, width=200)
        self.treeview.column("Second_Name", stretch=tk.YES, width=200)
        self.treeview.column("Phone", stretch=tk.YES, width=150)
        self.treeview.column("Total Expenditure", stretch=tk.YES, width=150)
        self.treeview.column("Address_Line_one", stretch=tk.YES, width=200)
        self.treeview.column("Address_Line_two", stretch=tk.YES, width=200)
        self.treeview.column("Pincode", stretch=tk.YES, width=150)

        self.treeview_scroll = ttk.Scrollbar(
            self.bottom_frame, orient=tk.VERTICAL, command=self.treeview.yview)
        self.treeview_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.treeview.configure(yscrollcommand=self.treeview_scroll.set)
        allCustomerData = Processes.Cursor_Init.showAll(
            self.tempCursorInit, "Customer")
        self.populate_listbox(allCustomerData)

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
        Cust_ID = (self.search_id_entry.get())
        if Cust_ID == '':
            self.populate_listbox(Processes.Cursor_Init.showAll(
                self.tempCursorInit, "Customer"))
        else:
            myResult = Processes.Cursor_Init.showBySearch(
                self.tempCursorInit, "Customer", "Cust_ID", Cust_ID)
            self.populate_listbox(myResult)

    def search_by_name(self):
        Cust_Name = self.search_name_entry.get()
        myResult = Processes.Cursor_Init.searchByName(
            self.tempCursorInit, "Customer", Cust_Name)
        self.populate_listbox(myResult)

    def sort_by_expenditure(self):
        data = []
        for child in self.treeview.get_children():
            row_data = []
            for column in self.treeview["columns"]:
                row_data.append(self.treeview.item(child)[
                                "values"][self.treeview["columns"].index(column)])
            data.append(row_data)
        sorted_list = sorted(data, key=lambda x: x[4])
        self.populate_listbox(sorted_list)

    def add_customer(self):
        add_customer_window = tk.Toplevel(self.master)
        AddCustomerPage.AddCustomer(add_customer_window, self.tempCursorInit)


if __name__ == "__main__":
    root = tk.Tk()
    app = CustomerInfoPage(master=root)
    app.mainloop()

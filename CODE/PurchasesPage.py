import tkinter as tk
from tkinter import ttk
import AddPurchasePage
import mysql.connector
import Processes
import DashboardPage


class PurchasesPage(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Purchase Information")
        self.master.geometry("1920x1080")
        self.tempCursorInit = tempCursorInit

        # Top frame
        self.top_frame = tk.Frame(self.master, pady=20)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.back_button = tk.Button(
            self.top_frame, text="Back", command=self.go_back)
        self.back_button.pack(side=tk.LEFT)

        # Search by purchase ID

        self.purchase_id_label = tk.Label(
            self.top_frame, text="Search by Purchase ID")
        self.purchase_id_label.pack(side=tk.LEFT, padx=(20, 10))

        self.purchase_id_entry = tk.Entry(self.top_frame)
        self.purchase_id_entry.pack(side=tk.LEFT, padx=10)

        self.purchase_id_submit_button = tk.Button(
            self.top_frame, text="Submit", command=self.search_by_purchase_id)
        self.purchase_id_submit_button.pack(side=tk.LEFT)

        # Search by supplier
        #  ID
        self.supplier_id_label = tk.Label(
            self.top_frame, text="Search by Supplier ID")
        self.supplier_id_label.pack(side=tk.LEFT, padx=(50, 10))

        self.supplier_id_entry = tk.Entry(self.top_frame)
        self.supplier_id_entry.pack(side=tk.LEFT, padx=10)

        self.supplier_id_submit_button = tk.Button(
            self.top_frame, text="Submit", command=self.search_by_supplier_id)
        self.supplier_id_submit_button.pack(side=tk.LEFT)

        # Sort by date
        self.sort_by_date_button = tk.Button(
            self.top_frame, text="Sort by Date", command=self.sort_by_date)
        self.sort_by_date_button.pack(side=tk.RIGHT, padx=20)

        # Start new purchase
        self.start_new_purchase_button = tk.Button(
            self.top_frame, text="Start New Purchase", command=self.start_new_purchase)
        self.start_new_purchase_button.pack(side=tk.RIGHT)

        # Bottom frame
        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # purchase listbox
        self.purchases_listbox = ttk.Treeview(self.bottom_frame, columns=(
            "purchase_id", "date", "supplier_id", "product_id", "quantity_bought", "product_name"), show="headings")
        self.purchases_listbox.column("purchase_id", width=100)
        self.purchases_listbox.column("date", width=100)
        self.purchases_listbox.column("supplier_id", width=100)
        self.purchases_listbox.column("product_id", width=100)
        self.purchases_listbox.column("quantity_bought", width=100)
        self.purchases_listbox.column("product_name", width=200)

        self.purchases_listbox.heading("purchase_id", text="Purchase ID")
        self.purchases_listbox.heading("date", text="Date")
        self.purchases_listbox.heading("supplier_id", text="Supplier ID")
        self.purchases_listbox.heading("product_id", text="Product ID")
        self.purchases_listbox.heading(
            "quantity_bought", text="Quantity Bought")
        self.purchases_listbox.heading("product_name", text="Product Name")

        self.purchases_listbox_scrollbar = ttk.Scrollbar(
            self.bottom_frame, orient=tk.VERTICAL, command=self.purchases_listbox.yview)
        self.purchases_listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.purchases_listbox.configure(
            yscrollcommand=self.purchases_listbox_scrollbar.set)
        self.purchases_listbox.pack(
            side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        allPurchaseData = Processes.Cursor_Init.showAll(
            self.tempCursorInit, "Purchase NATURAL JOIN (Purchase_has_Product NATURAL JOIN Product)")
        self.populate_listbox(allPurchaseData)

    def go_back(self):
        DashBoard = tk.Toplevel(self.master)
        DashboardPage.Dashboard(DashBoard, self.tempCursorInit)
        self.master.withdraw()

    def populate_listbox(self, data):
        for i in self.purchases_listbox.get_children():
            self.purchases_listbox.delete(i)
        num = 0
        for item in data:
            self.purchases_listbox.insert(parent='', index=num, iid=num, values=(
                item[0], item[1], item[2], item[3], item[4], item[5]))
            num = num + 1

    def start_new_purchase(self):
        add_purchase_stats_window = tk.Toplevel(self.master)
        AddPurchasePage.AddPurchasePage(
            add_purchase_stats_window, self.tempCursorInit)

    def search_by_purchase_id(self):
        purchase_ID = self.purchase_id_entry.get()
        if purchase_ID == '':
            self.populate_listbox(Processes.Cursor_Init.showAll(
                self.tempCursorInit, "Purchase NATURAL JOIN (Purchase_has_Product NATURAL JOIN Product)"))
        else:
            purchase_id = (int)(purchase_ID)
            myResult = Processes.Cursor_Init.showBySearch(
                self.tempCursorInit, "Purchase NATURAL JOIN (Purchase_has_Product NATURAL JOIN Product)", "Purchase_ID", purchase_id)
            self.populate_listbox(myResult)

    def search_by_supplier_id(self):
        Supplier_id = self.supplier_id_entry.get()
        if Supplier_id == '':
            self.populate_listbox(Processes.Cursor_Init.showAll(
                self.tempCursorInit, "Purchase NATURAL JOIN (Purchase_has_Product NATURAL JOIN Product)"))
        else:
            Supplier_ID = (int)(Supplier_id)
            myResult = Processes.Cursor_Init.showBySearch(
                self.tempCursorInit, "Purchase NATURAL JOIN (Purchase_has_Product NATURAL JOIN Product)", "Supplier_ID", Supplier_ID)
            self.populate_listbox(myResult)
        # TODO: implement search by supplier
        #  ID functionality
        pass

    def sort_by_date(self):
        data = []
        for child in self.purchases_listbox.get_children():
            row_data = []
            for column in self.purchases_listbox["columns"]:
                row_data.append(self.purchases_listbox.item(child)[
                                "values"][self.purchases_listbox["columns"].index(column)])
            data.append(row_data)
        sorted_list = sorted(data, key=lambda x: x[1])
        self.populate_listbox(sorted_list)
        # TODO: implement sorting by date functionality
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = PurchasesPage(master=root)
    app.mainloop()

import tkinter as tk
from tkinter import ttk
import AddSalesPage
import Processes
import DashboardPage
import DeleteSalePage


class SalesPage(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Sale Information")
        self.master.geometry("1920x1080")
        self.tempCursorInit = tempCursorInit

        # Top frame
        self.top_frame = tk.Frame(self.master, pady=20)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.back_button = tk.Button(
            self.top_frame, text="Back", command=self.go_back)
        self.back_button.pack(side=tk.LEFT)

        # Search by Sale ID
        self.sale_id_label = tk.Label(
            self.top_frame, text="Search by Sale ID")
        self.sale_id_label.pack(side=tk.LEFT, padx=(20, 10))

        self.sale_id_entry = tk.Entry(self.top_frame)
        self.sale_id_entry.pack(side=tk.LEFT, padx=10)

        self.sale_id_submit_button = tk.Button(
            self.top_frame, text="Submit", command=self.search_by_sale_id)
        self.sale_id_submit_button.pack(side=tk.LEFT)

        # Search by customer ID
        self.customer_id_label = tk.Label(
            self.top_frame, text="Search by Customer ID")
        self.customer_id_label.pack(side=tk.LEFT, padx=(50, 10))

        self.customer_id_entry = tk.Entry(self.top_frame)
        self.customer_id_entry.pack(side=tk.LEFT, padx=10)

        self.customer_id_submit_button = tk.Button(
            self.top_frame, text="Submit", command=self.search_by_customer_id)
        self.customer_id_submit_button.pack(side=tk.LEFT)

        # Sort by date
        self.sort_by_date_button = tk.Button(
            self.top_frame, text="Sort by Date", command=self.sort_by_date)
        self.sort_by_date_button.pack(side=tk.RIGHT, padx=20)

        # Start new Sale
        self.start_new_sale_button = tk.Button(
            self.top_frame, text="Start New Sale", command=self.start_new_sale)
        self.start_new_sale_button.pack(side=tk.RIGHT)

        self.start_new_sale_button = tk.Button(
            self.top_frame, text="Delete Sale", command=self.delete_sale)
        self.start_new_sale_button.pack(side=tk.RIGHT)

        # Bottom frame
        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Sale listbox
        self.Sales_listbox = ttk.Treeview(self.bottom_frame, columns=(
            "sale_id", "date", "customer_id", "emp_id", "product_id", "quantity_bought", "product_name"), show="headings")
        self.Sales_listbox.column("sale_id", width=100)
        self.Sales_listbox.column("date", width=100)
        self.Sales_listbox.column("customer_id", width=100)
        self.Sales_listbox.column("emp_id", width=100)
        self.Sales_listbox.column("product_id", width=100)
        self.Sales_listbox.column("quantity_bought", width=100)
        self.Sales_listbox.column("product_name", width=200)

        self.Sales_listbox.heading("sale_id", text="Sale ID")
        self.Sales_listbox.heading("date", text="Date")
        self.Sales_listbox.heading("customer_id", text="Customer ID")
        self.Sales_listbox.heading("emp_id", text="Employee ID")
        self.Sales_listbox.heading("product_id", text="Product ID")
        self.Sales_listbox.heading("quantity_bought", text="Quantity Bought")
        self.Sales_listbox.heading("product_name", text="Product Name")

        self.Sales_listbox_scrollbar = ttk.Scrollbar(
            self.bottom_frame, orient=tk.VERTICAL, command=self.Sales_listbox.yview)
        self.Sales_listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.Sales_listbox.configure(
            yscrollcommand=self.Sales_listbox_scrollbar.set)
        self.Sales_listbox.pack(
            side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        Query_Result = Processes.Cursor_Init.showAll(
            self.tempCursorInit, "Sale NATURAL JOIN (Sale_has_Product NATURAL JOIN Product)")
        self.populate_listbox(Query_Result)

    def go_back(self):
        DashBoard = tk.Toplevel(self.master)
        DashboardPage.Dashboard(DashBoard, self.tempCursorInit)
        self.master.withdraw()

    def populate_listbox(self, data):
        for i in self.Sales_listbox.get_children():
            self.Sales_listbox.delete(i)
        num = 0
        for item in data:
            self.Sales_listbox.insert(parent='', index=num, iid=num, values=(
                item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
            num = num + 1

    def start_new_sale(self):
        add_Sale_stats_window = tk.Toplevel(self.master)
        AddSalesPage.AddSalesPage(add_Sale_stats_window, self.tempCursorInit)

    def delete_sale(self):
        deleteSaleWindoe = tk.Toplevel(self.master)
        DeleteSalePage.DeleteSalePage(deleteSaleWindoe, self.tempCursorInit)

    def search_by_sale_id(self):
        Sale_id = self.sale_id_entry.get()
        if Sale_id == '':
            self.populate_listbox(Processes.Cursor_Init.showAll(
                self.tempCursorInit, "Sale NATURAL JOIN (Sale_has_Product NATURAL JOIN Product)"))
        # query = "Select "
        # if
        else:
            Sale_ID = (int)(Sale_id)
            Query_Result = Processes.Cursor_Init.showBySearch(
                self.tempCursorInit, "Sale NATURAL JOIN (Sale_has_Product NATURAL JOIN Product)", "Sale_ID", Sale_ID)
            # print(Query_Result)
            self.populate_listbox(Query_Result)
        # TODO: implement search by Sale ID functionality
        pass

    def search_by_customer_id(self):
        Cust_id = (self.customer_id_entry.get())
        if Cust_id == '':
            self.populate_listbox(Processes.Cursor_Init.showAll(
                self.tempCursorInit, "Sale NATURAL JOIN (Sale_has_Product NATURAL JOIN Product)"))
        else:
            Cust_ID = int(Cust_id)
            Query_Result = Processes.Cursor_Init.showBySearch(
                self.tempCursorInit, "Sale NATURAL JOIN (Sale_has_Product NATURAL JOIN Product)", "Cust_ID", Cust_ID)
            self.populate_listbox(Query_Result)
        # TODO: implement search by customer ID functionality
        pass

    def sort_by_date(self):
        data = []
        for child in self.Sales_listbox.get_children():
            row_data = []
            for column in self.Sales_listbox["columns"]:
                row_data.append(self.Sales_listbox.item(child)[
                                "values"][self.Sales_listbox["columns"].index(column)])
            data.append(row_data)
        sorted_list = sorted(data, key=lambda x: x[1])
        self.populate_listbox(sorted_list)
        # TODO: implement sorting by date functionality
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = SalesPage(master=root)
    app.mainloop()

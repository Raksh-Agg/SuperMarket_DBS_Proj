import tkinter as tk
from tkinter import ttk
import AddProductPage
import Processes
import UpdateQuantityPage
import DashboardPage


class ProductStatsPage(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Product Stats")
        self.master.geometry("1920x1080")
        # top frame
        self.top_frame = tk.Frame(self.master)
        self.top_frame.pack(side="top", fill="x")
        self.tempCursorInit = tempCursorInit

        self.back_button = tk.Button(
            self.top_frame, text="Back", command=self.go_back)
        self.back_button.pack(side="left", padx=10, pady=10)

        self.search_label = tk.Label(self.top_frame, text="Search by name:")
        self.search_label.pack(side="left", padx=10, pady=10)

        self.search_entry = tk.Entry(self.top_frame)
        self.search_entry.pack(side="left", padx=10, pady=10)

        self.submit_button = tk.Button(
            self.top_frame, text="Submit", command=self.search_product)
        self.submit_button.pack(side="left", padx=10, pady=10)

        self.price_low_high_button = tk.Button(
            self.top_frame, text="Price Low to High", command=self.sort_price_low_high)
        self.price_low_high_button.pack(side="left", padx=10, pady=10)

        self.price_high_low_button = tk.Button(
            self.top_frame, text="Price High to Low", command=self.sort_price_high_low)
        self.price_high_low_button.pack(side="left", padx=10, pady=10)

        self.sort_quantity_button = tk.Button(
            self.top_frame, text="Sort by Quantity Left", command=self.sort_quantity)
        self.sort_quantity_button.pack(side="left", padx=10, pady=10)

        self.add_product_button = tk.Button(
            self.top_frame, text="Update Product Quantity", command=self.update_product)
        self.add_product_button.pack(side="right", padx=10, pady=10)

        self.add_product_button = tk.Button(
            self.top_frame, text="Add New Product", command=self.add_product)
        self.add_product_button.pack(side="right", padx=10, pady=10)

        # bottom frame
        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.pack(side="bottom", fill="both", expand=True)

        self.columns = ("Product ID", "Product Name", "Price", "Quantity Left")
        self.treeview = ttk.Treeview(
            self.bottom_frame, columns=self.columns, show="headings")

        # define column headings
        for col in self.columns:
            self.treeview.heading(col, text=col)

        # add vertical scrollbar
        self.scrollbar_y = ttk.Scrollbar(
            self.bottom_frame, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar_y.set)
        self.scrollbar_y.pack(side="right", fill="y")

        # add horizontal scrollbar
        self.scrollbar_x = ttk.Scrollbar(
            self.bottom_frame, orient="horizontal", command=self.treeview.xview)
        self.treeview.configure(xscrollcommand=self.scrollbar_x.set)
        self.scrollbar_x.pack(side="bottom", fill="x")

        # pack the treeview
        self.treeview.pack(side="left", fill="both", expand=True)

        allProductData = Processes.Cursor_Init.showAll(
            self.tempCursorInit, "Product")
        self.populate_listbox(allProductData)

    def populate_listbox(self, data):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        num = 0
        for item in data:
            self.treeview.insert(parent='', index=num, iid=num, values=(
                item[0], item[1], item[2], item[3]))
            num = num + 1

    def go_back(self):
        DashBoard = tk.Toplevel(self.master)
        DashboardPage.Dashboard(DashBoard, self.tempCursorInit)
        self.master.withdraw()

    def search_product(self):
        Prod_Name = self.search_entry.get()
        myResult = Processes.Cursor_Init.searchByName(
            self.tempCursorInit, "Product", Prod_Name)
        self.populate_listbox(myResult)

    def sort_price_low_high(self):
        data = []
        for child in self.treeview.get_children():
            row_data = []
            for column in self.treeview["columns"]:
                row_data.append(self.treeview.item(child)[
                                "values"][self.treeview["columns"].index(column)])
            data.append(row_data)
        sorted_list = sorted(data, key=lambda x: x[2])
        self.populate_listbox(sorted_list)

    def sort_price_high_low(self):
        data = []
        for child in self.treeview.get_children():
            row_data = []
            for column in self.treeview["columns"]:
                row_data.append(self.treeview.item(child)[
                                "values"][self.treeview["columns"].index(column)])
            data.append(row_data)
        sorted_list = sorted(data, key=lambda x: x[2], reverse=True)
        self.populate_listbox(sorted_list)

    def sort_quantity(self):
        data = []
        for child in self.treeview.get_children():
            row_data = []
            for column in self.treeview["columns"]:
                row_data.append(self.treeview.item(child)[
                                "values"][self.treeview["columns"].index(column)])
            data.append(row_data)
        sorted_list = sorted(data, key=lambda x: x[3])
        self.populate_listbox(sorted_list)

    def add_product(self):
        add_product_window = tk.Toplevel(self.master)
        AddProductPage.AddProductPage(add_product_window, self.tempCursorInit)

    def update_product(self):
        update_product_window = tk.Toplevel(self.master)
        UpdateQuantityPage.UpdateQuantityPage(
            update_product_window, self.tempCursorInit)


if __name__ == "__main__":
    root = tk.Tk()
    app = ProductStatsPage(master=root)
    app.mainloop()

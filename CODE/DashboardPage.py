import tkinter as tk
import EmployeeStatsPage
import ProductStatsPage
import SalesPage
import PurchasesPage
import SupplierInfoPage
import CustomerInfoPage
import Processes
from tkinter import PhotoImage


class Dashboard(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Dashboard")
        self.master.geometry("1920x1080")
        self.tempCursorInit = tempCursorInit

        self.bg_image = PhotoImage(file="pngegg.png")
        label1 = tk.Label(self.master, image=self.bg_image)
        label1.place(x=0, y=0, relheight=1, relwidth=1)
        # create a frame in the center of the window
        frame = tk.Frame(self.master, bg="black")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.back_button = tk.Button(
            self.master, text="Exit", command=self.Exit)
        self.back_button.pack(side=tk.LEFT, anchor='n')

        # create the buttons inside the frame
        self.product_stats_button = tk.Button(
            frame, text="Inventory Reports", command=self.open_product_stats, padx=20, pady=20, bg="#CCCCCC", font=("Arial", 12, "bold"))
        self.product_stats_button.grid(row=0, column=0, padx=10, pady=10)

        self.supplier_stats_button = tk.Button(
            frame, text="Supplier Information", command=self.open_supplier_info, padx=20, pady=20, bg="#CCCCCC", font=("Arial", 12, "bold"))
        self.supplier_stats_button.grid(row=0, column=1, padx=10, pady=10)

        self.customer_stats_button = tk.Button(
            frame, text="Customer Information", command=self.open_customer_info, padx=20, pady=20, bg="#CCCCCC", font=("Arial", 12, "bold"))
        self.customer_stats_button.grid(row=0, column=2, padx=10, pady=10)

        self.employee_stats_button = tk.Button(
            frame, text="Employee Information", command=self.open_employee_stats, padx=20, pady=20, bg="#CCCCCC", font=("Arial", 12, "bold"))
        self.employee_stats_button.grid(row=1, column=0, padx=10, pady=10)

        self.orders_button = tk.Button(
            frame, text="Sales Report", command=self.open_orders, padx=20, pady=20, bg="#CCCCCC", font=("Arial", 12, "bold"))
        self.orders_button.grid(row=1, column=1, padx=10, pady=10)

        self.purchases_button = tk.Button(
            frame, text="Purchases", command=self.open_purchases, padx=20, pady=20, bg="#CCCCCC", font=("Arial", 12, "bold"))
        self.purchases_button.grid(row=1, column=2, padx=10, pady=10)

    def open_employee_stats(self):
        employee_stats_window = tk.Toplevel(self.master)
        EmployeeStatsPage.EmployeeStats(
            employee_stats_window, self.tempCursorInit)
        self.master.withdraw()

    def open_product_stats(self):
        product_stats_window = tk.Toplevel(self.master)
        ProductStatsPage.ProductStatsPage(
            product_stats_window, self.tempCursorInit)
        self.master.withdraw()

    def open_orders(self):
        orders_window = tk.Toplevel(self.master)
        SalesPage.SalesPage(orders_window, self.tempCursorInit)
        self.master.withdraw()

    def open_purchases(self):
        purchases_window = tk.Toplevel(self.master)
        PurchasesPage.PurchasesPage(purchases_window, self.tempCursorInit)
        self.master.withdraw()

    def open_customer_info(self):
        customer_info_window = tk.Toplevel(self.master)
        CustomerInfoPage.CustomerInfoPage(
            customer_info_window, self.tempCursorInit)
        self.master.withdraw()

    def open_supplier_info(self):
        supplier_info_window = tk.Toplevel(self.master)
        SupplierInfoPage.SupplierInfoPage(
            supplier_info_window, self.tempCursorInit)
        self.master.withdraw()

    def Exit(self):
        Processes.Cursor_Init.Finish(self.tempCursorInit)
        self.master.destroy()


if __name__ == "_main_":
    root = tk.Tk()
    app = Dashboard(master=root)
    app.mainloop()

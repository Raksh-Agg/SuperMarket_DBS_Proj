import tkinter as tk
from tkinter import ttk
import Processes
import AddEmployeePage
import UpdateJobPositionPage
import DashboardPage
from tkinter import messagebox


class EmployeeStats(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Employee Stats")
        self.master.geometry("1920x1080")
        self.tempCursorInit = tempCursorInit

        # Top frame with search boxes and buttons

        self.top_frame = tk.Frame(self.master)
        self.top_frame.pack(side=tk.TOP, pady=10)

        self.back_button = tk.Button(
            self.top_frame, text="Back", command=self.go_back)
        self.back_button.grid(row=0, column=0, pady=5)

        self.search_name_label = tk.Label(
            self.top_frame, text="Search by name:")
        self.search_name_label.grid(row=1, column=0, pady=7)
        self.search_name_entry = tk.Entry(self.top_frame, width=30)
        self.search_name_entry.grid(row=1, column=1, pady=7)

        self.search_name_button = tk.Button(
            self.top_frame, text="Submit", command=self.search_by_name)
        self.search_name_button.grid(row=1, column=3, pady=7)

        self.search_id_label = tk.Label(
            self.top_frame, text="Search by Employee Id:")
        self.search_id_label.grid(row=2, column=0, pady=7)
        self.search_id_entry = tk.Entry(self.top_frame, width=10)
        self.search_id_entry.grid(row=2, column=1, pady=7)
        self.search_id_button = tk.Button(
            self.top_frame, text="Submit", command=self.search_by_id)
        self.search_id_button.grid(row=2, column=2, pady=7)

        self.sort_id_button = tk.Button(
            self.top_frame, text="Sort by Employee Id", command=self.sort_by_id)
        self.sort_id_button.grid(row=3, column=0, pady=7)

        self.sort_salary_button = tk.Button(
            self.top_frame, text="Sort by Salary", command=self.sort_by_salary)
        self.sort_salary_button.grid(row=3, column=1, pady=7)

        self.sort_sold_button = tk.Button(
            self.top_frame, text="Employee Performance", command=self.sort_by_sold)
        self.sort_sold_button.grid(row=3, column=2, pady=7)

        self.add_button = tk.Button(
            self.top_frame, text="Change Employee Job Title", command=self.change_Job_Title)
        self.add_button.grid(row=4, column=0, pady=7)

        self.add_button = tk.Button(
            self.top_frame, text="Add New Employee", command=self.add_Employee)
        self.add_button.grid(row=4, column=1, pady=7)

        self.lower_frame = tk.Frame(self.master)
        self.lower_frame.pack(side=tk.BOTTOM, fill=tk.BOTH,
                              expand=True, padx=10, pady=10)

        self.treeview = ttk.Treeview(self.lower_frame, columns=(
            "id", "first_name", "second_name", "salary", "amt_sold", "designation", "phone", "sex", "address1", "address2", "pincode"))
        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.treeview.heading("id", text="Id")
        self.treeview.heading("first_name", text="First_Name")
        self.treeview.heading("second_name", text="Second_Name")
        self.treeview.heading("salary", text="Salary")
        self.treeview.heading("amt_sold", text="Amount Sold")
        self.treeview.heading("designation", text="Designation")
        self.treeview.heading("phone", text="Phone Number")
        self.treeview.heading("sex", text="Sex")
        self.treeview.heading("address1", text="Address Line 1")
        self.treeview.heading("address2", text="Address Line 2")
        self.treeview.heading("pincode", text="pincode")

        allCustomerData = Processes.Cursor_Init.showAll(
            self.tempCursorInit, "Employee")
        self.populate_listbox(allCustomerData)

    def populate_listbox(self, data):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        num = 0
        for item in data:
            self.treeview.insert(parent='', index=num, iid=num, values=(
                item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10]))
            num = num + 1

    def search_by_name(self):
        Emp_Name = self.search_name_entry.get()
        myResult = Processes.Cursor_Init.searchByName(
            self.tempCursorInit, "Employee", Emp_Name)
        self.populate_listbox(myResult)

    def search_by_id(self):
        Emp_ID = self.search_id_entry.get()
        if Emp_ID == '':
            self.populate_listbox(Processes.Cursor_Init.showAll(
                self.tempCursorInit, "Employee"))
        else:
            Emp_id = (int)(Emp_ID)
            myResult = Processes.Cursor_Init.showBySearch(
                self.tempCursorInit, "Employee", "Emp_ID", Emp_id)
            self.populate_listbox(myResult)

    def sort_by_sold(self):
        data = []
        for child in self.treeview.get_children():
            row_data = []
            for column in self.treeview["columns"]:
                row_data.append(self.treeview.item(child)[
                                "values"][self.treeview["columns"].index(column)])
            data.append(row_data)
        sorted_list = sorted(data, key=lambda x: x[4], reverse=True)
        self.populate_listbox(sorted_list)
        messagebox.showinfo("Employee Stats Generated",
                            "Employees Sorted acoording to the amount of revenue they generated")

    def sort_by_id(self):
        data = []
        for child in self.treeview.get_children():
            row_data = []
            for column in self.treeview["columns"]:
                row_data.append(self.treeview.item(child)[
                                "values"][self.treeview["columns"].index(column)])
            data.append(row_data)
        sorted_list = sorted(data, key=lambda x: x[0])
        self.populate_listbox(sorted_list)

    def sort_by_salary(self):
        data = []
        for child in self.treeview.get_children():
            row_data = []
            for column in self.treeview["columns"]:
                row_data.append(self.treeview.item(child)[
                                "values"][self.treeview["columns"].index(column)])
            data.append(row_data)
        sorted_list = sorted(data, key=lambda x: x[3], reverse=True)
        self.populate_listbox(sorted_list)

    def add_Employee(self):
        add_Employee_window = tk.Toplevel(self.master)
        AddEmployeePage.AddEmployeePage(
            add_Employee_window, self.tempCursorInit)

    def change_Job_Title(self):
        update_Job_Title = tk.Toplevel(self.master)
        UpdateJobPositionPage.UpdateJobPositionPage(
            update_Job_Title, self.tempCursorInit)

    def go_back(self):
        DashBoard = tk.Toplevel(self.master)
        DashboardPage.Dashboard(DashBoard, self.tempCursorInit)
        self.master.withdraw()


if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeStats(master=root)
    app.mainloop()

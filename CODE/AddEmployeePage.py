import tkinter as tk
from tkinter import messagebox
import Processes


class AddEmployeePage(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Add Employee")
        self.master.geometry("1920x1080")
        self.tempCursorInit = tempCursorInit

        # Back button
        self.back_button = tk.Button(
            self.master, text="Back", command=self.master.destroy, anchor='w')
        self.back_button.grid(row=0, column=0, padx=5, pady=5)

        # Employee first name
        self.fname_label = tk.Label(self.master, text="First Name")
        self.fname_label.grid(row=1, column=0, padx=10, pady=10)

        self.first_name_entry = tk.Entry(self.master)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Employee second name
        self.sname_label = tk.Label(self.master, text="Second Name")
        self.sname_label.grid(row=2, column=0, padx=10, pady=10)

        self.second_name_entry = tk.Entry(self.master)
        self.second_name_entry.grid(row=2, column=1, padx=10, pady=10)

        # Employee salary
        self.salary_label = tk.Label(self.master, text="Salary")
        self.salary_label.grid(row=3, column=0, padx=10, pady=10)

        self.salary_entry = tk.Entry(self.master)
        self.salary_entry.grid(row=3, column=1, padx=10, pady=10)

        # Employee designation
        self.designation_label = tk.Label(self.master, text="Designation")
        self.designation_label.grid(row=4, column=0, padx=10, pady=10)

        self.designation_options = [
            'Custodian', 'Security', 'Manager', 'Supervisor', 'Cashier']
        self.designation_var = tk.StringVar(self.master)
        self.designation_var.set(self.designation_options[0])
        self.designation_menu = tk.OptionMenu(
            self.master, self.designation_var, *self.designation_options)
        self.designation_menu.grid(row=4, column=1, padx=10, pady=10)

        # Employee phone number
        self.phone_label = tk.Label(self.master, text="Phone Number")
        self.phone_label.grid(row=5, column=0, padx=10, pady=10)

        self.phone_number_entry = tk.Entry(self.master)
        self.phone_number_entry.grid(row=5, column=1, padx=10, pady=10)

        # Employee sex
        self.sex_label = tk.Label(self.master, text="Sex")
        self.sex_label.grid(row=6, column=0, padx=10, pady=10)

        self.sex_options = ['M', 'F']
        self.sex_var = tk.StringVar(self.master)
        self.sex_var.set(self.sex_options[0])
        self.sex_menu = tk.OptionMenu(
            self.master, self.sex_var, *self.sex_options)
        self.sex_menu.grid(row=6, column=1, padx=10, pady=10)

        # Employee address line 1
        self.addr1_label = tk.Label(self.master, text="Address Line 1")
        self.addr1_label.grid(row=7, column=0, padx=10, pady=10)

        self.address_line_one_entry = tk.Entry(self.master)
        self.address_line_one_entry.grid(row=7, column=1, padx=10, pady=10)

        # Employee address line 2
        self.addr2_label = tk.Label(self.master, text="Address Line 2")
        self.addr2_label.grid(row=8, column=0, padx=10, pady=10)

        self.address_line_two_entry = tk.Entry(self.master)
        self.address_line_two_entry.grid(row=8, column=1, padx=10, pady=10)

        # Employee Postal Code
        self.postal_code_label = tk.Label(self.master, text="Postal Code")
        self.postal_code_label.grid(row=9, column=0, padx=10, pady=10)

        self.postal_code_entry = tk.Entry(self.master)
        self.postal_code_entry.grid(row=9, column=1, padx=10, pady=10)

        # Submit Button
        self.submit_button = tk.Button(
            self.master, text="Submit", command=self.submit_employee)
        self.submit_button.grid(
            row=10, column=0, columnspan=2, padx=10, pady=10)

    def submit_employee(self):
        # get values from entry fields
        first_name = self.first_name_entry.get()
        second_name = self.second_name_entry.get()
        salary = self.salary_entry.get()
        # amount_sold = self.amount_sold_entry.get()
        designation = self.designation_var.get()
        phone_number = self.phone_number_entry.get()
        sex = self.sex_var.get()
        address_line_one = self.address_line_one_entry.get()
        address_line_two = self.address_line_two_entry.get()
        postal_code = self.postal_code_entry.get()

        # check for empty required fields
        if not first_name:
            messagebox.showerror("Error", "First Name Field empty")
        elif not second_name:
            messagebox.showerror("Error", "Second Name Field empty")
        elif not salary:
            messagebox.showerror("Error", "Salary Field empty")
        elif not designation:
            messagebox.showerror("Error", "Designation Field empty")
        elif not phone_number:
            messagebox.showerror("Error", "Phone Number Field empty")
        elif not sex:
            messagebox.showerror("Error", "Sex Field empty")
        elif not address_line_one:
            messagebox.showerror("Error", "Address Line One Field empty")
        elif not postal_code:
            messagebox.showerror("Error", "Postal Code Field empty")
        # check for correct data types
        elif not salary.isdigit():
            messagebox.showerror("Error", "Invalid Salary")
        elif not phone_number.isdigit() or len(phone_number) != 10:
            messagebox.showerror("Error", "Invalid Phone Number")
        elif not postal_code.isdigit() or len(postal_code) != 6:
            messagebox.showerror("Error", "Invalid Postal Code")
        else:
            # save employee data to database
            messagebox.showinfo("Success", "Employee Added Successfully")
            # clear all entry fields
            self.first_name_entry.delete(0, tk.END)
            self.second_name_entry.delete(0, tk.END)
            self.salary_entry.delete(0, tk.END)
            self.designation_var.set('')
            self.phone_number_entry.delete(0, tk.END)
            self.sex_var.set('')
            self.address_line_one_entry.delete(0, tk.END)
            self.address_line_two_entry.delete(0, tk.END)
            self.postal_code_entry.delete(0, tk.END)

        # TODO: Complete kar dena ye function.
        # TODO: OK bhai
        Processes.Cursor_Init.insertEmployee(
            self.tempCursorInit, first_name, second_name, salary, designation, phone_number, sex, address_line_one, address_line_two, postal_code)
        messagebox.showinfo("Success", "Employee Added Successfully")
        self.master.withdraw()


if __name__ == "__main__":
    root = tk.Tk()
    app = AddEmployeePage(master=root)
    app.mainloop()

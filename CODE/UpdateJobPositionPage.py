import tkinter as tk
from tkinter import ttk, messagebox
import Processes


class UpdateJobPositionPage(tk.Frame):
    def __init__(self, master, tempCursorInit):
        super().__init__(master)
        self.master = master
        self.master.title("Update Job Position")
        self.tempCursorInit = tempCursorInit

        self.back_button = tk.Button(
            self.master, text="Back", command=self.master.destroy, anchor='w')
        self.back_button.grid(row=0, column=0, padx=5, pady=5)

        self.empid_label = tk.Label(self.master, text="Employee ID")
        self.empid_label.grid(row=1, column=0, padx=10, pady=10)

        self.validate_int = self.master.register(self.validate_integer)

        self.empid_entry = tk.Entry(
            self.master, validate="key", validatecommand=(self.validate_int, '%P'))
        self.empid_entry.grid(row=1, column=1, padx=10, pady=10)

        self.jobtitle_label = tk.Label(self.master, text="Job Title")
        self.jobtitle_label.grid(row=2, column=0, padx=10, pady=10)

        self.jobtitle_var = tk.StringVar(self.master)
        self.jobtitle_dropdown = ttk.OptionMenu(
            self.master, self.jobtitle_var, "Custodian", "Custodian", "Security", "Manager", "Supervisor", "Cashier")
        self.jobtitle_dropdown.grid(row=2, column=1, padx=10, pady=10)

        self.submit_button = tk.Button(
            self.master, text="Update", command=self.update_job_position)
        self.submit_button.grid(
            row=3, column=0, columnspan=2, padx=10, pady=10)

    def validate_integer(self, value):
        if value.isdigit() or value == "":
            return True
        else:
            return False

    def update_job_position(self):
        empid = self.empid_entry.get()
        jobtitle = self.jobtitle_var.get()

        if not empid.isdigit() or empid == "":
            messagebox.showerror("Error", "Please enter a valid Employee ID")
        else:
            Processes.Cursor_Init.updateJobPosition(
                self.tempCursorInit, jobtitle, empid)
            messagebox.showinfo("Success", "Job Position Updated Successfully")
            self.empid_entry.delete(0, tk.END)
    # TODO: complete the function


if __name__ == "__main__":
    root = tk.Tk()
    app = UpdateJobPositionPage(master=root)
    app.mainloop()

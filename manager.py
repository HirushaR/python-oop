from employee import Employee

class Manager(Employee):

    def __init__(self, first_name, last_name, pay, employees = None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees =  employees

    def assign_emplyee_to_manager(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_assign_employee_from_manager(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for employee in self.employees:
            print("# {} {}".format(employee.first_name, employee.last_name))

from employee import Employee
from developer import Developer
from manager import Manager

emp1 = Developer('Hirusha', 'Fernano', 10000, 'Python')
emp2 = Employee('john', 'doe', 10000) 
mgr_1 = Manager('Neil', 'Armstrong', 40000, [emp1])


print(mgr_1.fullname())
mgr_1.print_employees()

mgr_1.assign_emplyee_to_manager(emp2)
print("assign emp 2")
mgr_1.print_employees()

mgr_1.assign_emplyee_to_manager(emp1)
print("assign emp 1 duplicate")
mgr_1.print_employees()

mgr_1.remove_assign_employee_from_manager(emp1)
print("remove emp 1")
mgr_1.print_employees()


# print(emp1.fullname())
# print(emp1.pay)
# emp1.raise_amount = 1.05
# emp1.apply_rais()
# print(emp1.programming_language)

# print(emp2.fullname())
# # print(emp2.pay)
# # emp2.apply_rais()
# print(emp2.pay)

# print(Employee.num_of_employees)
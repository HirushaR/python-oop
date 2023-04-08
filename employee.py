class Employee:

    raise_amount = 1.04
    num_of_employees = 0 
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = '{}.{}@email.com'.format(first_name.lower(), last_name.lower())
        self.pay = pay
        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first_name , self.last_name)

    def apply_rais(self):
        self.pay = int(self.pay * self.raise_amount)
    


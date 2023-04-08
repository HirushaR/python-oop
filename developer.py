from employee import Employee

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, programming_language):
      super().__init__(first_name,last_name, pay)
      self.programming_language = programming_language
class Employee:
    def __init__(self, role, dept , salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showDetails(self):
        print("role = ",self.role)
        print("Dept = ",self.dept)
        print("Salary =",self.salary)

class Engineer(Employee):
    def __init__(self, role, dept, salary):
        super().__init__(role, dept, salary)

e1 = Employee("Accountant","Finnance","60k")
e1.showDetails()
        
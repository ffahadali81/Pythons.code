class Employee:
    def __init__(self, name, salary, dept):
        self.name = name
        self.salary = salary
        self.dept = dept
    def bonus(self, amount):
        self.salary += amount

    def display(self):
        print("Name",self.name)
        print("Salary",self.salary)
        print("Department",self.dept)

e1 = Employee("Ali",12000, "IT")
e1.display()
print("==========================================")

e1.bonus(5000)
e1.display()


# class Employee:

#     company_name = 'MSys Technologies'

#     def __init__(self, ename, empno):
#         self.name = ename
#         self.no = empno

#     def display(self):
#         return f"Employee name is {self.name} and employee_id is {self.no}"

# e1 = Employee("Abhishek", 2222)
# print(e1.company_name)
# print(e1.display())

class Person(object):
  
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
  
    def display(self):
        print(self.name)
        print(self.idnumber)
          
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        Person.__init__(self, name, idnumber)
        self.salary = salary
        self.post = post
  
        # invoking the __init__ of the parent class
        
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))

a = Employee('Rahul', 886012, 200000, "Trainee")
a.display()
a.details()
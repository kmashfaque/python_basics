# class Teacher:
#     def __init__(self, name, age, profession, subject):
#         self.name = name
#         self.age = age
#         self.profession = profession
#         self.subject = subject

#     def teacherfunction(self):
#         print(
#             f"My name is {self.name}. I am {self.age} years old. I am a {self.profession}. I have {self.subject} students.")


# teacher = Teacher("Ashish", 46, "teacher", "science")
# teacher.teacherfunction()
# teacher2 = Teacher("Chalchalani", 50, "teacher", "science")
# teacher2.teacherfunction()


# class inheritence

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def fullname(self):
#         print(f"My name is {self.fname} {self.lname}")


# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year


# student = Student("Shekikh", "Newaj", 2022)
# print(student.fullname())


# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def fullname(self):
#         print(f"My name is {self.fname} {self.lname}")


# class Student(Person):
#     def __init__(self, fname, lname, year):
#         Person.__init__(self, fname, lname)
#         self.graduationyear = year


# student = Student("Shekikh", "Newaj", 2022)
# print(student.fullname())


# exmaples for class variables and instance variables
# youtube link
# https: // www.youtube.com/watch?v = BJ-VvGyQxho

# import datetime


# class Employee:
#     num_of_employee = 0
#     raise_amount = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay

#         Employee.num_of_employee += 1

#     def fullname(self):
#         return "{} {} ".format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#         return self.pay

#     @classmethod
#     def set_raise_amnt(cls, amount):
#         cls.raise_amount = amount

#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split("-")
#         return cls(first, last, pay)

#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True


# Employee.set_raise_amnt(10)
# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)


# print(emp_1.apply_raise())
# emp_2.raise_amount = 1.05
# print(emp_2.apply_raise())


# for the classmethod

# emp_str_1 = "John-Doe-70000"
# emp_str_2 = "Steve-Smith-80000"
# emp_str_1 = "John-Doe-100000"


# new_emp_2 = Employee.from_string(emp_str_2)
# print(new_emp_2.first)


# for the staticmethod
# not takes any class or instances

# my_date = datetime.date(2022, 6, 26)
# print(Employee.is_workday(my_date))


# class inheritence

# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first+"."+last+"@gmail.com"

#     def fullname(self):
#         return "{} {}".format(self.first, self.last)


# class Developer(Employee):
#     def __init__(self, first, last, pay, pro_lang):
#         super().__init__(first, last, pay)
#         self.pro_lang = pro_lang


# class Manager(Employee):
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees

#     def add_emps(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)

#     def remove_emps(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)

#     def print_emps(self):
#         for emp in self.employees:
#             print("--> {}".format(emp.fullname()))


# dev_1 = Developer("abir", "rahaman", 10000, "python")
# dev_2 = Developer("Test", "employee", 10000, "java")

# mng_1 = Manager("SUe", "Smith", 9000, [dev_1])

# mng_1.add_emps(dev_2)
# mng_1.print_emps()

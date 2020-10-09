class Profile():
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.email=fname+lname+'@gmail.com'

    def fullname(self):
        return '{}{}'.format(self.fname,self.lname)
class Developer(Profile):
    def __init__(self,fname,lname,salary,prog_lan):
        super().__init__(fname,lname,salary)
        self.prog_lan=prog_lan

class Manager(Profile):
    def __init__(self,fname,lname,salary,employees=None):
        super().__init__(fname,lname,salary)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname())
   # def __str__(self):
    #    return f'{self.fname} {self.lname} {self.salary}'
    def __repr__(self):
        return "Profile('{}','{},'{})".format(self.fname,self.lname,self.salary)
    
profile1=Profile('Hasan',' Tuhin',500000)
print(profile1)
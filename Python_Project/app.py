class Profile():
    num_of_employee=0
    raise_amount=1.04
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

        Profile.num_of_employee+=1 #this will count number of employees

    def apply_raise(self):
        self.salary=int(self.salary*Profile.raise_amount)
print(f'Total employee:{Profile.num_of_employee}')
tuhin=Profile('Hassan','Tuhin',500000)
shifuddin=Profile('Shifuddin','Tushar',450000)


class Profile():
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

    def apply_raise(self):
        self.salary=int(self.salary*1.04)

shifuddin=Profile('Shifuddin','Tushar',450000)
tuhin=Profile('Hassan','Tuhin',500000)

print(f"tuhin's salry {tuhin.salary}")
tuhin.apply_raise()
print("tuhin's salary after applying apply_raise")
print(tuhin.salary)

print(f"shifuddin's salary {shifuddin.salary}")
shifuddin.apply_raise()
print("shifuddin's salary after applying apply_raise")
print(shifuddin.salary)
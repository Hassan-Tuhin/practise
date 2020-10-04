'''def find_max(numbers):
    maximum=numbers[0]
    for number in numbers:
        if number>maximum:
            maximum=number
    return maximum'''
class Profile():
    def __init__(self,fname,lname,age,salary):#it's a constructor
        self.fname=fname
        self.lname=lname
        self.age=age
        self.salary=salary
        self.email=fname+lname+'@gmail.com'

tuhin=Profile('Hassan','tuhin',20,500000)
print(tuhin.email)
tanbir=Profile('Tanbir','sakib',22,450000)
print(tanbir.email)

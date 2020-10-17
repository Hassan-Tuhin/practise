class Profile():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        
    @property
    def email(self):
        return f'{self.fname}{self.lname}@gmail.com'
    @property
    def fullname(self):
        if self.fname==None or self.lname==None:
            return'fullname not set.set it first'
        return f'{self.fname} {self.lname}'
    @fullname.setter
    def fullname(self,name):
        fname,lname=name.split(' ')
        self.fname=fname
        self.lname=lname
    @fullname.deleter
    def fullname(self):
        self.fname=None
        self.lname=None

hassan=Profile('Hassan','Tuhin')
hassan.fullname='G.H Tuhin'
print(hassan.fullname)
del hassan.fullname
print(hassan.fullname)
hassan.fullname='HHHH TTTT'
print(hassan.fullname)


#hassan.lname='Byt'
#print(hassan.email)
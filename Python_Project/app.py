class Mammal():  #it's the parent class
    def walk(self):
        print("Walk")


class Dog(Mammal):#We pass Mammel here as parent class.so all of the features of Mammal can be used by this class
    def pet(self):
        print("is a pet")


class Cat(Mammal):
    pass

dog=Dog()
dog.walk()#This is Mammal class method & we can ue it here by inheritance
dog.pet()#This is the method of Dog class

cat=Cat()
cat.walk()

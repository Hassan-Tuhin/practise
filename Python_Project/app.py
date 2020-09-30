class point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        print("move")
    def name(self):
        print("pass")

point2=point(10,20)
print(point2.y)

point2.y=25
print(point2.y)
class A:
    a=10
    def __init__(self,name,age):
        print('self',self)
        self.name=name
        self.age=age
a1 = A('chiru',34)

class B(A):
    b=20
    def __init__(self,name,age):
        print('self',self)
        self.name=name
        self.age=age

obj1=B('balu',28)
print(obj1.__dict__)
print('obj1',obj1)
print(B.a,B.b)
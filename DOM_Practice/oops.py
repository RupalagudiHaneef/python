'''class A:
    a=10
class B(A):
    b=20

class C(B):
    c=30
class D(C):
    d=40

ob1=D()
print(ob1.a,ob1.b,ob1.c,ob1.d)'''



'''class Bank:
    bname='SBI'
    bloc='BSVN'

    def __init__(self,name,phno,eid):
        self.name=name
        self.phno=phno
        self.eid=eid
    def display(self):
        print(self.name,self.phno,self.eid,end=' ')

c1=Bank("Harika",9876543210,'h@gmail.com')
class Bank_details(Bank):
    founder='Sairam'

    def __init__(self,name,phno,eid,add,pan):
        super().__init__(name,phno,eid)
        self.add=add
        self.pan=pan

    def display(self):
        super().display()
        print(self.add,self.pan)

c1=Bank_details("Harika",9876543210,'h@gmail.com','hoodi','asdfg12345')
c1.display()



'''

'''class school:
    sname='ABC'
    sloc='E.city'

class College(school):
    cname='GPLN'
    cloc='Hoodi'

class Masters(College):
    uname='Jain'
    uloc='BSVN'

    @classmethod
    def display(cls):
        print(cls.sname,cls.sloc,cls.cname,cls.cloc,cls.uname,cls.uloc)
Masters.display()'''

'''class school:
    sname='ABC'
    sloc='E.city'

class College:
    cname='GPLN'
    cloc='Hoodi'

class Masters(College,school):
    uname='Jain'
    uloc='BSVN'

    @classmethod
    def display(cls):
        print(cls.sname,cls.sloc,cls.cname,cls.cloc,cls.uname,cls.uloc)
Masters.display()
print(Masters.mro())'''

#heirarchical inheritance
'''
class school:
    sname='ABC'
    sloc='E.city'

class College(school):
    cname='GPLN'
    cloc='Hoodi'
s1=College()

class Masters(school):
    uname='Jain'
    uloc='BSVN'
s2=Masters()

print(school.uname)
'''

##polymorphism

'''class Demo:
    @staticmethod
    def sam():
        print("Why are you cmg late")
    a=sam()

    @staticmethod
    def sam(a,b):
        print(a+b)
    b=sam
    @staticmethod
    def sam(a,b,c):
        print(a*b*c)
ob=Demo()
ob.a
ob.b(10,20)
ob.sam(10,20,30)'''
'''
class Demo:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return Demo(self.value+other.value)
print("--Addition of numbers---------")
a=Demo(100)
b=Demo(200)

c=a+b
print(c.value,type(c.value))

print("----concatenation---------")

s1=Demo("Hii ")
s2=Demo("Good Morning")

result=s1+s2
print(result.value,type(result.value))
'''

'''
class Bank:
    __deposit=10000000000
    def __init__(self,name,phone,acno):
        self.name=name
        self.phone=phone
        self.__acno=acno

b=Bank("raju",987345678,1234567)
print(b.name)
print(b._Bank__acno)##syntax to access private members

print(b._Bank__deposit) ##(obj._cname__var/method)
print(Bank._Bank__deposit)##(cname._cname__var/method)
Bank._Bank__deposit=200000000000
print(Bank._Bank__deposit)'''

'''class Bank:
    def __init__(self,name,bal):
        self.name=name
        self.__bal=bal

    def get_bal(self):
        return self.__bal

    def set_bal(self,amount):
        self.__bal=amount

    ##deposit

    def deposit(self,amount):
        self.set_bal(self.get_bal()+amount)

    ##withdraw

    def withdraw(self,amount):
        if amount<=self.get_bal():
            self.set_bal(self.get_bal()-amount)
            print("withdrwan successful ",amount)
        else:
            print("insufficient balance")

b=Bank("Raju",1000)
print("----Before---")
print(b.get_bal())
print("--------After--------")

b.deposit(1000)
print(b.get_bal())

print("------After withdraw------")

b.withdraw(2000)
print(b.get_bal())'''



from abc import ABC,abstractmethod

class Student(ABC):

    def __init__(self,name):
        self.name=name

    @abstractmethod
    def study(self):
        pass
    @abstractmethod

    def write(self):
        pass

class school(Student):

    def study(self):
        print(self.name,"studying")

    def write(self):
        print(self.name,"writing")

s1=school("Raju")
s2=school("kiran")

s1.study()
s2.study()














        


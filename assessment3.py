#Python program Inheritance
#Class Person

class person(object):

    #constructor
    def __init__(self, name):
        self,name = name

    #To get name
    def getName(self):
        return self.name
    
    #To check if this person is employee
    def isEmployee(self):
        return False

#Inherited or sub class(person in bracket)
class employee(person):

    #Here we return true
    def isEmployee(self):
        return True

#Driver code
# An Object of Person 
emp = Person("Geek1")   
print(emp.getName(), emp.isEmployee())

#An Object of Employee
emp = employee("Geek2")  
print(emp.getName(), emp.isEmployee())

#To Check Class and subclass
class Base(object):
    pass #Empty Class

class Derived(Base): 
    pass #Empty Class

#Driver Code
print(issubclass(Derived, Base))
print(issubclass(Base, Derived))

d=Derived()
b=Base()

#b is not an instance of Derived
print(isinstance(d,Base))

#But d is an instance of base
print(isinstance(d, Base))

# python objects and classes -> class is a blueprint(template) while an object is an instance of a class
#class helps us define how the structure of the object would be
# two characteristics of objects; attributes(names) and behaviours(methods)
# NB THAT SELF OR THIS IS THE INSTANCE CLASS (OBJ) WE ARE REFERRING TO, THIS CALLS THE VALUE OF THE OBJECT KEY 

class Car:
    #----- lets define our class variable (inside the class but outside the constructor), 
    # and when can this be important, when you want to figure out the amount of times your
    # class is called...lets call it public variables
    
    #category = category
    #amount = amount
    
    #create a constructor or what we call instance variable
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
        print( self.category)
        
    def can_speed(self):            #instance method
        print(f'flies past {self.amount}')
        
    @classmethod                   #classmethod
    def generaL_attr(cls):
        print('All have four legs')
        
    @staticmethod                  #static method
    def cry():
        pass
        


obj1 = Car('benz', 1500) # we need to pass in a matching set of arguments to our constructor placeholders 
obj2 = Car('toyota', 4500)

obj1.can_speed()
obj2.can_speed()
obj1.generaL_attr()
obj2.generaL_attr()







# Inheritance and compositions   -----------------------------------------------------

#inheritance
# Let’s say you have a base class Animal and you derive from it to create a Horse class. 
# The inheritance relationship states that a Horse is an Animal. This means that Horse inherits the interface 
# and implementation of Animal, and Horse objects can be used to replace Animal objects in the application.

class BaseClass:
    pass


class SubClass(BaseClass):
    pass


#composition
# For example, your Horse class can be composed by another object of type Tail. 
# Composition allows you to express that relationship by saying a Horse has a Tail.
# when an attribute in a class, is actually a class as well


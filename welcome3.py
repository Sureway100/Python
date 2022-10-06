# python objects and classes -> class is a blueprint(template) while an object is an instance of a class
# two characteristics of objects; attributes(names) and behaviours(methods)
# NB THAT SELF OR THIS IS THE INSTANCE CLASS (OBJ) WE ARE REFERRING TO, THIS CALLS THE VALUE OF THE OBJECT KEY 

class Car:
    #category = category
    #amount = amount
    #create a constructor
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
        print( self.category)
        


obj1 = Car('shop', 1500) # we need to pass in a matching set of arguments to our constructor placeholders 
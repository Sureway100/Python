#this is week2


#functions--------------------------------------------------------------

#note -> Note the difference between parameters and arguments: 
# #Function parameters are the names listed in the function's definition(placeholders). 
#Function arguments are the real values passed to the function



def print_name(name, age, country):
    print(f'{name}, {age}, {country}')
    
    
#A positional argument means its position matters in a function call. A keyword argument is a function argument with a name label.

print_name('tom', 19, 'Canada')   #this is called positional arguments
print_name(country='nigeria', age=12, name='jerry')   #this is called keyword argument


def print_name(name, country, age=25):
    print(f'{name}, {age}, {country}')
    

# you can add default values to function parameters
print_name(country='nigeria', name='merry')
print_name('tom', 'Canada') 



def sumation(*args):   # with this you can put unlimited number of arguments
    print(args)
    xum = 0
    for i in args:
        xum += i
    return xum

b = sumation(1,2,3,4,5,6,7,8,9)
print(b)



#Decorator---------------------------------------------------------------------------

#A decorator is a design pattern in Python that allows a user to add new functionality to an existing 
# object without modifying its structure.


# define your deco function
# define your spicy conditions to the defined deco function
# call your function parameter inside your defined deco function
# return your deco function

def useDecora(function):
    print('using decorators')
    def check(a,b):
        if b == 0:
            print('this is not possible')
            return
        function(a, b)
    return check


@useDecora
def divide(a, b):
    return a / b

#remainder = useDecora(divide)

print('without ' , divide(10,0))


# how to use *args and **kwargs in a function-----------------------------------------
#*args => this is a non defined or specified number of arguments

def add(*anything):
    print(anything)   
add(1,2,3,4,5,6,7,8,9)
#output => (1, 2, 3, 4, 5, 6, 7, 8, 9)

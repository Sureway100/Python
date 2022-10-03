#this is week2


#functions

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
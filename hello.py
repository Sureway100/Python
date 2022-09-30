print('HELLO PYTHON, IS A NEW BEGINNING')
a = 10 #a is the variable and 10 is the object
print(a)
b = 10 * 2
c = 15 + 15
d = 'hello ' + 'good ' + 'goodmorning'
e = [2,3,4] + [5,6,7]

print(b)
print(c)
print(d)
print(e)

f = 'come here ' * 5;
print(f)

#--------------------------------------------------------------------------------------------------
if 15 < 25:
    print('yes this is true')
else:
    print('no not true')
 
#----     
DOB = 9  

pass
if DOB < 10:
    print('you are a child, go away')
    
elif DOB > 18:
    print('you can vote')
else:  
    print('wait for the court to decide')
    
    
    
#------------------------------- WHILE LOOP

number = 0
while number < 10:
    print(f"Number is {number}!")  #Then by using f-string, expression specified by {} will be replaced with it's value.
    number = number + 1
    
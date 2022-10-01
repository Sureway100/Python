from ast import For
from turtle import clear


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
    
    
#............................................. LIST
#list is same thing as array in other languages
#while 0 is th start index of the first item, -1 is the last item, -2 seconf to etc

item = [1, 'ada', True, 3, '2.5']
print(item[2])
print(item[-1])

#----------- functions used in list
#max, min, sum, len
data = [1,2,3,4,5,6,7,8,9]
print('list ', sum(data))
print(min(data))
print(max(data))
print(len(data))


    
    
#SLICING - to get a specific range of elements in a list [start:end]

dataInfo = [1,2,3,4,5,6,7,8,9]
print(dataInfo[:])
print(dataInfo[1:4]) #but dont print 4

print('reverse list ', dataInfo[::-1])
subdata = [x for x in dataInfo]
print(subdata)

subdata2 = [x for x in dataInfo if x > 5]
print(subdata2)

#this is using the regular for loop - method 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
#this is using list comprehension - method 2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] # the x infront is used in printing
print(newlist)

#methods you can you to manipulate a list and many more not listed
#append()
#insert()  => (x, y) => x is the index to select, y is the new value
#sort()
#count()
#remove()
#reverse

#--------------------------------------------------------------------Dictionaries 

addr = {
    "num" : 2,
    "street" : "adaGeorge"
}
print(addr)
#adding elements to dict
addr["state"] = "lagos"
print(addr)

print(addr["street"])

#methods you can you to manipulate a dict and many more not listed
#pop()
#clear()
#get() => same thing as retrieving
print(addr.keys())
print(addr.value())
print(addr.get("state"))
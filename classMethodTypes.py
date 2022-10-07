# Let’s begin by writing a (Python 3) class that contains simple examples for all three method types:

# class MyClass:
#     def method(self):
#         return 'instance method called', self

#     @classmethod
#     def classmethod(cls):
#         return 'class method called', cls

#     @staticmethod
#     def staticmethod():
#         return 'static method called'
# NOTE: For Python 2 users: The @staticmethod and @classmethod decorators are available as of Python 2.4 and this example will work as is. Instead of using a plain class MyClass: declaration you might choose to declare a new-style class inheriting from object with the class MyClass(object): syntax. Other than that you’re good to go.



# Instance Methods
# The first method on MyClass, called method, is a regular instance method. That’s the basic, no-frills method type you’ll use most of the time. You can see the method takes one parameter, self, which points to an instance of MyClass when the method is called (but of course instance methods can accept more than just one parameter).

# Through the self parameter, instance methods can freely access attributes and other methods on the same object. This gives them a lot of power when it comes to modifying an object’s state.

# Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute. This means instance methods can also modify class state.

# Class Methods
# Let’s compare that to the second method, MyClass.classmethod. I marked this method with a @classmethod decorator to flag it as a class method.

# Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.

# Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.

# Static Methods
# The third method, MyClass.staticmethod was marked with a @staticmethod decorator to flag it as a static method.

# This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).

# Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.

# Let’s See Them In Action!
# I know this discussion has been fairly theoretical up to this point. And I believe it’s important that you develop an intuitive understanding for how these method types differ in practice. We’ll go over some concrete examples now.

# Let’s take a look at how these methods behave in action when we call them. We’ll start by creating an instance of the class and then calling the three different methods on it.

# MyClass was set up in such a way that each method’s implementation returns a tuple containing information for us to trace what’s going on — and which parts of the class or object the method can access.

# Here’s what happens when we call an instance method:

# >>> obj = MyClass()
# >>> obj.method()
# ('instance method called', <MyClass instance at 0x10205d190>)
# This confirmed that method (the instance method) has access to the object instance (printed as <MyClass instance>) via the self argument.

# When the method is called, Python replaces the self argument with the instance object, obj. We could ignore the syntactic sugar of the dot-call syntax (obj.method()) and pass the instance object manually to get the same result:

# >>> MyClass.method(obj)
# ('instance method called', <MyClass instance at 0x10205d190>)
# Can you guess what would happen if you tried to call the method without first creating an instance?

# By the way, instance methods can also access the class itself through the self.__class__ attribute. This makes instance methods powerful in terms of access restrictions - they can modify state on the object instance and on the class itself.

# Let’s try out the class method next:

# >>> obj.classmethod()
# ('class method called', <class MyClass at 0x101a2f4c8>)
# Calling classmethod() showed us it doesn’t have access to the <MyClass instance> object, but only to the <class MyClass> object, representing the class itself (everything in Python is an object, even classes themselves).

# Notice how Python automatically passes the class as the first argument to the function when we call MyClass.classmethod(). Calling a method in Python through the dot syntax triggers this behavior. The self parameter on instance methods works the same way.

# Please note that naming these parameters self and cls is just a convention. You could just as easily name them the_object and the_class and get the same result. All that matters is that they’re positioned first in the parameter list for the method.

# Time to call the static method now:

# >>> obj.staticmethod()
# 'static method called'
# Did you see how we called staticmethod() on the object and were able to do so successfully? Some developers are surprised when they learn that it’s possible to call a static method on an object instance.

# Behind the scenes Python simply enforces the access restrictions by not passing in the self or the cls argument when a static method gets called using the dot syntax.

# This confirms that static methods can neither access the object instance state nor the class state. They work like regular functions but belong to the class’s (and every instance’s) namespace.

# Now, let’s take a look at what happens when we attempt to call these methods on the class itself - without creating an object instance beforehand:

# >>> MyClass.classmethod()
# ('class method called', <class MyClass at 0x101a2f4c8>)

# >>> MyClass.staticmethod()
# 'static method called'

# >>> MyClass.method()
# TypeError: unbound method method() must
#     be called with MyClass instance as first
#     argument (got nothing instead)
# We were able to call classmethod() and staticmethod() just fine, but attempting to call the instance method method() failed with a TypeError.

# And this is to be expected — this time we didn’t create an object instance and tried calling an instance function directly on the class blueprint itself. This means there is no way for Python to populate the self argument and therefore the call fails.

# This should make the distinction between these three method types a little more clear. But I’m not going to leave it at that. In the next two sections I’ll go over two slightly more realistic examples for when to use these special method types.

# I will base my examples around this bare-bones Pizza class:

# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients

#     def __repr__(self):
#         return f'Pizza({self.ingredients!r})'
 
# >>> Pizza(['cheese', 'tomatoes'])
# Pizza(['cheese', 'tomatoes'])
# Note: This code example and the ones further along in the tutorial use Python 3.6 f-strings to construct the string returned by __repr__. On Python 2 and versions of Python 3 before 3.6 you’d use a different string formatting expression, for example:

# def __repr__(self):
#     return 'Pizza(%r)' % self.ingredients
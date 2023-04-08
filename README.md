# python OOP

### Python Class and Object

creation of class is using `class` syntax folowed with class name. when we creating class we dont use paranthesis unless its inherit another class.

```python
class Employee:
    # class attribute
    name = ""
    age = 0    
```

create object of that class
```python
parrot1 = Employee()
```

after creating object use and assign class attribues 
```python
parrot1.name = "Jhon"
parrot1.age = 12
```

#### Class Constructor

Constructor method in python class not create by using class name as other language. It create by using
 ``` def __init__(self, parameters): ```
this syntax. ```__init__``` will create a constructor for the class and it will pass self as the first agument. __self__ is hidden parameter which we don't need to pass. 

example:

```python
class Employee:
    # constructor require first_name as parameter
    def __init(self, first_name):
        #first name will assign to fname object variable
        self.fname = first_name


#this will pass "jhon" as first parameter to Employee class
emp1 = Employee("Jhon")
print(emp1.fname)  # Jhon
```


#### Encapsulation
Encapsulation is one of the key features of object-oriented programming. Encapsulation refers to the bundling of attributes and methods inside a single class.

It prevents outer classes from accessing and changing attributes and methods of a class. This also helps to achieve data hiding.

##### Private Variables

private variables are creating using __ before variable.``` __rais_value ```

```python
class Employee:
    # constructor require first_name as parameter
    def __init(self, first_name, last_name):
        #first name will assign to fname object variable
        self.first_name = first_name
        self.last_name = first_name
        self.__salary = 5000
    
    def get_salary(self):
        print("{}".format(self.__salary)

    def set_salary(self, salary):
        self.__salary = int(salary)
#this will pass "jhon" as first parameter to Employee class
emp1 = Employee("Jhon", "doe")
emp1.__salary = 7000
emp1.get_salary() # 5000 
emp1.set_salary(10000)
emp1.get_salary() # 10000 
```

Here, we have tried to modify the value of __salary outside of the class. However, since __salary is a private variable, this modification is not seen on the output.

As shown, to change the value, we have to use a setter function i.e set_salary() which takes price as a parameter.



## Inheritance
Inheritance is a way of creating a new class for using details of an existing class without modifying it.

The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

```python
# base class
class Animal:
    
    def eat(self):
        print( "I can eat!")
    
    def sleep(self):
        print("I can sleep!")

# derived class
class Dog(Animal):
    
    def bark(self):
        print("I can bark! Woof woof!!")

# Create object of the Dog class
dog1 = Dog()

# Calling members of the base class
dog1.eat() # output-I can eat!
dog1.sleep() # output -I can sleep!

# Calling member of the derived class
dog1.bark() # I can bark! Woof woof!!
```

### Polymorphism

Polymorphism is another important concept of object-oriented programming. It simply means more than one form.

That is, the same entity (method or operator or object) can perform different operations in different scenarios.

```python

class Polygon:
    # method to render a shape
    def render(self):
        print("Rendering Polygon...")

class Square(Polygon):
    # renders Square
    def render(self):
        print("Rendering Square...")

class Circle(Polygon):
    # renders circle
    def render(self):
        print("Rendering Circle...")
    
# create an object of Square
s1 = Square()
s1.render() # output - Rendering Square...

# create an object of Circle
c1 = Circle()
c1.render() # output - Rendering Circle...
```


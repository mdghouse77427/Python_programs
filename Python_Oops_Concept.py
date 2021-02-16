#OOPS principles in python /Demo
#classes are user defined blue print are prototypes
#sum, multiplication,addition, Constant
#Class contain methods, variable, Instance variables, Contructors etc...
#Objects for your clasess
#When functions is used in calss is called as methods and Contructors
#if you use fuctions are indpendently is called as funtions
#If method is present inside the class you can't call method inside class.. you should come out the class and call method using it's name
#To call the method of the class you have to come out of the class and create object and call the method
#In class we can create 'N' no.of Objects no Matter how many variables in class
#There are Two variables you need to know One is class variables another one is Instance variable
#Wharever Variable you defined Imediatle in calss is called as Class variable
#Variable you defined inside the Contructors is called as Instance variables
#Class variables are Constant not matter how many variables you are created
#Instance Varable differ/Changing for every object Creation it's not impact on class variable
#"Self" variable is mandatory all the time wehn you are creating method are contructor
#In Python you never called Varable with thri name you should use self keyword to called instance variable
#Self is object refernce who is calling you
#How many arguments you are sending into the class that many arguments should ne in your constructor

#when you not defined any contructor one default contructor will create and attach to class

#NOTE : self keyword is mandatory for calling variable names into methods
#instance and class  variables have whole different  purpose
#Construtor name should be __init__

#How to declare class in Python

class Calculator:
	num = 100   #Class  Varable
	#default contructor should create using init
	def __init__(self, a, b):
		self.firstnumber = a   #firstnumber and secondnumber two variables are instance variables
		self.secondnumber=b
		print("I am called automaticaaly when object is created")	
	def getData(self): #To create method in python self should to pass as parameter
		print("I am executing as method in class")
	def summation(self):
		return self.firstnumber + self.secondnumber + Calculator.num
#How to create Object in Python
#In python to create Object of the class..Write class name add bracess() and assign to variable
obj = Calculator(2, 4)  #syntax to create objects in python
print(obj.getData())
print(obj.summation())
print(obj.num)

obj1 = Calculator(5, 4)  #syntax to create objects in python
print(obj1.summation())
print(obj1.num)
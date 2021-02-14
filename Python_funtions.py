#Funtions Concept

#In Python Funtion is a group of related statements that perform a specific task.
#In Python if you want to create a function use a keyword called 'def'

#Funtion declaration
def GreetMe():
	print("Greet me Good Luck")
	
#Fucation call
GreetMe()

#Prameterize Functions
print('***********parameterized funtion/contructor************')
def GreetMe(name):
	print("Greet me Good Luck " +name)
	
GreetMe("MD GHOUSE")

#Summ of two numbers
print("***********Method-1*************")
def add(a, b):
	print("{} , {}".format("Summ of two numbers is" , a+b))
	
add(2,5)

print("***********Method-2*************")
def AddIntegers(c,d):
	return(c+d)
	
print(AddIntegers(5,5))

#def is the idenfier to reated function and colon(:) is mandatory to end the function after you declared function
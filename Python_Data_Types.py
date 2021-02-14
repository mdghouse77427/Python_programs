#In Python There are 5 Data types 
# 1. Numeric(int , long , float ,complex)
# 2. Sting (str)
# 3. Sequence types: list, tuple, range
# 4. Binary types: bytes, bytearray, memoryview
# 5. Mapping data type: dict [DICTIONARY]
# 6. Boolean type: bool
# 7. Set data types: set, frozenset

# Numeric Data type EXAMPLE

#create a variable with integer value.
a=100
print("The type of variable having value", a, " is ", type(a))

#create a variable with float value.
b=10.2345
print("The type of variable having value", b, " is ", type(b))

#create a variable with complex value.
c=100+3j
print("The type of variable having value", c, " is ", type(c))


# String DATA TYPE

a = "string in a double quote"
b= 'string in a single quote'
print(a)
print(b)

# using ',' to concatenate the two or several strings
print(a,"concatenated with",b)

#using '+' to concate the two or several strings
print(a+" concated with "+b)

#LIST DATA TYpe EXAMPLES

a = "string in a double quote"
b= 'string in a single quote'
print(a)
print(b)

# using ',' to concatenate the two or several strings
print(a,"concatenated with",b)

#using '+' to concate the two or several strings
print(a+" concated with "+b)


# TUPLE DATA TYPE

#tuple having only integer type of data.
a=(1,2,3,4)
print(a) #prints the whole tuple

#tuple having multiple type of data.
b=("hello", 1,2,3,"go")
print(b) #prints the whole tuple

#index of tuples are also 0 based.

print(b[4]) #this prints a single element in a tuple, in this case "go"


#DICTIONAR DATA TYPE

#a sample dictionary variable

a = {1:"first name",2:"last name", "age":33}

#print value having key=1
print(a[1])
#print value having key=2
print(a[2])
#print value having key="age"
print(a["age"])


#LIST DATA TYPE EXAMPLE Practice:

#NOTE : In Python LIST DATA Type we can pass any type Data like String ,Integer that is the beauty of python
 # Using LIST Data type it should be in Square brackets
 # List Index is Start from 0[Zero Index value]

values = [1, 2, "Hellow", 1] 
#List is data type that allows multiple values and can be different data types
print(values)
print(values[0])  #1

print(values[2]) #Hellow

print(values[-1]) #1
#Here -1 is used to print Last value of the Array index

#Printing Sub-index values of LIST
print(values[1:3]) #2,Hellow Last Index value 3 will be exclusive

#How add New values/String in the list

values.insert(2,  "Ghouse") #[2, 'Hellow']
values.insert(3, "MD") #[1, 2, 'Ghouse', 'MD', 'Hellow', 1]
print(values)

#If you want to add any value in the last Index use "append" Keyword
values.append("END") #[1, 2, 'Ghouse', 'MD', 'Hellow', 1, 'END']

print(values)

#Replacing/UPDATING any Existing values in The LIST INDEx
values[4] = "HELLOW"
print(values)  #[1, 2, 'Ghouse', 'MD', 'HELLOW', 1, 'END']

#Deleting the Values in INDEX/LIST
del values[0]

print(values) #[2, 'Ghouse', 'MD', 'HELLOW', 1, 'END']

#values[4, 1] = "0" , "1"   # U can't add multiple data at a time in list for that you have to use TUPLE DATA TYPE
#print(values)


#Diference Between LIST and TUPLE

#LIST and TUPLE Does Same thing
#1. TUPLE Data type is IMMUTABLE and LIST Data type is Not-Immutable
#When you Declare the TUPLE[IMMUTABLE] You can't update is agian
# IMMUTABLE means You can't change existing Behaviour, Like When you Declare Variable/Values that is locked you can't Modify it
#In LIST we change the Existing Behaviour Like : Updating Values With Capital letters in LIST

#Tuple use Braces()  To declare Tuple   Every thing same which you declare in lilst

# TUPLE - same as LIST Data type But Immutable

val = (12, "Mahammad", "MD", 24.5)
print(val)
print(val[1])

#val[1] = "MAHAMMAD" #TypeError: 'tuple' object does not support item assignment   We can't update Tuple data-typ

 
#DICTIONARY DATA-TYPE is Combination LIST and TUPLE In Terms of Key:Value Pair

#For Declaring DICTIONARY Data type should use flower Bracket {}

#DICTIONARY
#----------------
dic = {"a" : 2, 4 : "gh", "name" : "md ghouse"}

#Here a is the key and 2 is the Value
#When you are using key(a) as string it should be in double quote's "a"
#When you are using Values(gh) as string it should be in double quote's 
#we can use key and Value pair as same Data-type..
#Dictionary don't use index's it's have different combinations
#Dictionary takes keys and Values to print index values not using any LIst Indexes
print(dic)

print(dic[4])
print(dic["a"])

#By Using key reference we can print thr Values in dictionary
#List uses [] , Tuple uses () , Dictionary uses {}


#How to create Dictionary Dynamically at Run time 

#Create one Variable using  dictionary syntax add as mentioned below

dict = {}   #Create one Empty Dictionary

dict["name"] = "Mahammad Ghouse"  # Add value in Empty Dictionary dic[name] is key and assigned "Mahammad Ghouse" as value in that dictionary

#To add key:Values in dictionary take value and assign to that dictionary

dict[4] = "Roll Number"
print(dict)  #{'name': 'Mahammad Ghouse', 4: 'Roll Number'}

dict[1, "Adress", "GENDER"] = "2", "Chinnamande", "MALE"
print(dict) # {'name': 'Mahammad Ghouse', 4: 'Roll Number', (1, 'Adress', 'GENDER'): ('2', 'Chinnamande', 'MALE')}

dict["Family Members"] = "5"
print(dict)  # {'name': 'Mahammad Ghouse', 4: 'Roll Number', (1, 'Adress', 'GENDER'): ('2', 'Chinnamande', 'MALE'), 'Family Members': '5'}
print(dict["Family Members"])

del dict['name']
print(dict)

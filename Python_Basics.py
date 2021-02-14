print("Hello World")

# here are the comments i have defined

a = 3
 
print(a)


str = "My name is Ghouse"


b , c, d = 5 , 6.7 , "Hello"

#print("Values are " +b , +c, +d  )

# In Python We can't use '+' Symbol to concatennate WHich having differnet data type , We can concatennate same data type in Python which having same Data type
# We can use Symbol Coma(,) and Plus(+) Symbol To concatennate in Python Both Variable should have same data type


# Concatenate String to String 

E="Concatenate Variable"
F="Concatenate Another Variable"
print("data type of variable"+E ,"data type of variable"+F)

#Concatenate integer to integer
G , H = 10 , 11
print(G,H)
#NOTE : We can Only Concatenate String to String and Integer to Integer {Which having same data type}
# We have to use flower braces{} and format method

print("{} {} {} {} ".format("Values are ", b , c , d))

#If you want to know How python Treating Variable taking which type data type use below statement to know

print(type(b))

print(type(c)) 

print(type(d))

# To know about the Data types in Python go through this Link https://www.journaldev.com/14036/python-data-types
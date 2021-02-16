#Basically we use Exception handling When something is wrong Refer example given below
#In python for raising Exception we are using raise exceotion method

ItemsInCart = 0
#2 items will be aaded to cart
if ItemsInCart != 2:
	raise Exception("Products cart count not matching")


#There is another way to write exceotion using assertion method
#When the Testcase condition is not mate you can fail that testcase explicitly for that use assertion

 #raise Exception("Products cart count not matching")
    pass  #pass ia key word it wwill pass the coindition even there is nothing to validate in python

assert (ItemsInCart == 0)  #when ever assert recives false condition it will break your test


#try catch mechanism
#try method is used to validate error and send it to another block further execution another block called catch[in python we use as except]

# try catch

try:
    with open("google.txt", 'r') as reader:
        reader.read()
except:
    print("Some how i reached  this block because there is failure in try block")  # this is customized error we are printig


# if you want to print what python throughs exception erros

try:
    with open("google.txt", 'r') as reader:
        reader.read()
except Exception as e:
    print(e)  # this is customized error we are printig

#finally 
#This keyword will use when try and except/catch blocks are used
#finally keyword in python it will work when any line of code is stuck it will come untill the finally block reached
#In any exception block stuckare passed still the finally block should be print
#finally keyword is used to clear the records after completing the work reading record to delete that record we use finally keyword

# if you want to print what python throughs exception erros

try:
    with open("google.txt", 'r') as reader:
        reader.read()
except Exception as e:
    print(e)  # this is customized error we are printig

finally:
     print("Cleanig up record")
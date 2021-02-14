#if and else Conditions

#NOTE : Here if-else condition havind some difference compare to other languages
#Here If and else block should use colon(:) and Python is completly Code indendation , we are jot using any braces for condition and loops 
#Code Indentation Means python have some standards like when writing some code under ant if, else and loops , methos should enclosed with colon(:) , should write logic under the block which having spaces
#Example

greeting = "Good Morning"
if greeting == "good":
	print("Conditions Matches")
	print("seconde line")
else:
	print("Condition not matched")
print("if and else condition code coompleted")

#NOTE : For Every bolck should enclosed with colon(:) if not it throughs error
#Use TAB to write code in blocks

a = 3 
b = 3
if a == b:
	print("Conditions Matches")
	print("seconde line")
else:
	print("Condition not matched")
print("if and else condition code coompleted")

print('*********************************')
a = 3 
b = 3
if a > b:
	print("Conditions Matches")
	print("seconde line")
else:
	print("Condition not matched")
print("if and else condition code coompleted")

print('*********************************')
#Loops Concept

#for loop
#for loop is Iterate untill it Reache range what we given
#for <variable name like i , j..> in <object name/Listname which you declared> :(Colon is mandatory)

list = [2,3,4,5,6]
for i in list:
	print(i)
#Print Multiples of 2
print('*********************************')
for i in list:
	print("Multiples of 2 is :" , i*2)
	
#Sum of first five natural number 1+2+3+4+5=15
sum = 0
for j in range(1,6):  #range(i,j) this iterates(->) i to j-1
	sum=sum+j
	print(sum)
print('*********************************')
#In THis program we printed sum of natural number which added +1

#If we want to add summation with +2 increment
sum1 = 0
for k in range(1,6,2):
	sum1=sum1+k
	print(sum1)

#If we don't declare intial declare it will declare n-1
print('************SKIP FIRST INDEX*******************')	
for l in range(10):  #it will Iterate from 0 to n-1
	print(l)
	
	
#While loops Concept
#While loops are used to check Condition If the Condition is True it Keep on execute loop what we declared in the loop 
#In WHile loop if the condition is not true it will go inside the while loop 
#If the While loop condition is true then only it will run the while loop
# While will Execute untill the Condition become false

print('*******While-Loop**********')

it = 4
while it>1:
	print("My  name is ghouse")
	it = it-1
	
print("While loop execution is done")

#in While loop we can write the if and else conditions

#Exampe i don't want to print 3-number i want to print only o,1,2,4
print('********expect one number***********')

num =4
while num>1:
	if num!=3:
		print(num)
	#else:
	num=num-1

print('************using Break statement*************')
#In WHile loop they are two key words break and continue
#Break keyword/statement is used to halt loop abropitly/Halt your execution
#we can use muliple if conditions in while loop

num =10
while num>1:
	if num==3:
		break
	print(num)
	num=num-1
	
print('************using continue statement*************')

#we can use continue statement used to skip current iteration to continue second Iteration
#continue statement is skip that specific Iterarion and repeat and compare another condition and perform another Iteration
num =10
while num>1:
	if num ==10:
		num = num-1  #reducing one values should be mandatory using while 
		continue  #Here ti skips this Iteration and goes back to while loop to check another condition and to peroform another Iterarion
	if num==3:
		break  #after break statmet it should not goto another Iteration/statement it stops at the same break statement itself then it comes out of the while loop
	print(num)
	num=num-1	
	
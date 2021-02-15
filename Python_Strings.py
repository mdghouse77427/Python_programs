#String functions is similar to List 

#In String each and every character treated as same in List... In string Character is start from 0th Index

str = "Mahammad Ghouse"
str1 = "MD"
str2 = "Ghouse"
print(str[2]) #h

#If you want to print only sub string
# Let's say i want to print only "mmad"
#If you want to extratc sub-string from whole string

print(str[4:8])  #mmad  , if you want to print sustring in python

#How to concatenate one string to another string

#If you want to concatenate same data type it's simple using + operator

print(str+str1)  #Concatenation

#If you want to check one particular string is present in this full string name

print(str2 in str)

print(str2 in str1)  #substring check

#How split string and How tom trim that string

#If i want to split string based upon using space
var = str.split(" ")

print(var)

#If you want to extract particular string from var

print(var[0]) #Mahammad

#Trim is basically used to remove spacs from starting and end of your string

#In python to remove spaces we have to use " strip " method

str3 = "  Ghouse  "
print(str3.strip())

#If your requirement is just remove the beginig white spaces not the ending white spaces
#if you just pass strip it will remove all spaces in string
#To remove beginig white space of your string you have to use keyword/method lstrip
#To remove end white space of your string you have to use keyword/method rstrip
print(str3)
print(str3.lstrip())
print(str3.rstrip())
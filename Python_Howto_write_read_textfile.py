#How to Read write data in text file in python
#In python there is a method to to read and write data called "open"
#When you are opening any file make sure that you are closing that file that is good practice
#if you not close text file there will be memory leaks , your file will be corrupted
#Difference between readline and readlines readline will read only one line present in text fiile
#read lines method used to read all lines present in textfile 
#read lines method workd like it will read all content present in textfile and store into readlins method assign that in one variable and use for loop extract vale form list


file = open("test.txt")
#Read all contents of file
 #print(file.read())
#read N number charatecr by passing parameter
#print(file.read(5))

#Read content in file by line wise
#read one single line at a time readline()
#print(file.readline())
#print(file.readline())

#print line by line using readline method
#line = file.readline()
#while line!="":
#    print(line)
#    line = file.readline()


for line in file.readlines():
    print(line)
file.close()


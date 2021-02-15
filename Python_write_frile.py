#In python how to write file 
#in python we are opening file and seplaretly closing that file
#In python there is a method to open and close directly
#If you open any file how can you tell to python the file is read mode are write mode to indicate that we use two flags
#For read mode use flag as 'r' and for write mode use flag as 'w'


#read the file and store all the lines in list



with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open("test.txt", 'w') as writer:
        for line in reversed(content):
            writer.write(line)
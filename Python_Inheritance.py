#Inheritance

#Inheritance is Acquiring properties of Parent class
#If the Constructor is not Default make sure that you are calling parent Constructor in Child class Constructor
#We can call any variable , methods , constructor of Parent class in Child class

from Python_Oops_Concept import Calculator


class ChildImpl(Calculator):
    num2 = 200
    def __init__(self):
        Calculator.__init__(self, 2, 5)
    def getCompletedata(self):
        return self.num2 + self.num + self.summation()

obj = ChildImpl()
print(obj.getCompletedata())

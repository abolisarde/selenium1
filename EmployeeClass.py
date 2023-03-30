
class Employee:
    empid = 101
    name = "Shubham"
    address = "Pune"

    def getInfo(self):
        print(f"Info : empId : {self.empid}, Name : {self.name}, address :{self.address}" )

    def updateInfo(self, empid : int, name :str, address : str) -> str: 
        self.empid = empid
        self.name = name            # emp.name = "Nikhil"
        self.address = address

emp = Employee()
emp.getInfo()       #Info : empId : 101, Name : Shubham, address :Pune

emp.updateInfo(2002, "Nikhil", "Mumbai")
emp.getInfo()       #Info : empId : 2002, Name : Nikhil, address :Mumbai

emp.updateInfo("DummyId", 1111, 100.33) ## python is not type strict or not strongly typed, we can pass any type of arguemtn to any type of parameter
emp.getInfo()       #Info : empId : DummyId, Name : 1111, address :100.33

emp2 = Employee()
emp2.getInfo()      #Info : empId : 101, Name : Shubham, address :Pune
emp2.updateInfo(3003, "Ashish", "Nagpur")
emp2.getInfo()      #Info : empId : 3003, Name : Ashish, address :Nagpur

emp.getInfo()       #Info : empId : DummyId, Name : 1111, address :100.33


emp2 = Employee()       ## default values from class
emp2.getInfo()      ## Info : empId : 101, Name : Shubham, address :Pune
emp2.address = "Kolhapur"

emp3 = Employee()       ## default values from class
emp3.getInfo()      ## Info : empId : 101, Name : Shubham, address :Pune
###==========================================================================

Employee.name  = 'Amol'     ## we are updating to class attribute
Employee.address  = 'UK'     ## we are updating to class attribute


print(Employee.name)        ##Amol
print(emp.name)             ##1111      ## latest value of emp.name 
print(emp2.name)            #Amol
print(emp3.name)            #Amol

print(Employee.address)        ##UK
print(emp.address)             ##100.33      ## latest value of emp.name 
print(emp2.address)            #Kolhapur
print(emp3.address)            #UK




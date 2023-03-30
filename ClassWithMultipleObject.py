class Employee:
    empid = 101
    name = "Shubham"
    address = "Pune"

    def getInfo(self):
        print(f"Info : empId : {self.empid}, Name : {self.name}, address :{self.address}" )

    def updateInfo(self, empid : int, name :str, address : str): 
        self.empid = empid
        self.name = name            # emp.name = "Nikhil"
        self.address = address

emp = Employee()
emp.getInfo()  
emp.company = "Apple"       ##assignment
print(emp.company)

emp2 = Employee()
emp2.getInfo()  
## retrival
print(emp2.company)     ## error since emp2 dont have company attribute



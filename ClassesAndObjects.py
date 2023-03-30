
# empid = 1001        ## variable
# name = 'Amol'       ## variable
# address = 'Nagar'   ## variable
# salary = 3000000    ## variable


# def getEmployeeInfo():      ## user defined Function ## signature /defination
#     print(f"Empid : {empid}, Name : {name}, Address :{address}, salary :{salary}")

# getEmployeeInfo()       ## Function call 

# salary = 4000000        # varible 
# getEmployeeInfo()       ## Function call 


###=============================================================================================

class Employee:     ## class => keyword , Employee => Class name , Class name has to be First char should be captial
    
    empid = 1001        ## attribute
    name = 'Amol'       ## attribute
    address = 'Nagar'   ## attribute
    salary = 3000000    ## attribute

    ## without self method
    def getCompanyName():       # we are not using class attribute in this method so we not passing self as first argument
        print("Credence")
    # # # def getEmployeeInfo():      ## user defined Method ## signature
    # # #     print(f"Empid : {empid}, Name : {name}, Address :{address}, salary :{salary}")
    
    ## self : is a first parameter to method if you want to access class attribute
    ## self : it is not mandatory to have name as self, it can be anything like selfie or anything
    def getEmployeeInfo(self):      ## user defined Method ## signature
        print(f"Empid : {self.empid}, Name : {self.name}, Address :{self.address}, salary :{self.salary}")
    
    # # # getEmployeeInfo()    # We are calling method within class itself, we should call it from outside

    # # # getCompanyName()     # We are calling method within class itself, we should call it from outside

## now we are outside of class

## First approach
# emp = Employee()        ### Employee is class and emp is object
# Employee.getEmployeeInfo(emp)    # We are calling method by class name

# Employee.getCompanyName()     # We are calling method within class itself, we should call it from outside

# print(Employee.name)

## Second approach 

emp = Employee()  ## object creation of Employee class

### emp.getCompanyName()
    ## self : is a first parameter to method if you want to access class attribute
    ## self : it is not required to have name self, it can be any name and object will be automatically passed in self by python 
    ## self : class object
emp.getEmployeeInfo()       ##  self is not required when we are not dealing/using with attributes


a = "welcome"   ##  a is object for str class
a.capitalize()  ## capitalize(self)  a will be passed into self by python automatically

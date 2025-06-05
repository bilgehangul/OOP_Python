def num_format(num):
        if num == int(num):
            return "%.1f" % num
            
        elif num*10 == int(num*10):
            return "%.1f" % num
        else:
            return "%.2f" % num

class Employee:
    counter = 1
    def __init__(self,name,hours_worked=0.0,pay_rate=0.0):
        self.id = Employee.counter
        self.name = name
        self.hours_worked = hours_worked
        self.pay_rate = pay_rate
        Employee.counter +=1
        
    def getRate(self):
        return self.pay_rate
    def getEID(self):
        return self.id
    def getName(self):
        return self.name
    def getHours(self):
        return self.hours_worked
    def getGrossPay(self):
        return self.hours_worked*self.pay_rate
    def setRate(self,rate):
        self.pay_rate = rate
    def setHours(self,hours):
        self.hours_worked = hours
    

    def __eq__(self,ID):
        return self.id == ID
    def __str__ (self):
        return ("Employee Name: %s\nEmployee ID: %d\nHourly Rate: %s\nHours Worked: %s\nGross Pay: %s\n"%(self.name,self.getEID(),num_format(self.pay_rate),num_format(self.hours_worked),num_format(self.getGrossPay())))

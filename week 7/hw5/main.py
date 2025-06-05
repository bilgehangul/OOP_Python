from re import A
from linkedList import  *
from employee import *

print("*** CS 172 Payroll Simulator ***")

choice = ""
employee_list = []
while choice!="f":
    
    print("a. Add New Employee")
    print("b. Enter Employee Hours")
    print("c. Update Employee Hourly Rate")
    print("d. Display Payroll")
    print("e. Remove Employee from Payroll")
    print("f. Exit the program")
    
    
    choice = input("Enter your choice:")

    if choice == "a":
        name = input("Enter the new employee name:")
        h_rate = float(input("Enter their hourly rate:"))
        new_employee = Employee(name,0.0,h_rate)
        
        
        employee_list.append(new_employee)

        print("Employee",new_employee.getEID(),"added to payroll")
    elif choice == "b":
        for i in employee_list:
            hours_worked = input("Enter hours worked for employee %d: "%(i.getEID()))
            i.setHours(float(hours_worked))
    elif choice == "c":
        emp_id = int(input("Enter employee ID:"))
        found = False
        for i in employee_list:
            if i.getEID()==emp_id:
                new_wage = input("Enter new wage for employee %d:"%(i.getEID()))
                i.setRate(float(new_wage))
                found = True
        if found==False:
            print("Employee doesn't exist.")
    elif choice=="d":
        print("*** Payroll***")
        for i in employee_list:
            print(i)
    elif choice == "e":
        emp_id = int(input("Enter employee ID:"))
        found = False
        for i in employee_list:
            if i.getEID()==emp_id:
                employee_list.remove(i)
                found = True
        if found==False:
            print("Employee doesn't exist.")
    elif choice=="f":
        print("Goodbye.")

        




from stackclass import Stack

def postfix(exp):
    nums = Stack()
    nums.push(0)
    exp = exp.split(" ")
    for i in exp:
        if exp=="exit":
            return ""
        elif i.isdigit():
            i = int(i)
            nums.push(i)
        elif (i=="+"):
            a = nums.pop()
            b = nums.pop()
            result = a+b
            nums.push(result)
        elif  i=="-":
            a = nums.pop()
            b = nums.pop()
            result = b-a
            nums.push(result)
        elif i=="*":
            a = nums.pop()
            b = nums.pop()
            result = a*b
            nums.push(result)
        elif i=="/":
            a = nums.pop()
            b = nums.pop()
            result = b/a
            nums.push(result)
        else:
            i = int(i)
            nums.push(i)
    return float(result)

            
            




if __name__ == "__main__": 
        
    print("Welcome to Postfix Calculator")
    print("Enter exit to quit")
    exp = input("Enter Expression\n")
    while not exp=="exit":
        print("Result:",postfix(exp))
        exp = input("Enter Expression\n")

    




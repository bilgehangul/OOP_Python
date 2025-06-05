from fraction import *

def H(n):
    number = Fraction(0,1)
    for i in range(1,n+1):
        number += Fraction(1,i)
    return number

def T(n):
    number = Fraction(0,1)
    a = 0
    for i in range(n+1):
        a = Fraction(1,2)**i
        number +=a
    return number

def Z(n):
    number = Fraction(0,1)
    sol = Fraction(2,1)
    for i in range(n+1):
        sol -= Fraction(1,2)**i
    return sol
    
def R(n,b):
    num = Fraction(0,1)
    for i in range(1,n+1):
        num +=Fraction(1,i)**b
    return num

if __name__ == "__main__":
    
    print("Welcome to Fun with Fractions!")
    b = True
    while b:
        try:
            iterations = int(input("Enter Number of iterations (integer>0):\n"))
            if iterations<=0:
                print("Bad Input")
            else:
                b = False
        except TypeError:
            print("Bad Input")
            
    print("H(%d)=%s"%(iterations,H(iterations)))
    print("H(%d)~=%.8f"%(iterations,H(iterations).approximate()))
    print("T(%d)=%s"%(iterations,T(iterations)))
    print("T(%d)~=%.8f"%(iterations,T(iterations).approximate()))
    print("Z(%d)=%s"%(iterations,Z(iterations)))
    print("Z(%d)~=%.8f"%(iterations,Z(iterations).approximate()))
    print("R(%d,%d)=%s"%(iterations,iterations,R(iterations,iterations)))
    print("R(%d,%d)~=%.8f"%(iterations,iterations,R(iterations,iterations).approximate()))
    
    
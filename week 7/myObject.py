#File:     myObject.py
#Purpose:  Simple class MyObject to demostrate the hash method and hash tables
#Author:   Adelaida A. Medlock
#Date:     Febraury 27, 2020

class MyObject():
    def __init__(self, value):
        self.__value = value
    
    def getValue(self):
        return self.__value
        
    def __hash__(self):
        return ord(self.__value) - 32
    
    def __str__(self):
        return ('Value of my object: ' + str(self.__value))


# main script to test linked list class
if __name__ == "__main__":
    sampleObj = MyObject('A')
    print(sampleObj)
    print('Hash value for my sampleObject is:', hash(sampleObj))
    
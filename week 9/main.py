import random
from BST import *


def populateList(n,s):
    lst = []
    for i in range(n):
        lst.append(i)
    random.seed(s)
    random.shuffle(lst)
    return lst 


def searchLength(lst, n):
    count = 1
    for i in lst:
        if i == n:
            return count
        else:
            count +=1
    return len(lst)
        
def listToBST(lst):
    bstobject = BST()
    for i in range(len(lst)):
        bstobject.append(lst[i])
    return bstobject


if __name__ == "__main__":
    avgoflist = []
    avgofbst = []

    for n in range(1,1000,100):
        sumcountlist = 0
        sumcountbst = 0
        for s in range(1,5):
            lst = populateList(n,s)
            bst = listToBST(lst)

            for v in range(n):
                sumcountlist+=searchLength(lst,v)
                sumcountbst +=bst.searchLength(v)
        avgoflist.append(sumcountlist/(4*n))
        avgofbst.append(sumcountbst/(4*n))
    print("Average Search Length for List:",avgoflist,"Average Search Length for BST:",avgofbst)
	
		
		
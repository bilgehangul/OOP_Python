class Item:
    
    __name = ""
    __price = 0.0
    __taxable = False
    
    def __init__(self,__name,__price,__taxable):
        self.__name = __name
        self.__price = __price
        self.__taxable = __taxable
        
    def getPrice(self):
        return self.__price
    
    def getTax(self,tax_rate):
        if self.__taxable == True:
            return (tax_rate*self.__price)/100
        else:
            return self.__taxable
        
    def __str__(self):
        string = "{:_<20}".format(self.__name)+"{:_>20}".format(self.__price)
        return string
    
class Receipt:
    
    __tax_rate = 7.0
    __purchases = []
    
    def __init__ (self,__tax_rate):
        self.__tax_rate = __tax_rate
        
    def addItem (self,item):
        self.__purchases.append(item)
        
    def __str__ (self):
        total_tax = 0.0
        sub_total = 0.0
        total_cost = 0.0
        
        receipt = "----- Receipt time -----\n"
        
        for i in self.__purchases:
            
            total_tax += i.getTax(self.__tax_rate)
            sub_total += i.getPrice()
            
            receipt += str(i) + "\n"
            
        
        total_cost = sub_total + total_tax
        sub_total = "{:.2f}".format(sub_total)
        total_tax = "{:.2f}".format(total_tax)
        total_cost = "{:.2f}".format(total_cost)
        
        receipt += "\n" + "{:_<20}".format("Sub Total") + "{:_>20}".format(sub_total)+"\n" 
        receipt += "{:_<20}".format("Tax") + "{:_>20}".format(total_tax)+"\n"
        receipt += "{:_<20}".format("Total") + "{:_>20}".format(total_cost)
        return receipt
        
        

        
        




if __name__=="__main__":
    print("Welcome to Receipt Creator")
    add_item = "yes"
    receipt_object = Receipt(7.0)
    taxable = True
    
    while add_item == "yes":
        item_name = str(input("Enter Item name:"))
        item_price = float(input("Enter Item Price:"))
        is_taxable = str(input("Is the item taxable (yes/no):"))
        
        if is_taxable == "no":
            taxable = False
        
        item = Item(item_name,item_price,taxable)
        receipt_object.addItem(item)
        add_item = str(input("Add another item (yes/no):"))
    

    print(receipt_object)
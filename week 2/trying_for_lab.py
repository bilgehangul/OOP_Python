import datetime
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
    def getTax(self, tax_rate):
        tax = 0.0
        if self.__taxable:
            tax = (self.__price * tax_rate)/100
            return tax
        def __str__(self):
            price = "{:.2f}".format(self.__price)
            return "{:_<20}".format(self.__name)+"{:_>20}".format(price)
class Receipt:
    __tax_rate = 7.0
    __purchases = []
    
    
    
    def __init__(self,__tax_rate):
        self.__tax_rate = __tax_rate
        
        
    def addItem(self, item):
        self.__purchases.append(item)
        
        
    def __str__(self):
        receipt = "----- Receipt "+str(datetime.datetime.now())+" -----\n"
        total_tax = 0.0
        sub_cost = 0.0
        total_cost = 0.0
        for item in self.__purchases:
            receipt += str(item)+"\n"
            sub_cost += Item.getPrice(self)
            total_tax += Item.getTax(self.__tax_rate)
            
            
            
            
            
            
            
            
            
            
            
            
        total_cost = "{:.2f}".format(sub_cost+total_tax)
        sub_cost = "{:.2f}".format(sub_cost)
        total_tax = "{:.2f}".format(total_tax)
        
        receipt += "\n"
        receipt += "{:_<20}".format("Sub Total")+"{:_>20}".format(sub_cost)+"\n"
        receipt += "{:_<20}".format("Tax")+"{:_>20}".format(total_tax)+"\n"
        receipt += "{:_<20}".format("Total")+"{:_>20}".format(total_cost)
        return receipt
    
    
    
    
    
    
    
    
    
    
    
receipt = Receipt(7.0)
print("Welcome to Receipt Creator")
item_name = input("Enter Item name: ")
item_price = input("Enter Item price: ")
item_price = float(item_price)
item_taxable = input("Is the item taxable (yes/no): ")
if item_taxable == "no":
    item_taxable = False
else:
    item_taxable = True
item = Item(item_name,item_price,item_taxable)
receipt.addItem(item)
add_another_item = input("Add another item (yes/no): ")
while add_another_item == "yes":
    item_name = input("Enter Item name: ")
    item_price = input("Enter Item price: ")
    item_price = float(item_price)
    item_taxable = input("Is the item taxable (yes/no): ")
    if item_taxable == "no":
        item_taxable = False
    else:
        item_taxable = True
    item = Item(item_name,item_price,item_taxable)
    receipt.addItem(item)
    add_another_item = input("Add another item (yes/no): ")
print(receipt)
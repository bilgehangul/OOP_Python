class ItemToPurchase:
    
    def __init__(self,item_name = "none", item_price = 0, item_quantity = 0, item_description = "none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    def print_item_description(self):
        print("%s: %s"%(self.item_name,self.item_description))
    
    def print_item_cost(self):
        
        print("%s %d @ $%d = $%d"%(self.item_name,self.item_quantity,self.item_price,self.item_price*self.item_quantity))
        
class ShoppingCart:
    
    def __init__(self, customer_name = "none", current_date = "January 1, 2016", cart_items = []):
        self.customer_name =customer_name
        self.current_date =current_date
        self.cart_items = cart_items
        
    
    
    def add_item(self,itemToPurchase):
        self.cart_items.append(itemToPurchase)
        
        
    def remove_item(self,itemname):
        item_removed = False
        for i in self.cart_items:
            if i.item_name == itemname:
                self.cart_items.remove(i)
                item_removed = True
                break
            
        if not item_removed:
            print("Item not found in cart. Nothing removed.")
            
            
            
    def modify_item(self,itemToPurchase):
        item_modified = False
        
        for i in self.cart_items:
            
            if i.item_name == itemToPurchase.item_name:
                i.item_quantity = itemToPurchase.item_quantity
                item_modified  = True
        if not item_modified:
            print("Item not found in cart. Nothing modified.")
            
    
        
    
    def get_num_items_in_cart(self):
        total_quantity = 0
        for i in self.cart_items:
            total_quantity += i.item_quantity
        return total_quantity

    def get_cost_of_cart(self) :
        total_cost = 0
        for i in self.cart_items:
            total_cost += i.item_price * i.item_quantity
        return total_cost
    
    
    def print_total(self):
        cost = self.get_cost_of_cart()
        
        if cost == 0:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: %d' %self.get_num_items_in_cart())
            print("\nSHOPPING CART IS EMPTY")
            print('\nTotal: $%d' %(cost))
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: %d\n' %self.get_num_items_in_cart())
            for item in self.cart_items:
                total = item.item_price * item.item_quantity
                print('%s %d @ $%d = $%d' % (item.item_name, item.item_quantity, item.item_price, total))
              
            print('\nTotal: $%d' %(cost))
    
    def print_descriptions(self):
        cost = self.get_cost_of_cart()
        
        if cost == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print('{}\'s Shopping Cart - {}\n'.format(self.customer_name, self.current_date))
            print("Item Descriptions")
            for item in self.cart_items:
                item.print_item_description()
    










def print_menu(newCart):
    customer_Cart = newCart
    
    menu = ("\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n")
    
    command = ""
    
    while command != "q":
        print(menu)
        command = input('Choose an option:\n')
        while(command != 'a' and command != 'o' and command != 'i' and command != 'q' and command != 'r' and command != 'c'):
            command = input('Choose an option:\n')
        if(command == 'a'):
            print("ADD ITEM TO CART")
            item_name = input('Enter the item name:\n')
            item_description = input('Enter the item description:\n')
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))       
            itemtoPurchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            customer_Cart.add_item(itemtoPurchase)
              
        elif(command == 'o'):
            print('OUTPUT SHOPPING CART')
            customer_Cart.print_total()  
        elif(command == 'i'):
            print('OUTPUT ITEMS\' DESCRIPTIONS')
            customer_Cart.print_descriptions()
        elif(command == 'r'):
            print('REMOVE ITEM FROM CART')
            itemName = input('Enter name of item to remove:\n')
            customer_Cart.remove_item(itemName)
        elif(command == 'c'):
            print('CHANGE ITEM QUANTITY')
            itemName = input('Enter the item name:\n')
            qty = int(input('Enter the new quantity:\n'))
            itemToPurchase = ItemToPurchase(itemName,0,qty)
            customer_Cart.modify_item(itemToPurchase)




if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print("\nCustomer name: %s" %customer_name)
    print("Today's date: %s\n" %current_date)
    
    newCart = ShoppingCart(customer_name, current_date)
    
    print_menu(newCart)  

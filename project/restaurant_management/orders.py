class Order:
    def __init__(self):
        self.items={}
    
    def add_item(self,item):
        if item in self.items:
            self.items[item]+=item.quantity
        else:
            self.items[item]=item.quantity
        
    
    def remove_item(self,item):
        if item in self.items:
            del self.items[item]
    
    @property
    def calculate_total(self):
        return sum(item.price*quantity for item,quantity in self.items.items())
    
    def clear_cart(self):
        self.items={}
        print("Cart cleared successfully!")
 
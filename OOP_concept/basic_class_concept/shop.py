class Shop:
    cart=[]
    def __init__(self, buyer):
        self.buyer=buyer

    def add_to_cart(self, item):
        self.cart.append(item)

p1=Shop("meh jabeen")
p1.add_to_cart("shoes")
p1.add_to_cart("phone")

nisho=Shop("nisho")
nisho.add_to_cart("cap")
nisho.add_to_cart("watch")

print(nisho.cart)       
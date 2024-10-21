# create an item class
class Item:
    # create a class attribute to hold discount
    discount = 0.1
    # create a class constructor
    def __init__(self, item_name:str, price:float, quantity:int ):
        print(f"\nItem name: {item_name}")
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    # create a method to calculate the total price of the item
    def calculate_total_price(self):
        return self.quantityself.price
    
    # calculate discount on items
    def calculate_discount(self):
        if self.price > 1000:
            Item.discount = 0.3
            return self.price * Item.discount
        return self.price * Item.discount
    
    # calculte how much the item will cost after discount
    def calculate_amount(self):
        return self.price - Item.calculate_discount(self)


item1 = Item('MacBook', 1000, 3)
print(item1.calculate_amount())
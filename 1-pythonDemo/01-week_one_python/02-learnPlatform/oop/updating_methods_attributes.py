class Shoe:
    #now our method has 4 paramters(including self)
    def __init__(self,brand,shoe_type,price):
        #we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price 
        self.in_stock = True 
    
    #takes a flaot/percent as anargument and reduces the price of the item by that eprcentage
    def on_sale_by_percent(self, percent_off):
        self.price = self.price * (1-percent_off)
    
    # Returns a total with tax added to the price.
    def total_with_tax(self, tax_rate):
        tax = self.price * tax_rate
        total = self.price + tax
        return total
    
    # Reduces the price by a fixed dollar amount.
    def cut_price_by(self, amount):
        if amount < self.price:
            self.price -= amount
        else:
            print("Price deduction too large.")

# Create some shoes. Call some methods on those shoes. Print your shoe's attributes..
# my_shoe = Shoe("Converse", "Low-tops", 36.00)
# print(my_shoe.total_with_tax(0.05))
# my_shoe.cut_price_by(10)
# print(my_shoe.price)

laz_shoe = Shoe('nike','vaptormax2.0', 199.99)
laz_shoe.cut_price_by(78.99)
laz_shoe.on_sale_by_percent(.2)
print(laz_shoe.total_with_tax(0.099))

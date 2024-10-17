class Itemz:
    """
    A class to represent an item in the inventory.

    Attributes:
    name : str
        Name of the item.
    price : float
        Price of the item.
    qty : int
        Quantity of the item.
    category : str
        Category of the item, default is 'general'.
    env_fee : float
        Environmental fee, default is 0.
    """

    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty
        self.category = "general"
        self.env_fee = 0

    def gettotal(self):
        """
        Calculate the total price for the item based on the quantity.
        """
        return self.price * self.qty

    def getmostprices(self):
        """
        Calculate a discounted price at 60% of the total.
        """
        return self.price * self.qty * 0.6

class ShoppingCart:
    """
    A class to represent a shopping cart.

    Attributes:
    items : list
        A list to store items added to the cart.
    taxrates : float
        The tax rate applied to the items in the cart, default is 0.08.
    """

    def __init__(self):
        self.items = []
        self.taxrates = 0.08
        self.memberdiscount = 0.05
        self.bigspenderdiscount = 10
        self.coupondiscount = 0.15
        self.currency = "USD"

    def additem(self, item):
        """
        Add an item to the shopping cart.

        Parameters:
        item : object
            The item to be added to the cart.
        """
        self.items.append(item)

    def calculatesubtotal(self):
        """
        Calculate the subtotal for all items in the shopping cart.

        Returns:
        float: The subtotal price of all items.
        """
        subtotal = 0
        for item in self.items:
            subtotal += item.gettotal()
        return subtotal

    def applydiscount(self, subtotal, ismember, hascoupon):
        """
        Apply discounts to the subtotal based on membership and spending amount.

        Parameters:
        subtotal : float
            The current subtotal before discounts.
        ismember : bool
            Indicates if the customer is a member.
        hascoupon : bool
            Indicates if the customer has a coupon.

        Returns:
        float: The subtotal after discounts.
        """
        if ismember:
            subtotal = subtotal - (subtotal * self.memberdiscount)

        if subtotal > 100:
            subtotal = subtotal - self.bigspenderdiscount

        if hascoupon:
            subtotal -= subtotal * self.coupondiscount

        return subtotal

    def calculatetotal(self, ismember, hascoupon):
        """
        Calculate the total after applying discounts to the subtotal.

        Parameters:
        ismember : bool
            Indicates if the customer is a member.
        hascoupon : bool
            Indicates if the customer has a coupon.

        Returns:
        float: The final total after discounts.
        """
        subtotal = self.calculatesubtotal()
        subtotal = self.applydiscount(subtotal, ismember, hascoupon)
        total = subtotal + (subtotal * self.taxrates)
        return total

def main():
    """
    Main function to run the shopping cart total calculator.
    """
    cart = ShoppingCart()

    item1 = Itemz("Apple", 1.5, 10)
    item2 = Itemz("Banana", 0.5, 5)
    item3 = Itemz("Laptop", 1000, 1)  # Cambiado de string a número

    item3.category = "electronics"

    cart.additem(item1)
    cart.additem(item2)
    cart.additem(item3)

    ismember = True
    hascoupon = True

    total = cart.calculatetotal(ismember, hascoupon)

    if total < 0:
        print("Error in calculation!")
    else:
        print("The total price is: $" + str(int(total)))

if __name__ == "__main__":
    main()

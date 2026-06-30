# trolley.py
# This file contains the main logic for the Smart Trolley project.


# Step 1: Create the Item class
# Each item has a name, price, quantity, and category.

class Item:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    # Step 2: Calculate subtotal
    def subtotal(self):
        return self.price * self.quantity


# Step 3: Calculate total bill

def calculate_total(cart):
    total = 0

    for item in cart:
        total += item.subtotal()

    return total


# Step 4: Calculate discount
# Members get 10% discount.
# Non-members get 5% discount if they spend RM100 or more.

def calculate_discount(total, is_member):
    if is_member:
        return total * 0.10
    elif total >= 100:
        return total * 0.05
    else:
        return 0
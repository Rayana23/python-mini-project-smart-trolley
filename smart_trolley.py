# Simple Smart Trolley
# Final Project for Python 101

# In this project, we will build a small shopping trolley system.

# The program will:
# 1. Store shopping items
# 2. Store item prices
# 3. Store item quantities
# 4. Calculate subtotals
# 5. Calculate the total bill
# 6. Apply discounts
# 7. Display a receipt
# 8. Save the receipt to a text file
# 9. Add error handling
# 10. Turn the project into a Streamlit app later

# Step 1: Create an Item class
# A class is a blueprint for creating objects.
# Here, every item in the trolley will have:
# - name
# - price
# - quantity

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

         # Step 2: Create a subtotal method
         # Subtotal means price multiplied by quantity.
    def subtotal(self):
        return self.price * self.quantity
    
# Step 3: Create shopping items

item1 = Item("Milk", 8.50, 2)
item2 = Item("Bread", 4.00, 1)
item3 = Item("Eggs", 12.00, 1)
item4 = Item("Salmon",50.0,2)

# Step 4: Store items in a list
# This list represents the shopping cart.

cart = [item1, item2, item3, item4]

# Step 5: Create a function to calculate the total bill

def calculate_total(cart):
    total = 0

    for item in cart:
        total += item.subtotal()

    return total

# Step 6: Calculate discount.
# If the total is RM100 or more, apply 10% discount.
# Otherwise, there is no discount.
def calculate_discount(total):
    if total >= 100:
        return total * 0.10
    else:
        return 0



# Step 7: Save receipt
def save_receipt(cart, total, discount, final_amount):
    try:
        with open("receipt.txt", "w") as file:
            file.write("=========================\n")
            file.write("SMART TROLLEY RECEIPT\n")
            file.write("=========================\n\n")

            for item in cart:
                file.write("Item: " + item.name + "\n")
                file.write("Price: RM" + str(item.price) + "\n")
                file.write("Quantity: " + str(item.quantity) + "\n")
                file.write("Subtotal: RM" + str(item.subtotal()) + "\n\n")

            file.write("Total Bill: RM" + str(total) + "\n")
            file.write("Discount: RM" + str(discount) + "\n")
            file.write("Amount Payable: RM" + str(final_amount) + "\n")
            file.write("Thank you for shopping!\n")

        print("Receipt saved successfully.")

    except:
        print("An error occurred while saving the receipt.")

# Step 8: Run the program
total = calculate_total(cart)
discount = calculate_discount(total)
final_amount = total - discount

save_receipt(cart, total, discount, final_amount)
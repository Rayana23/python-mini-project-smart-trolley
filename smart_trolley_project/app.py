# app.py
# This file creates the Streamlit web app interface.


# Step 1: Import Streamlit

import streamlit as st


# Step 2: Import our own project logic

from trolley import Item, calculate_total, calculate_discount


# Step 3: Create the app title

st.title("🛒 Simple Smart Trolley")
st.write("Build a beginner-friendly shopping trolley using Python and Streamlit.")


# Step 4: Create session state
# Streamlit reruns the app whenever users interact with it.
# session_state helps us remember the cart items.

if "cart" not in st.session_state:
    st.session_state.cart = []


# Step 5: Create input fields

st.subheader("Add Item")

name = st.text_input("Item Name")

price = st.number_input(
    "Price (RM)",
    min_value=0.0,
    value=0.0,
    step=0.50
)

quantity = st.number_input(
    "Quantity",
    min_value=1,
    value=1,
    step=1
)

category = st.selectbox(
    "Category",
    ["Food", "Drinks", "Stationery", "Lifestyle", "Other"]
)


# Step 6: Add item button

if st.button("Add Item"):
    if name.strip() == "":
        st.warning("Please enter an item name.")
    else:
        item = Item(name, price, quantity, category)
        st.session_state.cart.append(item)
        st.success(name + " added to cart.")


# Step 7: Display shopping cart

st.divider()
st.subheader("Shopping Cart")

if len(st.session_state.cart) == 0:
    st.info("Your cart is empty.")

else:
    for item in st.session_state.cart:
        st.write(
            item.name
            + " | "
            + item.category
            + " | RM "
            + str(item.price)
            + " × "
            + str(item.quantity)
            + " = RM "
            + str(item.subtotal())
        )


# Step 8: Membership discount option

is_member = st.checkbox("I am a member")


# Step 9: Calculate totals

if len(st.session_state.cart) > 0:
    total = calculate_total(st.session_state.cart)
    discount = calculate_discount(total, is_member)
    final_amount = total - discount

    st.divider()
    st.subheader("Receipt Summary")

    st.metric("Total Bill", "RM " + format(total, ".2f"))
    st.metric("Discount", "RM " + format(discount, ".2f"))
    st.metric("Amount Payable", "RM " + format(final_amount, ".2f"))

    if final_amount > 200:
        st.warning("Budget warning: Your total is above RM200.")

    receipt_text = "SMART TROLLEY RECEIPT\n"
    receipt_text += "=====================\n\n"

    for item in st.session_state.cart:
        receipt_text += "Item: " + item.name + "\n"
        receipt_text += "Category: " + item.category + "\n"
        receipt_text += "Price: RM" + format(item.price, ".2f") + "\n"
        receipt_text += "Quantity: " + str(item.quantity) + "\n"
        receipt_text += "Subtotal: RM" + format(item.subtotal(), ".2f") + "\n\n"

    receipt_text += "Total Bill: RM" + format(total, ".2f") + "\n"
    receipt_text += "Discount: RM" + format(discount, ".2f") + "\n"
    receipt_text += "Amount Payable: RM" + format(final_amount, ".2f") + "\n"

    st.download_button(
        label="Download Receipt",
        data=receipt_text,
        file_name="receipt.txt",
        mime="text/plain"
    )


# Step 10: Clear cart button

if st.button("Clear Cart"):
    st.session_state.cart = []
    st.success("Cart cleared.")
    st.rerun()
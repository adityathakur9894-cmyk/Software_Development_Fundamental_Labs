# Webstore Purchase Checker
# Author: A. N. Other
# Date: March 2026

# Get user inputs
registered = input("Are you a registered user? (yes/no): ").strip().lower()
guest = input("Are you using a guest login? (yes/no): ").strip().lower()
cart_items = int(input("How many items are in your shopping cart? "))
gift_card = input("Are you purchasing a gift card? (yes/no): ").strip().lower()

# Convert inputs to boolean
is_registered = registered == "yes"
is_guest = guest == "yes"
has_items = cart_items > 0
buying_gift_card = gift_card == "yes"

# Check if purchase is allowed
if (is_registered and has_items) or (is_guest and buying_gift_card):
    print("\nPurchase allowed! You can proceed to payment.")
else:
    print("\nPurchase not allowed. You do not meet the requirements.")
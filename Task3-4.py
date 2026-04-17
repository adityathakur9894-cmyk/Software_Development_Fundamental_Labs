# Inventory data
inventory = {
    "101": {"name": "Laptop", "quantity": 10, "price": 800},
    "102": {"name": "Mouse", "quantity": 50, "price": 20},
    "103": {"name": "Keyboard", "quantity": 30, "price": 40}
}

# Task 3: Update Inventory
def update_inventory(item_id):
    if item_id in inventory:
        print("Item found!")

        new_quantity = int(input("Enter new quantity: "))
        new_price = float(input("Enter new price: "))

        inventory[item_id]["quantity"] = new_quantity
        inventory[item_id]["price"] = new_price

        print("Inventory updated successfully!")
    else:
        print("Item not found.")

# Task 4: Display Inventory Item
def display_inventory_item(item_id):
    if item_id in inventory:
        item = inventory[item_id]
        total_value = item["quantity"] * item["price"]

        print("\n--- Inventory Item Details ---")
        print("Item Name  :", item["name"])
        print("Item ID    :", item_id)
        print("Quantity   :", item["quantity"])
        print("Price      :", item["price"])
        print("Total Value:", total_value)
    else:
        print("Item not found.")


item_id = input("Enter Item ID: ")

update_inventory(item_id)
display_inventory_item(item_id)

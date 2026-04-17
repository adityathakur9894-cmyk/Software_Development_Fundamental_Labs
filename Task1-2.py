item_counter = 1000

# Task 1
def add_inventory_item():
    global item_counter
    
    print("Adding Inventory Item:\n")
    
    item_name = input("Item Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per Item: "))
    
    item_id = item_counter
    item_counter += 1
    
    print("\nItem Name:", item_name)
    print("Item ID:", item_id)
    print("Quantity:", quantity)
    print("Price per Item: $%.2f" % price)
    
    return item_name, item_id, quantity, price


# Task 2
def calculate_total_value():
    item_name, item_id, quantity, price = add_inventory_item()
    
    total_value = quantity * price
    
    print("\nTotal Value: $%.2f" % total_value)
    
    return total_value


# Run
calculate_total_value()
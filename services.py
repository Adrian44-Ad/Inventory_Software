# Module that stores all the service functions.



# Adds a product to the inventory. Returns False if the product already exists
def add_product(inventory, name, price, quantity):

    for product in inventory:
        if product["name"].lower() == name.lower():
            return False
        
        product = {
            "name"  : name,
            "price" : price,
            "quantity"  : quantity
        }

    return True

# Returns a list of strings in a readable format
def show_inventory(inventory):

    if not inventory:
        return ["The inventory is empty!"]
    
    result = []
    for product in inventory:
        line = f'''
            Product Name: {product['name']}
            Product Price: {product['price']}
            Quantity: {product['quantity']}
        '''

        result.append(line)

    return result

# Search for a product by name. Returns the product dictionary or None
def search_product(inventory, name):

    for product in inventory:
        if product["name"].lower() == name.lower():
            return product
    
    return None

# Update price and/or quantity. Returns True if updated, False if not found
def update_product(inventory, name, new_price = None, new_quantity = None):

    for product in inventory:
        if product["name"].lower() == name.lower():
            if new_price is not None:
                product["price"] = new_price
            if new_quantity is not None:
                product["quantity"] = new_quantity
            return True
        
    return False

# Delete a product. Returns True if deleted, False if not found
def delete_product(inventory, name):
    
    for i, product in enumerate(inventory):
        if product["name"].lower() == name.lower():
            del inventory[i]
            return True
        
    return False

# Calculate inventory statistics. Returns a dictionary or None if empty
def calculate_statistics(inventory):

    if not inventory:
        return None
    
    # calculate
    total_units = sum(product["quantity"] for product in inventory)
    total_value = sum(product["price"] * product["quantity"] for product in inventory)

    most_expensive = max(inventory, key = lambda product: product["price"])
    most_stock = max(inventory, key = lambda product: product["quantity"])
    
    statistics = {
        "total_units" : total_units,
        "total_value" : total_value ,
        "most_expensive" : {
            "name" : most_expensive ["name"],
            "price" : most_expensive ["price"] 
        },
        "most_stock" : {
            "name" : most_stock ["name"],
            "quantity" : most_stock ["quantity"]
        }
    }

    return statistics
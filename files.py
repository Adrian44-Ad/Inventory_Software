# Module for managing .CSV files
import csv

# Saves the inventory to a CSV file. Returns True if saved successfully, False if there was an error or the inventory is empty.
def save_CSV (inventory, path, include_header = True):

    if not inventory:
        print("The inventory is empty, cannot be save.")
        return False
    
    try:
        with open(path,"w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            if include_header:
                writer.writerow(["name", "price", "quantity"])
            
            for item in inventory:
                writer.writerow([
                    item["name"],
                    item["price"],
                    item["quantity"]
                ])

        print(f"Inventory saved in: {path}")
        return True
        
    except PermissionError:
        print("Error: You do not have permission to write to this path...")
        return False
    
    except Exception as ex:
        print("Unexpected error while saving: ", ex)
        return False


# Load an inventory from a CSV file. Returns a list of the inventory and errors
def load_CSV (path):

    inventory = []
    errors = 0

    try:
        with open(path, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            try:
                header = next(reader)
            except StopIteration:
                print("File not found...")
                return [], 0
            
            # Validate header
            if header != ["name", "price", "quantity"]:
                print("Error: Invalid Header...")
                return [], 0
            
            for row in reader:
                try:
                    if len(row) != 3:
                        raise ValueError
                    name = row[0]
                    price = float(row[1])
                    quantity = int(row[2])

                    if price < 0 or quantity < 0:
                        raise ValueError
                    
                    inventory.append({
                        "name" : name,
                        "price" : price,
                        "quantity" : quantity
                    })

                except ValueError:
                    errors += 1

        print(f"Loaded Products: {len(inventory)}")
        print(f"Invalid rows omited: {errors}")

        return inventory, errors

    except FileNotFoundError:
        print("Error: file not found...")
        return [], 0
    except UnicodeDecodeError:
        print("Error: File encoding problem issues...")
        return [], 0

    except Exception as Ex:
        print("Unespected Error: ", Ex)
        return [], 0
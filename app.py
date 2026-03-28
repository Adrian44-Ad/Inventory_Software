from services import *
from files import *

# Inventory stored on .CSV File
PATH = "inventory.csv"


# main function
def main ():

    # Inventory stored on .CSV File
    PATH = "inventory.csv"
    inventory = []

    title_ui = f'''
                    =============================
                    WELCOME TO INVENTORY SOFTWARE 
                    =============================\n
                '''
    print(title_ui)

    init_software = input("Do you want to start the system? (y/n): ").lower()
    print("=" * 60)

    # Main cycle
    while init_software == "y":

        # Show menu
        menu_ui = f'''
                        --- INVENTORY MENU ---
                        1. Add Product
                        2. Show products
                        3. Search products
                        4. Update products
                        5. Delete products
                        6. Show Statistics
                        7. Save CSV file
                        8. Load CSV file
                        9. Exit
                        ----------------------
                   '''
        print(menu_ui)

        ACTIVE_STATE = True
        option = int(input("Select an option from the menu: "))

        match option:
            
            case 1:

                i = 0

                while ACTIVE_STATE:
                
                    print("-" * 50)
                    print(f"Add your products #{i + 1}")
                    print("-" * 50)
                    name = input("Introduce the product name: ")
                    price = float(input("Introduce the product price: "))
                    quantity = int(input("Introduce the product quantity: "))

                    i = i + 1

                    add_product(inventory, name, price, quantity)

                    print("-" * 50)
                    repeat = input("Add another product? (y/n): ").lower()
                    print("-" * 50)

                    if repeat == "n":
                        break

            case 2:

                print(f'''
                           - INVENTORY LIST -
                      ============================
                      ''')
                
                if not inventory:
                    print("The inventory is empty!...")

                else:
                    for i, product in enumerate(inventory):

                        print(f'''
                            Product ID #{i + 1}
                          ===================
                            Name: {product['name']}
                            Price: {product['price']}
                            Quantity: {product['quantity']}
                          -------------------------------
                            ''')
                
            case 3:

                print(f'''
                           - SEARCH PRODUCTS -
                      ============================
                      ''')
                
                name = input("Enter product name to search: ")
                print("-" * 50)

                product = search_product(inventory, name)

                if product:
                    print(f'''
                            PRODUCT FOUND
                          =================
                          Name: {product['name']}
                          Price: {product['price']}
                          Quantity: {product['quantity']}
                        ---------------------------------
                           ''')
                else:
                    print("Product not Found!...")

            case 4:

                print(f'''
                           - UPDATE PRODUCTS -
                      ============================
                      ''')
                
                name = input("Enter product name to update: ")
                print("-" * 50)

                price_input = input("Enter new price (leave empty to skip): ")
                quantity_input = input("Enter new quantity (leave empty to skip): ")

                new_price = float(price_input) if price_input else None
                new_quantity = int(quantity_input) if quantity_input else None

                updated = update_product(inventory, name, new_price, new_quantity)

                if updated:
                    print("Product updated successfully!...")
                else:
                    print("Product not found!...")
        
            case 5:

                print(f'''
                           - DELETE PRODUCTS -
                      ============================
                      ''')
                
                name = input("Enter product name to delete: ")
                print("-" * 50)

                deleted = delete_product(inventory, name)

                if deleted:
                    print("Product deleted successfully!...")
                else:
                    print("Product not found")

            case 6:
                print(f'''
                           - INVENTORY STATISTICS -
                         ============================
                      ''')
                
                stats = calculate_statistics(inventory)

                if stats is None:
                    print("No data available. Inventory is empty!...")
                else:
                    print(f'''
                        Total Units: {stats['total_units']} |
                        Total Value: {stats['total_value']} |
                        =====================================
                           ''')
                    
                    print(f'''
                        - MOST EXPENSIVE PRODUCTS -
                        =============================
                        | Name: {stats['most_expensive']['name']} |
                        | Price: {stats['most_expensive']['price']} |
                        ________________________________________
                           ''')

                    print(f'''
                        - PRODUCTS WITH HIGHEST STOCK -
                        =============================
                        | Name: {stats['most_stock']['name']} |
                        | Quantity: {stats['most_stock']['quantity']} |
                        ________________________________________
                           ''')

            case 7:
                print(f'''
                           - SAVE INVENTORY TO CSV FILE -
                         ==================================
                      ''')
                
                saved = save_CSV(inventory, PATH)

                if saved:
                    print("Save operation completed successfully!...")
                else:
                    print("Save operation failed!...")


            case 8:
                print(f'''
                           - LOAD INVENTORY FROM CSV FILE -
                         ====================================
                      ''')
                
                loaded_inventory, errors = load_CSV(PATH)

                if not loaded_inventory:
                    print("No data Loaded!...")
                    break

                choice = input("Overwrite current inventory? (y/n): ").lower()

                if choice == "y":
                    inventory = loaded_inventory
                    action = "Replaced"
                else:
                    # Fusion
                    for new_product in loaded_inventory:
                        found = False

                        for product in inventory:
                            if product["name"].lower() == new_product["name"].lower():
                                product["quantity"] += new_product["quantity"]
                                product["price"] = new_product["price"]
                                found = True
                                break
                        if not found:
                            inventory.append(new_product)
                    
                    action = "Merged"

                # Show a summary
                print(f'''
                    |    LOAD SUMMARY    |
                    ======================
                    |
                    |- Products Loaded: {len(loaded_inventory)}
                    |- Invalid rows omitted: {errors}
                    |- Action: {action}
                    |__________________________________
                       ''')
                
            case 9:
                print(
                        '''
                            | Thank you for using Inventory Software! |
                            | See you next time!...                   |
                        '''
                    )
                
                break
            
            case _:
                print("Incorrect option...!")


if __name__ == "__main__":
    main()
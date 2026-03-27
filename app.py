from services import *
from files import *

# Inventory stored on .CSV File
PATH = "inventory.csv"


# main function
def main ():

    inventory = load_CSV(PATH)
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
                        ----------------------\n
                   '''
        print(menu_ui)

        ACTIVE_STATE = True
        option = int(input("Select an option from the menu: "))

        match option:
            case 1:
                while ACTIVE_STATE:
                    i = 1
                    print("-" * 50)
                    print(f"Add your products #{i}")
                    print("-" * 50)
                    name = input("Introduce the product name: ")
                    price = float(input("Introduce the product price: "))
                    quantity = int(input("Introduce the product quantity: "))

                    add_product(inventory, name, price, quantity)

                    i += 1

                    repeat = input("Add another product? (y/n): ").lower()

                    if repeat == "n":
                        break

            case 2:
                print("")
            case 3:
                print("")
            case 4:
                print("")
            case 5:
                print("")
            case 6:
                print("")
            case 7:
                print("")
            case 8:
                print("")
            case 9:
                print("")
            case _:
                print("Incorrect option...!")


if __name__ == "__main__":
    main()
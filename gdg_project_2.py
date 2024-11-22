cart = {}

# Function to add or update an item in the cart
def add_item(name, price, quantity):
    if name in cart:
        # Item exists, update quantity
        cart[name] = (price, cart[name][1] + quantity)
        print(f"Updated {name} in the cart. New quantity: {cart[name][1]}")
    else:
        # Item doesn't exist, add new item
        cart[name] = (price, quantity)
        print(f"Added {name} to the cart with quantity {quantity}.")

# Function to remove an item from the cart
def remove_item(name):
    if name in cart:
        del cart[name]
        print(f"Removed {name} from the cart.")
    else:
        print(f"Error: {name} not found in the cart.")

# Function to update the quantity of an existing item
def update_quantity(name, quantity):
    if name in cart:
        price = cart[name][0]
        cart[name] = (price, quantity)
        print(f"Updated {name} quantity to {quantity}.")
    else:
        print(f"Error: {name} not found in the cart.")

# Function to calculate the total cost of the items in the cart
def calculate_total():
    total = sum(price * quantity for price, quantity in cart.values())
    return total

# Function to display the contents of the cart
def view_cart():
    if cart:
        print("\nShopping Cart:")
        print(f"{'Item Name':<20} {'Price':<10} {'Quantity':<10} {'Total':<10}")
        print("-" * 50)
        for name, (price, quantity) in cart.items():
            total = price * quantity
            print(f"{name:<20} {price:<10} {quantity:<10} {total:<10}")
        print("-" * 50)
        print(f"Total Cost: {calculate_total():.2f}")
    else:
        print("Your cart is empty.")

# User Interface - Main Menu
def shopping_cart_system():
    while True:
        print("\n--- Shopping Cart System ---")
        print("1. Add/Update Item")
        print("2. Remove Item")
        print("3. Update Item Quantity")
        print("4. View Cart")
        print("5. Calculate Total")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))
            add_item(name, price, quantity)
        
        elif choice == '2':
            name = input("Enter item name to remove: ")
            remove_item(name)
        
        elif choice == '3':
            name = input("Enter item name to update: ")
            quantity = int(input("Enter new quantity: "))
            update_quantity(name, quantity)
        
        elif choice == '4':
            view_cart()
        
        elif choice == '5':
            total = calculate_total()
            print(f"Total cost of items in the cart: {total:.2f}")
        
        elif choice == '6':
            print("Exiting the shopping cart system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

# Start the shopping cart system
if __name__ == "__main__":
    shopping_cart_system()

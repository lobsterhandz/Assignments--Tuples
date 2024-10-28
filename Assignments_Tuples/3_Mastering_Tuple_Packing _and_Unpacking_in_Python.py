# 3. Customer Order Processing
# Task: Unpack each tuple and format the order details.

def process_orders(orders):
    for customer_name, product, quantity in orders:
        print(f"Customer: {customer_name}, Product: {product}, Quantity: {quantity}")

# System loop to get user input for customer orders with exception handling
orders = []
while True:
    try:
        customer_name = input("Enter customer name (or 'done' to finish): ").strip()
        if customer_name.lower() == 'done':
            break
        if not customer_name:
            print("Customer name cannot be empty. Please try again.")
            continue
        product = input("Enter product: ").strip()
        if not product:
            print("Product name cannot be empty. Please try again.")
            continue
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be a positive integer. Please try again.")
            continue
        orders.append((customer_name, product, quantity))
    except ValueError:
        print("Invalid input. Please enter a valid quantity (an integer).")
    except Exception as e:
        print(f"An error occurred: {e}")

process_orders(orders)

"""
Build a customer report for
Sales Orders
"""

def print_customer_address(name, city, state, street):
    """Print a composed address"""
    customer_address =f"{name}\n {street}\n {city}, {state}"
    print(customer_address)

def calculate_order_total(qty, cost):
    """calculate the total by multiply qty by cost"""
    return qty * cost

def print_customer_report():
    """Pirnt a customer report"""
    print("Shipping Address:")
    print_customer_address(
        "Customer Name",
        "Boston",
        "MA",
        "440 Tremont Street"
    )
    #print("Order Total:")
    total=calculate_order_total(11, 11.11)
    round_total =round(total, 2)
    print(f"Order Total: {round_total}")


print_customer_report()

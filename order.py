# 1. Store toppings in a list
# 2. get the customer name
# 3. User a conditional to apply Pricing
#     * small = $10
#     * Medium = $15
#     * Large = $20
# 4. Print an order summary using an f String
# 5. Use a loop to print each topping
# 6. refactor into a reusable function

def calculate_total(size, toppings):
    if size.lower() == 'small':
        base_price = 10
    elif size.lower() == 'medium':
        base_price = 15
    else:
        base_price = 20

    # add an additional 1.50 for each topping
    topping_cost = len(toppings) * 1.50
    total = base_price + topping_cost
    return total


def takeOrder(name, size, toppings):

    total = calculate_total(size, toppings)
    
    order = f"Name: {name}\n"
    order += f"Size: {size}\n"
    order += f"Toppings:\n"
    for topping in toppings:
        order += f"- {topping}\n"
    order += f"Total: {total:.2f}"

    print(order)
    print("============================")


takeOrder('Nathan', 'medium', ['bacon', 'pepperoni', 'meatballs'])
takeOrder('Sarah', 'large', ['peas', 'beans'])
takeOrder('Bob', 'small', ['grapes', 'tomato', 'onions'])
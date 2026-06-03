# 1. Store toppings in a list
# 2. get the customer name
# 3. User a conditional to apply Pricing
#     * small = $10
#     * Medium = $15
#     * Large = $20
# 4. Print an order summary using an f String
# 5. Use a loop to print each topping
# 6. refactor into a reusable function


def takeOrder(name, size, toppings):

    if size.lower() == 'small':
        total = 10
    elif size.lower() == 'medium':
        total = 15
    else:
        total = 20
    
    order = f"Name: {name}\n"
    order += f"Size: {size}\n"
    order += f"Toppings:\n"
    for topping in toppings:
        order += f"- {topping}\n"
    order += f"Total: {total}"

    print(order)
    print("============================")


takeOrder('Nathan', 'medium', ['bacon', 'pepperoni', 'meatballs'])
takeOrder('Sarah', 'large', ['peas', 'beans'])
takeOrder('Bob', 'small', ['grapes', 'tomato', 'onions'])
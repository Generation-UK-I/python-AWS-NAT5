from pizza_module import *
      

size = input("What size pizza would you like? [small/medium/large]:\n")
type = input("Would you like deep or thin pizza?:\n")
crust = input("Would you like a stuffed or plain crust? [stuffed/plain]:\n")
order_1 = pizza(size, type, crust)

sauce = input("Would you like tomato or BBQ sauce?\n")
order_1.sauce(sauce)

cheese = input("Would you like mozzarella or vegan cheese?\n")
order_1.cheese(cheese)

toppings = []

while True:
    prompt = "What toppings would you like?\n"
    prompt += "Type 'done' when finished\n\n"
    prompt += "\t- Peppers\n\t- Pepperoni\n\t- Ham\n\t- Chicken\n\t- Mushrooms\n"
    choice = input(prompt)
    if choice == "done":
        break
    else:
        toppings.append(choice)

order_1.toppings(toppings)

order_1.cook()

order_1.describe_pizza()

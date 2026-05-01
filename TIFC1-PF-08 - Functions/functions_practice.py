import time

class pizza():
    def __init__(self, size, type, crust):
        self.size = size
        self.type = type
        self.crust = crust
        print(f"You have ordered a {size} {type} pizza,with a {crust} crust...")
        
    def sauce(self, sauce_type):
        self.sauce_type = sauce_type
        print(f"Adding {sauce_type} sauce...")

    def cheese(self, cheese_type):
        self.cheese_type = cheese_type
        print(f"Adding {cheese_type} cheese...")
        
    def toppings(self, toppings):
        self.toppings = toppings
        for item in toppings:
            print(f"Adding {item} to your pizza...")
            
    def cook (self):
        print("Cooking your pizza...")
        time.sleep(1)
        print("Cooking your pizza...")
        time.sleep(1)
        print("Cooking your pizza...")
        time.sleep(1)
        print("Your pizza is cooked")
        
    def describe_pizza(self):
        print(f"We've made you a {self.size}, {self.type}, {self.crust} crust pizza, with {self.sauce_type} sauce, {self.cheese_type} cheese, and ")
        for item in self.toppings:
            print(f"- {item}")
        print("toppings.\nThank you for your order")
        

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

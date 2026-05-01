coffee_dict = {
    'cappuccino' : {
        'price' : 3.50,
        'description' : 'espresso, steamed milk, and foam'
    },
    'latte' : {
        'price' : 3.00,
        'description' : 'espresso, steamed milk'
    }
}

def order_coffee():
    print("Coffee menu:")
    while True:
        for key in coffee_dict:
            print(f"- {key}")
        your_coffee = input("Which coffee would you like to order? [or 'quit']\n")
        if your_coffee == "cappuccino":
            print("creating your cappuccino...")
        elif your_coffee == "latte":
            print("creating your latte...")
        elif your_coffee == "quit":
            break
        else:
            print("Please make a valid selection.")

while True:
    prompt = "Welcome to Frankie & Scout's bookshop\n"
    prompt += "Please choose from the following options\n"
    prompt += "1) Order Coffee\n2) Order Food\n0) Quit\n"

    user_option = input(prompt)
    if user_option == "1":
        order_coffee()
    elif user_option == "2":
        print("functionality not yet ready")
    elif user_option == "0":
        break
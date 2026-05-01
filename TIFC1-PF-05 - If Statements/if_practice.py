food = input("What would you like to order? \n")

if food.lower() == 'croissant':
    print("You have bought a croissant!")
elif food.lower() == 'cinnamon roll':
    print("You have ordered a cinnamon roll warmed up!")
elif food.lower() == ' brownie':
    print("You have ordered a brownie, warmed up with a scoop of ice cream.")
elif food.lower() == 'cheese danish':
    print("You have ordered a cheese danish to go!")
elif food.lower() == 'sandwich':
    print("You have ordered a sandwich to go!")
else:
    print("This is not available... So I will go home!")
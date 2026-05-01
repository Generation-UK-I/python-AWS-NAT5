
# my_dictionary = {
#     "Ant" : "A small insect / A technical instrutor",
#     "Bat" : "A small flying mammal / A crime fighter",
#     "Cat" : "A household pet that thinks it's better than you",
#     "Dog" : "Man's best friend; Dogs > cats",
#     "Elephant" : "Hairless Mammoth, big nose",
#     "Fox" : "Hairless Mammoth, big nose",
#     "Goose" : "A big honking bird",
#     "Haggis" : "a small, shaggy animal native to the Highlands",
#     "Iguana" : "A tiny dinosaur",
#     "Jellyfish" : "A floating carrier bag which makes you pee on yourself",
#     "Koala" : "Aka 'Drop-bear' Australia's most dangerous marsupial",
#     "Lion" : "Star of various Disney movies, usually singing",
#     "Monkey" : "Like a child, but hairy",
#     "Narwhal" : "Sea unicorn",
#     "Ostrich" : "Danger chicken",
#     "Panda" : "Monochrome teddy bear",
#     "Quail" : "Tiny chicken, used by posh people for target practice",
#     "Rabbit" : "Long eared, incessant reproducer",
#     "Snake" : "Danger noodle",
#     "Tigger" : "Winnie the Pooh's bouncy buddy",
#     "Urukai" : "Ugly bad dudes in LOTR",
#     "Vulture" : "Smaller danger chicken",
#     "X" : "Danger noodle"
# }

# while True:
#     selection = input("Lookup an animal or type 'exit' to quit:\n")
    
#     if selection in my_dictionary.keys():
#         print(f"An {selection} is {my_dictionary[selection]}")
#     elif selection == "exit":
#         break
#     else:
#         print("Please make a valid selection...")



cats = {
    'weasley' : { 
        'fur': 'white and ginger',
        'eyes': 'yellow',
        'toes': 'pink'
        },

    'noche' : { 
        'fur': 'black',
        'eyes': 'green',
        'toes': 'pink'
        },

    'bigglesworth' : { 
        'fur': 'none',
        'eyes': 'red',
        'toes': 'cloven hoofs'
        }
}

for cat_name, cat_info in cats.items():
    print(cat_name)
    print(cat_info)



my_list = ["Frankie", "Scout", "Weasley", "Noche"]

for pet in my_list:
    print(pet)
    











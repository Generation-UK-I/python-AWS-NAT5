def describe_pet(pet_first_name, pet_last_name):
    my_pet = {'first': pet_first_name, 'last': pet_last_name}
    return my_pet


def dog_food(foods):
    print(foods)
    for food in foods:
        dinner = f"Do you fancy {food} for dinner tonight?"
        print(dinner)
           



def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
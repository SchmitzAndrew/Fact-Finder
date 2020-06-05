from lists_for_seperation import city_name_list
from lists_for_seperation import people_list

def add_term(user_search):
    print('''You can your search query to 2 different lists. 
    1. City
    2. Person''')
    list_addition_choice = input("C for city and P for person")
    if list_addition_choice == C:
        add_to_city_name_list(user_search)
    elif list_addition_choice == P:
        add_to_people_list(user_search)
    else:
        print("Not a valid selection")
        add_term(user_search)

def add_to_city_name_list(user_search):
    city_name_list.append(user_search)
    print("Your term: " + user_search + "has been added to our list. Thanks for the submission. :\)")
    return city_name_list
    #return to start



def add_to_people_list(user_search):
    people_list.append(user_search)
    print("Your term: " + user_search + "has been added to our list. Thanks for the submission. :\)")
    return people_list

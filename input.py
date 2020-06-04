#imports
from lists_for_seperation import people_list
from lists_for_seperation import years_list
from lists_for_seperation import city_name_list
from lists_for_seperation import country_name_list
from lists_for_seperation import geoname_id_list


#Recieve user input and split into what kind of data

def take_user_input():
    user_search = input("Enter your search here.")
    return user_search

def find_category(user_search):
    if user_search in people_list:
        people_search()
    elif user_search in years_list:
        years_search()
    elif user_search in city_name_list:
        city_search()
    elif user_search in country_name_list:
        country_search()
    elif user_search in geoname_id_list:
        geoname_search()
    else:
        user_search_not_found()
        user_search

def user_search_not_found(user_search):
    print("Your search term: " + user_search + "did not match our database :(. Would you like to...")
    print('''Search the web for your term[1]
    Add the term to the database[2]
    Repeat search with new term[3]''')
    user_search_not_found_choice = input("S,A, or R")
    if user_search_not_found_choice == S:
        search_for_outlier_term()
    elif user_search_not_found_choice == A:
        add_term()
    elif user_search_not_found_choice == R:
        take_user_input()
    else:
        print("Not a valid chouce.")
        user_search_not_found()



        






#imports
from lists_for_seperation import people_list, years_list, city_name_list, country_name_list
from searcher import people_search, years_search, city_search, country_search, search_for_outlier_term
from add_file_to_database import add_term

print("Welcome to my Python statistics finder.")

#Recieve user input and split into what kind of data
def take_user_input_and_sort():
    user_search = input("Enter your search here. Our database has information on people and places, so searching for those will give you the most accurate response.").lower()
    if user_search in people_list:
        people_search(user_search)
    elif user_search in years_list:
        years_search(user_search)
    elif user_search in city_name_list:
        city_search(user_search)
    elif user_search in country_name_list:
        country_search(user_search)
    else:
        user_search_not_found(user_search)

def user_search_not_found(user_search):
    print("Your search term: " + user_search + " did not match our database :(. Would you like to...")
    print('''Search the web for your term[1]
    Add the term to the database[2]
    Repeat search with new term[3]''')
    user_search_not_found_choice = input("S,A, or R").upper()
    if user_search_not_found_choice == "S":
        search_for_outlier_term(user_search)
    elif user_search_not_found_choice == "A":
        add_term(user_search)
    elif user_search_not_found_choice == "R":
        take_user_input_and_sort(user_search)
    else:
        print("Not a valid choice.")
        take_user_input_and_sort(user_search)

take_user_input_and_sort()



        






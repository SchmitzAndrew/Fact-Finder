import wikipedia

def people_search(user_search):
    person_query = user_search + " person"
    search = wikipedia.search(person_query)
    if search[1]:
        query = search[1]
    else:
        query = search[0]
    print(wikipedia.summary(query, sentences = 10000))

def years_search(user_search):
    year_query = user_search + "year"
    search = wikipedia.search(year_query)
    if search[1]:
        query = search[1]
    else:
        query = search[0]
    print(wikipedia.summary(query, sentences=10000))

def city_search(user_search):
    city_query = user_search + "city"
    search = wikipedia.search(city_query)
    if search[1]:
        query = search[1]
    else:
        query = search[0]
    print(wikipedia.summary(query, sentences=10000))

def country_search(user_search):
    city_query = user_search + "country"
    search = wikipedia.search(city_query)
    if search[1]:
        query = search[1]
    else:
        query = search[0]
    print(wikipedia.summary(query, sentences=10000))

#raw search since not matched with a topic
def search_for_outlier_term(user_search):
    wikipedia.search(user_search)



